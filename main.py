from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from ai_ops_env.environment import OpsEnv
from ai_ops_env.models import Action
from ai_ops_env.tasks import get_tasks
from ai_ops_env.grader import grade_easy
from inference import run_baseline
import subprocess
import sys
import os

app = FastAPI()
env = OpsEnv()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>AI Ops System</title>
<style>
body {
    background: #000;
    margin: 0;
    font-family: "Courier New", monospace;
    overflow: hidden;
}
.terminal {
    padding: 20px;
    color: #00ff88;
    height: 100vh;
    box-sizing: border-box;
}
.terminal-header {
    background: #111;
    color: #00ff88;
    padding: 15px 20px;
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 20px;
    border-bottom: 1px solid #00ff88;
    padding-bottom: 10px;
    text-align: center;
    position: relative;
}
.digital-clock {
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 14px;
    font-family: "Courier New", monospace;
    color: #00ff88;
    opacity: 0.9;
}
.api-btn {
    position: absolute;
    right: 20px;
    top: 50%;
    transform: translateY(-50%);
    background: transparent;
    color: #00ff88;
    border: 1px solid #00ff88;
    padding: 8px 16px;
    font-family: "Courier New", monospace;
    font-size: 12px;
    cursor: pointer;
    border-radius: 4px;
    transition: all 0.3s ease;
}
.api-btn:hover {
    background: #00ff88;
    color: #000;
}
.status-badge {
    position: absolute;
    right: 160px;
    top: 50%;
    transform: translateY(-50%);
    color: #00ff88;
    font-family: "Courier New", monospace;
    font-size: 12px;
    opacity: 0.9;
}
.terminal-body {
    white-space: pre-wrap;
    line-height: 1.6;
    font-size: 14px;
    height: calc(100vh - 100px);
    overflow-y: auto;
    padding-right: 10px;
    border: 2px solid #00ff88;
    border-radius: 8px;
    padding: 15px;
    margin: 10px;
    background: #000;
    box-sizing: border-box;
}
/* Custom scrollbar */
.terminal-body::-webkit-scrollbar {
    width: 8px;
}
.terminal-body::-webkit-scrollbar-track {
    background: #000;
    border: 1px solid #00ff88;
}
.terminal-body::-webkit-scrollbar-thumb {
    background: #00ff88;
    border-radius: 4px;
}
.terminal-body::-webkit-scrollbar-thumb:hover {
    background: #00d4ff;
}
/* Section Colors */
.summary { color: #00d4ff; }
.insights { color: #ffd700; }
.reward { color: #ff9f1c; }
.system { color: #c77dff; }
.info { color: #00ff88; }
.step { color: #00ff88; }
.start { color: #00d4ff; }
.end { color: #ffd700; }
.error { color: #ff4444; }
/* Blinking cursor */
.cursor::after {
    content: "_";
    animation: blink 1s infinite;
    color: #00ff88;
}
@keyframes blink {
    0% { opacity: 1; }
    50% { opacity: 0; }
    100% { opacity: 1; }
}
/* Command style */
.command {
    color: #00ff88;
    margin: 5px 0;
}
/* Loading animation - removed for plain text status */
</style>
</head>
<body>
<div class="terminal">
    <div class="terminal-header">
        <div class="digital-clock" id="digitalClock"></div>
        AI Ops System - Autonomous Decision Engine (Real-time AI Optimization)
        <div class="status-badge">[STATUS] SYSTEM ACTIVE *</div>
        <button onclick="openDocs()" class="api-btn">View API Docs</button>
    </div>
    <div id="output" class="terminal-body cursor">
        <div class="command">> Initializing system...</div>
        <div>[STATUS] Processing tasks...</div>
    </div>
</div>
<script>
function openDocs() {
    window.open('/docs', '_blank');
}
function updateDigitalClock() {
    const now = new Date();
    
    // Terminal-style timestamp: YYYY-MM-DD HH:MM:SS
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0');
    const day = now.getDate().toString().padStart(2, '0');
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    
    const timestamp = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    
    document.getElementById('digitalClock').innerHTML = `[SYSTEM TIME] ${timestamp}`;
}
// Update clock immediately and then every second
updateDigitalClock();
setInterval(updateDigitalClock, 1000);
function typeOutput(text) {
    const output = document.getElementById("output");
    let i = 0;
    function typing() {
        if (i < text.length) {
            output.innerHTML += text.charAt(i);
            i++;
            setTimeout(typing, 5);
        }
    }
    typing();
}
function formatLogLine(line) {
    if (line.includes('[INFO]')) {
        return `<span class="info">${line}</span>`;
    } else if (line.includes('[START]')) {
        return `<span class="start">${line}</span>`;
    } else if (line.includes('[STEP]')) {
        return `<span class="step">${line}</span>`;
    } else if (line.includes('[END]')) {
        return `<span class="end">${line}</span>`;
    } else if (line.includes('[ERROR]')) {
        return `<span class="error">${line}</span>`;
    } else if (line.includes('Total Reward:')) {
        // Highlight final score with fire emoji and performance rating
        const rewardMatch = line.match(/Total Reward: ([\d.]+) \/ ([\d.]+)/);
        if (rewardMatch) {
            const score = parseFloat(rewardMatch[1]);
            const maxScore = parseFloat(rewardMatch[2]);
            const percentage = (score / maxScore) * 100;
            
            let performance = '';
            if (percentage >= 80) performance = 'EXCELLENT PERFORMANCE';
            else if (percentage >= 60) performance = 'GOOD PERFORMANCE';
            else if (percentage >= 40) performance = 'MODERATE PERFORMANCE';
            else performance = 'NEEDS IMPROVEMENT';
            
            return `<span class="reward">🔥 FINAL SCORE: ${score} / ${maxScore} (${performance})</span>`;
        }
        return `<span class="reward">${line}</span>`;
    } else if (line.includes('[STATUS]')) {
        return `<span class="summary">${line}</span>`;
    } else if (line.includes('[API]')) {
        return `<span class="info">${line}</span>`;
    } else if (line.includes('[AI SUMMARY]')) {
        return `<span class="insights">${line}</span>`;
    } else if (line.includes('[COMPLETE]')) {
        return `<span class="summary">${line}</span>`;
    } else if (line.includes('=== EXECUTION SUMMARY ===')) {
        return `<br><span class="summary">${line}</span>`;
    } else if (line.includes('=== DECISION INSIGHTS ===')) {
        return `<br><span class="insights">${line}</span>`;
    } else if (line.includes('=== REWARD BREAKDOWN ===')) {
        return `<br><span class="reward">${line}</span>`;
    } else if (line.includes('=== SYSTEM INFO ===')) {
        return `<br><span class="system">${line}</span>`;
    } else if (line.includes('Reward') || line.includes('reward')) {
        return `<span class="reward">${line}</span>`;
    } else if (line.includes('# SYSTEM:')) {
        return `<span class="system">${line}</span>`;
    } else if (line.includes('# AI_REASON:')) {
        return `<span class="system">${line}</span>`;
    } else if (line.includes('Status') || line.includes('Total') || line.includes('Average') || line.includes('Execution')) {
        return `<span class="info">${line}</span>`;
    } else if (line.includes('High Priority') || line.includes('Medium Priority') || line.includes('Low Priority') || line.includes('System Efficiency')) {
        return `<span class="insights">${line}</span>`;
    } else if (line.startsWith('Step')) {
        return `<span class="reward">${line}</span>`;
    } else if (line.startsWith('Model') || line.startsWith('Mode') || line.startsWith('Execution Type')) {
        return `<span class="system">${line}</span>`;
    } else if (line.startsWith('>')) {
        return `<div class="command">${line}</div>`;
    } else if (line.trim() === '') {
        return '<br>';
    }
    return line;
}
async function runInference() {
    const output = document.getElementById("output");
    output.innerHTML = '<div class="command">> Initializing AI Ops System...</div><div>[STATUS] Processing tasks...</div>';
    
    try {
        const response = await fetch('/inference-raw');
        const data = await response.json();
        
        let logOutput = '<div class="command">> AI Ops Optimization Pipeline Started</div>';
        
        // Process logs if they exist
        if (data.logs && Array.isArray(data.logs)) {
            data.logs.forEach(log => {
                if (log && log.trim()) {
                    logOutput += formatLogLine(log) + '\\n';
                } else if (log === '') {
                    logOutput += '<br>';
                }
            });
        }
        
        // Add API info line first
        logOutput += '<div>[API] /step | /state | /reset available</div>';
        
        // Add completion status
        logOutput += '<div>[STATUS] Optimization complete</div>';
        
        // Add AI summary
        logOutput += '<div>[AI SUMMARY] System prioritized high-impact tasks for maximum efficiency</div>';
                
        output.innerHTML = logOutput;
        
        // Auto-scroll to bottom to show all content
        output.scrollTop = output.scrollHeight;
        
    } catch (error) {
        output.innerHTML = `<div class="command">> Error: ${error.message}</div><span class="error">[ERROR] Failed to connect to AI Ops engine</span>`;
    }
}
// Auto-start when page loads
window.onload = function() {
    setTimeout(runInference, 1500);
};
</script>
</body>
</html>
"""

@app.api_route("/reset", methods=["GET", "POST"])
def reset():
    state = env.reset()
    return {"state": state}

@app.api_route("/step", methods=["GET", "POST"])
def step(action: Action = None):
    # For GET requests, provide a default action or return error
    if action is None:
        return {"error": "Action parameter required for step endpoint"}
    
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs,
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/state")
def state():
    return env.state_view()

@app.get("/tasks")
def tasks():
    return get_tasks()

@app.api_route("/grader", methods=["GET", "POST"])
def grader_endpoint(action: Action = None):
    # For GET requests, provide a default action or return error
    if action is None:
        return {"error": "Action parameter required for grader endpoint"}

    task = next((t for t in env.state.tasks if t.id == action.task_id), None)

    if not task:
        return {"score": 0.0}

    score = grade_easy(action, task)
    return {"score": score}

@app.get("/baseline")
def baseline():
    return run_baseline()

@app.get("/inference-raw")
def inference_raw():
    try:
        # Add current directory to Python path and run inference.py
        env = os.environ.copy()
        env['PYTHONPATH'] = os.getcwd()
        
        # Run inference.py and capture its console output
        result = subprocess.run(
            [sys.executable, "-c", "from inference import run_baseline; run_baseline()"],
            capture_output=True,
            text=True,
            cwd=os.getcwd(),
            env=env
        )
        
        # Check if the output is already JSON (from ai_ops_env/inference.py)
        stdout_content = result.stdout.strip()
        if stdout_content.startswith('{"logs":'):
            # Parse the JSON directly from stdout
            try:
                import json
                return json.loads(stdout_content)
            except json.JSONDecodeError:
                # If parsing fails, fall back to processing as logs
                pass
        
        # Process the output to extract logs (fallback for other inference functions)
        output_lines = stdout_content.split('\n')
        logs = []
        total_reward = 0.0
        
        for line in output_lines:
            if line.strip():
                logs.append(line.strip())
                # Extract reward from STEP lines
                if '[STEP]' in line and 'reward=' in line:
                    try:
                        reward_part = line.split('reward=')[1].split()[0]
                        total_reward += float(reward_part)
                    except:
                        pass
        
        # Calculate average score from logs
        reward_count = len([log for log in logs if '[STEP]' in log and 'reward=' in log])
        average_score = round(total_reward / reward_count, 2) if reward_count > 0 else 0.0
        
        return {
            "logs": logs,
            "result": {
                "total_reward": round(total_reward, 2),
                "average_score": average_score,
                "status": "SUCCESS"
            },
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
            
    except Exception as e:
        return {
            "logs": [f"[ERROR] {str(e)}"],
            "result": {
                "total_reward": 0.0,
                "status": "ERROR"
            },
            "stdout": "",
            "stderr": str(e),
            "returncode": -1,
            "error": str(e)
        }

@app.get("/run")
def run():
    from inference import run_baseline
    
    result = run_baseline()
    
    return {
        "tasks": result["tasks"],
        "score": result["score"],
        "done": True
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)

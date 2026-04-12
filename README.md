 <h1 align="center"><u> 💻 AI OPS RL Intelligence Environment System ♾️ </u></h1>

<div align="center">

| Title          | AI Ops System |
|----------------|--------------|
| Emoji          | 🤖          |
| Color From     | blue         |
| Color To       | green        |
| SDK            | docker       |
| Python Version | 3.10         |
| App port       | 7860         |
| App File       | app.py       |
| Tag            | OPENENV      |

</div>

Autonomous Incident Detection & Recovery using Reinforcement learning environment for Task Prioritization. 
- “From tasks to intelligence — building systems that learn to decide.”

- Category: AI Systems • Reinforcement Learning • DevOps Automation

---
## 🔗 Overview :

- OpenEnv-compatible AI Ops environment for autonomous incident management
- Simulates real-world system behavior (CPU, memory, traffic, errors)
- Reinforcement learning agent performs step-by-step decision making
- Structured pipeline: detection → analysis → decision → execution → recovery
- Adaptive reward mechanism enables continuous improvement
- Stochastic environment models real-world uncertainty
- Deterministic mode ensures reproducible evaluation (seed-based)
- Generates transparent, explainable execution logs for each step
- Designed for scalable, self-healing infrastructure systems

---
## 🔗 Why This Matters :

- Modern systems face unpredictable failures that require rapid and intelligent response
- Manual incident handling is slow, error-prone, and not scalable
- Traditional rule-based systems lack adaptability in dynamic environments
- Reinforcement learning enables autonomous, data-driven decision making
- Simulated environments allow safe testing without impacting real infrastructure
- Adaptive systems can continuously improve performance over time
- Explainable AI builds trust by making decisions transparent and traceable
- Enables the vision of self-healing, autonomous infrastructure systems
---
## 🔗 Environment at glance :

- OpenEnv-compatible RL environment tailored for real-world AI Ops scenarios
- Models dynamic system states (CPU, memory, error rate, latency) under varying load conditions
- Supports multi-scenario incident simulation (traffic spikes, resource saturation, system instability)
- Action space designed for autonomous recovery (analysis, detection, scaling, stabilization)
- Reward function shaped by system improvement, efficiency, and recovery success
- Adaptive reward mechanism learns from historical action effectiveness
- Stochastic behavior introduces real-world uncertainty and non-determinism
- Deterministic mode (seed-based) enables reproducible and consistent evaluation
- Handles both success and failure episodes with clear termination logic
- Designed to simulate self-healing infrastructure through sequential decision-making

---
## 🔗 Core Intelligence & Capabilities :

- Autonomous Incident Resolution: End-to-end pipeline for detecting, analyzing, and resolving system failures without human intervention
- Reinforcement Learning Decision Engine: Sequential action selection using reward-driven optimization (State → Action → Reward → Next State)
- Multi-Scenario Simulation: Handles diverse system conditions including CPU spikes, memory pressure, traffic surges, and latency issues
- Stochastic Environment Modeling: Introduces real-world uncertainty for robust and realistic agent behavior
- Adaptive Reward Mechanism: Continuously adjusts rewards based on action effectiveness and system improvement
- Deterministic Mode (Reproducibility): Seed-based execution ensures consistent and verifiable results
- Explainable AI Execution Logs: Transparent step-by-step reasoning for every decision and action taken
- Failure-Aware Execution: Supports action failures and recovery retries for realistic system behavior
- Phase-Based Decision Pipeline: Structured flow across detection, analysis, decision, execution, and recovery stages
- Performance-Driven Optimization: Measures system improvement through CPU, memory, error rate, and latency reduction
- OpenEnv Compliance: Fully aligned with required output format and evaluation standards
- Scalable & Modular Design: Easily extendable to real-world infrastructure and deployment scenarios
   
---
## 🔗 System Architecture :
The system operates through a structured, step-by-step pipeline where a user-triggered event initializes the environment with current system metrics such as CPU usage, memory, error rate, and latency. The AI agent first detects any anomalies and performs a detailed analysis to identify the root cause of the issue. Based on the observed state, the reinforcement learning agent selects the most optimal action using its learned policy and reward feedback.

<div align="center">
 
```
[USER INPUT / TRIGGER]
 ↓
[ENVIRONMENT INITIALIZATION]
(State: CPU, Memory, Error, Latency)
 ↓
[PHASE 1: DETECTION]
Identify system anomaly (e.g., HIGH_CPU)
 ↓
[PHASE 2: ANALYSIS]
Analyze system state and root cause
 ↓
[PHASE 3: DECISION]
RL Agent selects optimal action
 ↓
[PHASE 4: EXECUTION]
Execute action (scale / balance / mitigate)
 ↓
[PHASE 5: RECOVERY]
System stabilizes and metrics improve
 ↓
[REWARD CALCULATION]
Evaluate performance improvement
 ↓
[STATE UPDATE]
Update system metrics (next state)
 ↓
[TERMINATION CHECK]
Stable? → YES → END  
Else → Continue next step
 ↓
[FINAL OUTPUT]
[END] + Summary + System Metrics
```

</div>

---


## 🔗 Workflow :
The system operates through a structured, step-by-step pipeline where a user-triggered event initializes the environment with current system metrics such as CPU usage, memory, error rate, and latency. The AI agent first detects any anomalies and performs a detailed analysis to identify the root cause of the issue. Based on the observed state, the reinforcement learning agent selects the most optimal action using its learned policy and reward feedback.

<div align="center">

```
[USER TRIGGER / TASK INPUT]
 ↓
[INITIALIZE ENVIRONMENT STATE]
(CPU, Memory, Error Rate, Latency)
 ↓
[DETECT SYSTEM EVENT]
Identify anomaly (e.g., HIGH_CPU)
 ↓
[ANALYZE CURRENT STATE]
Evaluate system condition & root cause
 ↓
[RL DECISION ENGINE]
Select optimal action based on policy & reward
 ↓
[EXECUTE ACTION]
(Scale resources / Load balance / Stabilize)
 ↓
[SYSTEM FEEDBACK]
Update metrics based on action impact
 ↓
[REWARD EVALUATION]
Calculate reward from system improvement
 ↓
[STATE TRANSITION]
Move to next updated system state
 ↓
[TERMINATION CHECK]
Stable? → YES → END  
Else → Continue loop
 ↓
[FINAL OUTPUT]
Structured logs + Summary + Final system metrics
```
</div>

---
## 🔗 Reward System (Core Logic) :

The system evaluates each decision using a weighted scoring model:
it transforms simple system metrics into intelligent, learning behavior that consistently makes the right decisions at the right time.
This reward system represents cutting-edge RL engineering that combines theoretical excellence with practical validation compliance, creating an AI environment that learns, adapts, and improves with every interaction!
- Learns from experience: Good actions get better over time.
- Penalizes mistakes: Wrong decisions lose points
- Rewards speed: Faster solutions earn more
```
Final reward = (0.4 × priority_score) + (0.4 × action_score) + (0.2 × speed_bonus)

Example :
High CPU incident + AI scales resources quickly:

reward = (0.4 × 0.99) + (0.4 × 0.99) + (0.2 × 0.8)
        = 0.396 + 0.396 + 0.16
        = 0.95
```
## 🔗 Reward Progression Logic :

<div align="center">
 
| Step  | Action                 | Reward | Status    |
|-------|------------------------|--------|-----------|
| **1** | analyze_system_state   | 0.40   | Detection |
| **2** | detect_high_cpu        | 0.40   | Analysis  |
| **3** | evaluate_scaling       | 0.44   | Decision  |
| **4** | scale_resources        | 0.66   | Execution |
| **5** | stabilize_system       | 0.66   | Recovery  |
| **Final** | Average Score      | **0.51** | Success  |


</div>

---

## 🔗 Performance Adjustment :

<div align="center">

| Performance Level | Reward Adjustment | New Range      |
|------------------|------------------|----------------|
| **Excellent (>70%)** | +0.02           | 0.42 – 0.99    |
| **Good (40–70%)**    | ±0.00           | 0.40 – 0.99    |
| **Poor (<30%)**      | -0.02           | 0.38 – 0.97    |

</div>

</div>

---

## 🔗 Score Calculation :

Final score is computed as:
Normalized average of rewards across all steps
Ensures score remains in range **(0, 1)** as required by evaluation
```
final_score = sum(all_step_rewards) / number_of_steps
###  Example

Step 1: 0.40
Step 2: 0.40  
Step 3: 0.44
Step 4: 0.66
Step 5: 0.66

final_score = (0.40 + 0.40 + 0.44 + 0.66 + 0.66) / 5
             = 2.56 / 5
             = 0.51
final_score = max(0.01, min(final_score, 0.99))
```
---

## 🔗 Score Meaning :

Higher Score = Smarter AI = Better System Recovery! 
<div align="center">

| Score Range | Performance Level | Meaning |
|-------------|------------------|---------|
| **0.90 – 0.99** | Excellent  | Near-perfect AI decisions, optimal system recovery |
| **0.70 – 0.89** | Very Good  | Strong decisions, effective problem resolution |
| **0.50 – 0.69** | Good       | Solid performance, successful recovery |
| **0.30 – 0.49** | Average    | Acceptable decisions, partial success |
| **0.10 – 0.29** | Poor       | Weak decisions, minimal improvement |
| **0.01 – 0.09** | Very Poor  | Failed decisions, system still critical |

</div>

---
## 🔗 Tasks in this system now :
The AI Ops Environment features ten comprehensive tasks that simulate real-world IT operations scenarios. These tasks are carefully designed to test different aspects of AI decision-making, from basic monitoring to complex optimization challenges.

The system includes two easy-level tasks focused on fundamental operations like system health monitoring and log analysis. These serve as entry points for the AI to demonstrate basic problem-solving capabilities. The majority of tasks (eight) are medium-complexity scenarios that involve sophisticated operations such as load balancing optimization, anomaly detection, resource allocation, incident response automation, and performance tuning.

<div align="center">

| Task                          | Description                                             | 
|-------------------------------|---------------------------------------------------------|
| Basic System Monitoring       | Monitor basic system health and status                  |
| Simple Log Analysis           | Analyze basic system logs for errors                    |
| Load Balancing Optimization   | Distribute workload across servers efficiently          | 
| Anomaly Detection Monitoring  | Identify unusual patterns in system behavior            | 
| Resource Allocation Planning  | Optimize CPU, memory, and storage usage                 |
| Incident Response Automation  | Automatically handle system emergencies                 |
| Performance Tuning Engine     | Optimize system performance parameters                  | 
| Cost Efficiency Optimization  | Reduce operational costs while maintaining performance  | 
| Intelligent Scheduling System | Optimize task scheduling for maximum efficiency         | 
| Database Performance Tuning   | Optimize database queries and indexing for performance  | 
</div>


---
## 🔗 How to Run

The AI Ops Environment runs as a web dashboard where five intelligent agents collaborate to solve IT incidents through a five-phase pipeline. Users watch in real-time as the system detects problems, makes decisions, executes solutions, and learns from each experience to improve future performance.
Users interact through an intuitive web interface that displays live system metrics, allows task and event selection, and provides real-time visibility into the AI's decision-making process. The dashboard shows the progression through each phase, displays reward scores, and demonstrates how the system transforms critical states (like 95% CPU usage) into healthy ones (like 32% CPU usage) through intelligent automation.

## 🔗 Local Setup :

```bash
# 1. Clone repository
git clone <your-repo-url>
cd ai-ops-environment-meta--main

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start server
uvicorn app:app --host 0.0.0.0 --port 7860

# 4. Open browser
http://localhost:7860
```
```
# Required for LLM integration
export API_BASE_URL="https://your-llm-proxy.com/v1"
export API_KEY="your-api-key-here"
export MODEL_NAME="Qwen/Qwen2.5-72B-Instruct"

# Or create .env file
echo "API_BASE_URL=https://your-llm-proxy.com/v1" > .env
echo "API_KEY=your-api-key-here" >> .env
echo "MODEL_NAME=Qwen/Qwen2.5-72B-Instruct" >> .env
```
## 🔗 Run AI interface :
```
# Random mode
python inference.py

# Deterministic mode 
python inference.py load_balancing_optimization HIGH_CPU 42

# Local development (port 7860)
uvicorn app:app --host 0.0.0.0 --port 7860 --reload

# Different port if 7860 is busy
uvicorn app:app --host 0.0.0.0 --port 8080 --reload

```
## 🔗  Docker setup :
```
# Build and run
docker build -t ai-ops-env .
docker run -p 7860:7860 ai-ops-env
```
## 🔗 Hugging face (optional) :
```
# 1. Create new Space
# Go to huggingface.co → Spaces → Create New Space
# Choose: Docker, Python 3.9, Public

# 2. Push to HF Space
git clone https://huggingface.co/spaces/your-username/your-space-name
cd your-space-name
git remote add origin https://huggingface.co/spaces/your-username/your-space-name

# 3. Copy your files
cp -r /path/to/your/ai-ops-environment/* .

# 4. Set environment variables
# In Space Settings → Variables:
# API_BASE_URL=your-llm-proxy-url
# API_KEY=your-api-key
# MODEL_NAME=Qwen/Qwen2.5-72B-Instruct

# 5. Push and deploy
git add .
git commit -m "Deploy AI Ops Environment"
git push
```
```
# Test locally before pushing
openenv validate

# Check HF Space logs for errors
# Space URL: https://your-username-your-space-name.hf.space

- Select task from dropdown
- Choose event type
- (Optional) Enter seed for reproducible results
- Click "Run System"
- Watch AI solve the problem!
```
## 🔗 Troubleshooting:
```
# Check if server is running
curl http://localhost:7860/

# Check logs for errors
# Look for "ERROR" or "CRITICAL" messages

# Test API endpoints
curl http://localhost:7860/reset
curl http://localhost:7860/run?task=load_balancing_optimization&event=HIGH_CPU
```

---

## 🔗 Agent Purpose :

<div align="center">

|  Agent           | Primary Function       | Key Actions                                      | Success Metric                |
|------------------|------------------------|--------------------------------------------------|-------------------------------|
| Detection Agent  | Find system problems   | analyze_system_state, detect_high_cpu            | Early issue identification    |
| Analysis Agent   | Understand root causes | evaluate_scaling, classify_leak_severity         | Accurate problem diagnosis    |
| Decision Agent   | Choose best solutions  | select_optimal_strategy, evaluate_cleanup_options| Optimal action selection      |
| Execution Agent  | Implement fixes        | scale_resources, restart_service                 | Successful problem resolution |
| Recovery Agent   | Stabilize system       | stabilize_system, monitor_performance            | System health restoration     |

</div>

---

## 🔗 AI Intelligence capabilities :

- Autonomous Decision-Making: Dynamically selects optimal actions based on real-time system state and reward feedback
- Adaptive Learning Mechanism: Continuously improves strategies by learning from past actions and outcomes
- Context-Aware Analysis: Understands system conditions (CPU, memory, errors) to make informed decisions
- Uncertainty Handling: Operates effectively under stochastic and unpredictable system behavior
- Explainable Reasoning: Provides transparent, step-by-step insights into every decision and action taken

---
## 🔗 Action & Observation Space :

- The agent observes the system state through key performance metrics:
CPU Usage
Memory Usage
Error Rate
Latency
These values represent the current condition of the system and guide decision-making.

- Action Space
The agent can perform the following actions to manage and stabilize the system:
Analyze System State
Detect System Anomaly
Evaluate Recovery Strategy
Scale Resources
Redistribute Load
Stabilize System

- Interaction Mechanism
At each step:
The agent observes the current state
Selects an action from the action space
Receives a reward based on system improvement
Transitions to a new state
This loop continues until the system reaches a stable condition or the episode terminates.

---
## 🔗 Project Structure :

```bash
ai-ops-rl-intelligence-envrionment /
├── 📄 app.py                  # FastAPI server & API endpoints
├── 📄 inference.py            # AI inference engine
├── 📄 openenv.yaml            # Environment configuration
├── 📄 Dockerfile              # Container setup
├── 📄 requirements.txt        # Python dependencies
├── 📄 pyproject.toml          # Project metadata
│
├── 📁 ai_ops_env/             # Core AI Ops environment
│   ├── 📄 __init__.py
│   ├── 📄 environment.py      # Main simulation engine
│   ├── 📄 grader.py           # Scoring & evaluation logic
│   ├── 📄 tasks.py            # Task definitions
│   ├── 📄 reward_learning.py  # Adaptive reward system
│   └── 📄 policy_learning.py  # Strategy optimization
│
├── 📁 static/                 # Frontend assets
│   ├── 📄 ui.js               # Interactive dashboard logic
│   ├── 📄 style.css           # Styling
│   └── 📄 script.js           # Additional scripts
│
├── 📁 templates/              # HTML templates
│   └── 📄 index.html          # Main UI page
│
├── 📁 agents/                 # AI agents
│   └── 📄 rules_agent.py      # Rule-based agent logic
│
├── 📁 .windsurf/              # IDE workflows & automation
│   └── 📁 workflows/
│       ├── 📄 run-inference.md
│       └── 📄 tasks.md
│
└── 📁 .git/                   # Git version control
```
---

## 🔗 Tech Stack :

| Component              | Technology             | Purpose                          |
|------------------------|------------------------|----------------------------------|
| Backend Framework      | FastAPI                | Web server & API endpoints       |
| AI Integration         | OpenAI API             | LLM model communication          |
| Environment Simulation | Python                 | Core system logic                |
| Reinforcement Learning | Custom RL              | Learning & adaptation            |
| Frontend               | HTML/CSS/JavaScript    | Web dashboard                    |
| Containerization       | Docker                 | Deployment & portability         |
| Package Management     | pip / requirements.txt | Dependency management            |
| Configuration          | YAML                   | Environment setup                |
| Web Server             | Uvicorn                | ASGI server                      |
| Validation             | OpenEnv                | Compliance checking              |

---
## 🔗 Environment Variables use by this system :

| Variable     | Description                     | Example Value                     |
|--------------|---------------------------------|-----------------------------------|
| API_BASE_URL | LLM proxy endpoint URL          | https://your-llm-proxy.com/v1     |
| API_KEY      | Authentication key for LLM API  | sk-your-api-key-here              |
| MODEL_NAME   | LLM model identifier            | Qwen/Qwen2.5-72B-Instruct         |
```
echo "API_BASE_URL=https://your-llm-proxy.com/v1" > .env
echo "API_KEY=sk-your-api-key-here" >> .env
echo "MODEL_NAME=Qwen/Qwen2.5-72B-Instruct" >> .env
```
---

## 🔗 Future Enhancements :

- Integration with real-world cloud infrastructure (AWS, Kubernetes)
- Deployment of fully autonomous self-healing systems in production
- Advanced multi-agent collaboration for complex incident handling
- Incorporation of predictive analytics for proactive failure prevention
- Support for large-scale distributed system environments
- Integration with real-time monitoring tools (Prometheus, Grafana)
- Enhanced reward modeling using advanced RL algorithms
- Continuous online learning from live system feedback
- Expansion to domain-specific environments (finance, healthcare, IoT)
- Improved explainability using advanced AI reasoning techniques
- Human-in-the-loop control for hybrid decision systems
- Optimization for edge computing and resource-constrained systems

---
## 🔗 Contribution :

B. SAI GANESH
                    
    AI Developer | System Builder | Innovator
---

## 🔗 Conclusion :

This project demonstrates a complete and intelligent AI Ops environment powered by reinforcement learning, where an autonomous agent can detect, analyze, and resolve system incidents through structured decision-making. By combining stochastic simulation, adaptive learning, and explainable execution, the system moves beyond static automation toward dynamic, self-improving infrastructure management. It highlights the potential of AI-driven operations to reduce manual intervention, improve system reliability, and enable scalable, self-healing systems. This work represents a strong step toward the future of autonomous, resilient, and intelligent system orchestration.
As the system grows, it will incorporate deeper reasoning capabilities, adaptive learning strategies, and real-time integrations with production systems—transforming it from a simulation framework into a fully autonomous, enterprise-ready AI operations engine.





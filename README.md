 <h1 align="center"><u> 💻 AI OPS Intelligence System ♾️ </u></h1>

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

Autonomous Decision-Making Environment for Task Prioritization. 
- “From tasks to intelligence — building systems that learn to decide.”

« Status: Live • Deployed 
 |  Category: AI Systems • Reinforcement Learning • DevOps Automation»

---

## 🔗 Live Demo :

 Hugging Face Space:
👉 https://ganesh756-ai-ops-system.hf.space/

 Interactive API Docs (Swagger UI):
👉 https://ganesh756-ai-ops-system.hf.space/docs

---
## 🔗 Overview :

 This project introduces a Hybrid AI Ops Autonomous Decision Engine that leverages both Reinforcement Learning (RL) and Large Language Model (LLM) reasoning to optimize task execution in dynamic environments. The system is designed to intelligently manage and prioritize tasks under varying system conditions such as load, resource availability, and operational constraints.
At its core, the solution functions as an adaptive decision-making agent that continuously observes the system state, evaluates task priorities, and selects optimal actions to maximize efficiency. By incorporating a reward-driven learning mechanism, the system improves its performance step-by-step, demonstrating progressive optimization across execution cycles.

---                  

## 🔗 Key Features :

-  Hybrid RL + LLM decision intelligence  

- Transparent reward calculation system  

-  Performance scoring (Efficiency, Quality, Confidence)  

-  Step-by-step decision tracing (Explainable AI)  

-  REST API endpoints for integration   
   
---
## 🔗 System Architecture :
<div align="center">
 
```
User Request / Validator
        ↓
     FastAPI Server (main.py)
        ↓
     AI Engine (inference.py)
        ↓
 RL Decision + LLM Reasoning
        ↓
 Task Execution (ai_ops_env)
        ↓
 Structured Output ([START][STEP][END])
```
</div>

---
## 🔗 Reward System (Core Logic) :

The system evaluates each decision using a weighted scoring model:
```
Final Reward: round((w_priority * priority_score) + (w_action * action_score) + (w_efficiency * efficiency_score), 2)
```
## 🔗 Score Calculation :

Final score is computed as:
Normalized average of rewards across all steps
Ensures score remains in range **(0, 1)** as required by evaluation
###  Example
```
Rewards: `0.27, 0.39, 0.51, 0.63, 0.75`  
Score ≈ 0.51
```
---
## 🔗 Reward Progression Logic :

<div align="center">

| Phase                     | Description                                                                 | Example Rewards        |
|---------------------------|-----------------------------------------------------------------------------|-----------------------|
| **Early Steps** *(Exploration Phase)* | Lower rewards reflect initial uncertainty while evaluating actions        | 0.27, 0.39            |
| **Middle Steps** *(Learning Phase)*   | Moderate rewards indicate improved decision-making with feedback          | 0.51, 0.63            |
| **Final Step** *(Optimization Phase)* | Higher reward represents convergence toward optimal strategy              | 0.75+                 |

</div>

---
## 🔗 Step-wise Optimization :

<div align="center">

| Step | Description |
|------|-------------|
| **1. Analyze** | Analyzes current system load and task context |
| **2. Select Action** | Selects an action (assign, etc.) based on priority |
| **3. Evaluate** | Evaluates the outcome using a reward function |

</div>

---
## 🔗 Endpoints of the system :

<div align="center">

| Endpoint | Description                |
|----------|----------------------------|
| `/run`      | AI pipeline               |
| `/step`  | Execute optimization step  |
| `/state` | View current tasks         |
| `/reset` | Reset environment          |

</div>

---
## 🔗 Tech Stack :

<div align="center">

| Category                | Technology                          |
|------------------------|--------------------------------------|
| Backend               | FastAPI                              |
| AI Logic              | Reinforcement Learning + LLM         |
| Environment Simulation| Custom AI Ops Environment            |
| Deployment            | Hugging Face Spaces (Docker)         |
| UI                    | Terminal-style Web Interface         |

</div>

---
## 🔗 Structure Overview :

- inference.py → Executes tasks, logs "[START][STEP][END]", computes score
- ai_ops_env/ → Core RL environment with real-world task simulation
- tasks/ → Defines task scenarios (easy → medium → hard)
- evaluation/ → Scoring and performance metrics
- agent/ & agents/ → Decision-making logic (LLM + fallback hybrid)
- main.py / server/ → API + UI interface
- configs/ → Environment and runtime configurations
- Dockerfile → Enables containerized deployment on Hugging Face

---
## 🔗 Tasks :

<div align="center">

| Task Name                        | Description                                                                          
|----------------------------------|-------------------------------------------------------------------------------------|
| Load Balancing Optimization      | Distributes workloads across systems to avoid overload and ensure smooth performance
| Anomaly Detection & Monitoring   | Identifies unusual patterns or failures in system behavior                 
| Resource Allocation Planning     | Allocates CPU, memory, and network resources efficiently                 
| Incident Response Automation     | Handles system failures and alerts automatically                            
| Performance Tuning Engine        | Adjusts system parameters for optimal performance                            
| Cost Efficiency Optimization     | Reduces unnecessary resource usage and operational costs 
| Intelligent Scheduling           | Predicts system failure
| basic_system_monitoring          | Monitor basic system health and status
| simple_log_analysis              | Analyze basic system logs for errors
| database_performance_tuning      | Optimize database queries and indexing for better performance

</div>

---
## 🔗 Output format :
```
[START] task=<task_name> env=<environment> model=<model>
[STEP] step=<n> action=<action> reward=<value> done=<true|false> error=<msg|null>
[END] success=<true|false> steps=<n> score=<value> rewards=<r1,r2,...>
```
## 🔗 LLM Integration :
The system uses the OpenAI-compatible client:
```
Python
client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("API_KEY")
)
```
Supports proxy-based evaluation (LiteLLM)
No hardcoded credentials
Fully environment-driven

---
## 🔗 How to Run :
```
git clone https://github.com/YOUR_USERNAME/ai-ops-system.git
cd ai-ops-system
```
```
pip install -r requirements.txt
```
```
set API_KEY= os.getenv("API_KEY")
set API_BASE_URL= os.getenv("API_BASE_URL")
set MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
```
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open in browser:
```
http://127.0.0.1:8000 (for local only)
```

## 🔗 Setup Instructions :

Follow these steps to run the project locally.

##  Clone the Repository :

git clone https://github.com/YOUR_USERNAME/ai-ops-system.git
cd ai-ops-system

##  Install Dependencies :
```
pip install -r requirements.txt
```
##  Set Environment Variables :
 Linux /  Mac
```
export API_KEY= os.getenv("API_KEY")
export API_BASE_URL= os.getenv("API_BASE_URL")
export MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
```
 Windows
```
set API_KEY= os.getenv("API_KEY")
set API_BASE_URL= os.getenv("API_BASE_URL")
set MODEL_NAME=Qwen/Qwen2.5-72B-Instruct
```
##  Run the Application
```
uvicorn main:app --host 0.0.0.0 --port 8000
```
 Open in Browser
 ## Run locally 
 ```
python inference.py
 ```

##  Docker Setup (Optional) :

Build and run using Docker:
```
docker build -t ai-ops-system .
docker run -p 8000:8000 ai-ops-system
```
---
## 🔗 AI Intelligence :

This system combines Reinforcement Learning and LLM reasoning to enable:

- Adaptive decision-making  
- Reward-based learning  
- Context-aware task prioritization  
- Explainable AI with transparent logs  

The system continuously optimizes decisions based on feedback loops.

---
## 🔗 Action & Observation Space :

##  Observation :
The observation represents the current system state including:
- Task description
- Priority level
- System status
- Previous decisions

##  Action :
The agent can perform actions such as:
- Prioritize task
- Assign resource
- Optimize execution step

##  Reward :
The reward is calculated based on:
- Task priority handling
- Decision correctness
- Efficiency of execution
---
## 🔗 Project Structure :

```bash
ai-ops-system/
│
├── inference.py              # OpenEnv inference script (core evaluation logic)
├── main.py                   # FastAPI server + UI handling
├── client.py                 # API / client interaction layer
├── models.py                 # Data models (actions, observations, rewards)
├── openenv.yaml              # OpenEnv configuration and metadata
│
├── ai_ops_env/               # Reinforcement Learning environment
│   ├── state.py              # Task definitions (Email, Support, Incident)
│   └── ...                   # Environment logic and helpers
│
├── agent/                    # Core agent logic
├── agents/                   # Multi-agent / extended logic
├── core/                     # Core system components
├── utils/                    # Utility functions
├── configs/                  # Configuration files
│
├── tasks/                    # Task-specific implementations
├── evaluation/               # Evaluation and scoring logic
├── tests/                    # Testing modules
│
├── server/                   # Backend server components
├── docs/                     # Documentation assets
│
├── Dockerfile                # Container setup (Hugging Face deployment)
├── requirements.txt          # Python dependencies
├── pyproject.toml            # Project configuration
├── uv.lock                   # Dependency lock file
│
├── README.md                 # Main project documentation
├── CODE_OF_CONDUCT.md        # Community guidelines
├── LICENSE                   # License information
├── BENCHMARK.md              # Benchmark details
│
├── .gitignore                # Ignored files
└── .deployignore             # Deployment exclusions
## 🔗 Screenshots :
```
<img width="1918" height="766" alt="image" src="https://github.com/user-attachments/assets/6c9464e9-07f1-4ba0-854e-4bfaccdaed7e" />

---
## 🔗 Contribution :
B. SAI GANESH
                    
    AI Developer | System Builder | Innovator
---
## 🔗 Conclusion :
This project demonstrates the foundation of an intelligent AI Ops Autonomous System that combines Reinforcement Learning and LLM-driven reasoning to simulate real-world operational decision-making. While the current system delivers structured, scalable, and reliable optimization across multiple tasks, it is designed as a continuously evolving environment.
As the system grows, it will incorporate deeper reasoning capabilities, adaptive learning strategies, and real-time integrations with production systems—transforming it from a simulation framework into a fully autonomous, enterprise-ready AI operations engine.





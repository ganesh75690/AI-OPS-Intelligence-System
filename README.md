🚀 AI Ops Intelligence

Autonomous Decision-Making Environment for Task Prioritization

> 🟢 Status: Live • Deployed • Fully Functional
🧪 Live Demo

🌐 Hugging Face Space:
👉 https://ganesh756-ai-ops-system.hf.space/

📘 API Docs (Recommended):
👉 https://ganesh756-ai-ops-system.hf.space/docs

---
🧠 Overview

AI Ops Intelligence is a simulation environment designed to train and evaluate AI agents for real-world operational decision-making.
It mimics a business operations workflow where agents must:

- Analyze incoming tasks
- Prioritize them based on urgency
- Choose appropriate actions
- Optimize outcomes using reward-based feedback
This environment follows the OpenEnv standard for building agent training systems.

---
🎯 Problem Statement

Modern organizations face challenges in:
- Managing high volumes of tasks
- Prioritizing critical incidents
- Efficient resource allocation

Manual handling leads to inefficiencies and delays.
---

💡 Solution
This project provides a structured AI training environment where agents learn to:

- 📌 Classify task priorities
- ⚙️ Decide correct actions (assign, escalate, ignore)
- 📊 Optimize decisions using reward-based evaluation


<img width="1916" height="867" alt="image" src="https://github.com/user-attachments/assets/6449ce57-3030-4a9b-8323-2cbe1845a452" />

<img width="1916" height="853" alt="image" src="https://github.com/user-attachments/assets/d9433477-a144-403d-9e8c-766663d80404" />

<img width="1918" height="907" alt="image" src="https://github.com/user-attachments/assets/ea8e931e-983f-4c44-9b3f-f922db6c27ee" />


---

🧩 Features

- ✅ OpenEnv-compatible API ("reset", "step", "state")
- ✅ Multi-level task system:
  - Easy → Priority classification
  - Medium → Action selection
  - Hard → Multi-task decision-making
- ✅ Reward-based grading system (0–1 scoring)
- ✅ Baseline agent for reproducible evaluation
- ✅ Dockerized deployment
- ✅ Live API hosted on Hugging Face

## 💡 Why This Matters

This system demonstrates how AI can assist in:

- Reducing operational delays
- Improving system reliability
- Automating decision workflows
- Enhancing productivity in enterprise environments


## 🚀 System Capabilities

- Intelligent task prioritization
- Adaptive decision-making
- Reward-driven optimization
- Scalable environment simulation
- API-first design for integration

---

⚙️ API Endpoints

Endpoint| Description
"/reset"| Reset environment
"/step"| Execute agent action
"/state"| View current state
"/tasks"| List all tasks
"/grader"| Evaluate actions
"/baseline"| Run baseline agent

---

🤖 Baseline Agent

A simple rule-based agent is included to:

- Interact with the environment
- Generate reproducible results
- Provide evaluation benchmarks


## 🧠 Learning Mechanism

The agent improves through:

1. Observing system state  
2. Taking actions  
3. Receiving reward signals  
4. Adjusting strategy  

This loop enables optimization over time.

---

📈 Reward System

The environment uses reward shaping:

- ✔ Correct decisions → Positive reward
- ⚠ Partial correctness → Partial reward
- ❌ Incorrect decisions → Penalty

This enables realistic AI training scenarios.

---

🧱 Project Structure

ai-ops-environment/
│
├── environment.py
├── models.py
├── state.py
├── tasks.py
├── grader.py
├── inference.py
├── main.py
├── Dockerfile
├── requirements.txt
└── openenv.yaml

---

🚀 How to Run Locally

pip install -r requirements.txt
uvicorn main:app --reload

Open:

http://127.0.0.1:8000/docs

---

🐳 Docker Support

docker build -t ai-ops-env .
docker run -p 7860:7860 ai-ops-env

---

🌍 Real-World Applications

- DevOps automation
- IT incident management
- Customer support systems
- Workflow optimization

## 📊 Evaluation Results

| Task Level | Score |
|-----------|------|
| Easy      | 0.9  |
| Medium    | 0.7  |
| Hard      | 0.5  |

**Average Score:** 0.7

---

🏆 Innovation

Unlike traditional apps, this project focuses on:

«🔥 Training AI agents in a simulated decision environment
🔥 Combining task prioritization with reward-based learning
🔥 Providing reproducible evaluation via baseline + grader»

---

📜 License

This project is licensed under the MIT License.

---

🙌 Author

Ganesh

---

⭐ Final Note

This project demonstrates how AI agents can be trained to make intelligent operational decisions in real-world environments using structured simulations.

---

from ai_ops_env.environment import OpsEnv
from ai_ops_env.models import Action


# -------------------------------
# HEALTH SYSTEM
# -------------------------------
def calculate_system_health(tasks):
    high = sum(1 for t in tasks if t.priority == "high")
    medium = sum(1 for t in tasks if t.priority == "medium")
    low = sum(1 for t in tasks if t.priority == "low")

    total = len(tasks) if tasks else 1

    health = 1 - ((high * 0.6 + medium * 0.3 + low * 0.1) / total)
    return max(0, min(1, health))


# -------------------------------
# SMART AGENT (ADVANCED)
# -------------------------------
def smart_agent(task, health_score):
    if task.priority == "high":
        return "assign", 0.95, "Critical task"
    elif task.priority == "medium":
        if health_score < 0.5:
            return "assign", 0.80, "System unstable"
        return "assign", 0.65, "Normal handling"
    else:
        if health_score < 0.3:
            return "assign", 0.55, "Low but critical system"
        return "ignore", 0.40, "Low priority"


# -------------------------------
# LOGGING (STRICT FORMAT)
# -------------------------------
def log_start(task, env, model):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step, action, reward, done, error=None):
    error_val = error if error else "null"
    done_val = str(done).lower()

    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={done_val} error={error_val}",
        flush=True,
    )


def log_end(success, steps, rewards, avg_health, efficiency):
    rewards_str = ",".join([f"{r:.2f}" for r in rewards])


    print(
        f"[END] success={str(success).lower()} steps={steps} rewards={rewards_str}",
        flush=True,
    )


# -------------------------------
# MAIN EXECUTION
# -------------------------------
def run_baseline():
    env = OpsEnv()
    obs = env.reset()

    rewards = []
    steps = 0
    health_history = []

    # ✅ START LOG 
    log_start("ai_ops_optimization", "ai_ops_env", "elite_agent_vFinal")

    try:
        while steps < 5:

            #  SYSTEM HEALTH
            health_score = calculate_system_health(obs.tasks)
            health_history.append(health_score)

            for task in obs.tasks:

                #  SMART DECISION
                action_type, confidence, reason = smart_agent(task, health_score)

                action = Action(
                    task_id=task.id,
                    action_type=action_type
                )

                obs, reward, done, _ = env.step(action)

                rewards.append(reward)

                #  STRONG ACTION STRING 
                action_str = (
                    f"{action_type}"
                    f"|p:{task.priority}"
                    f"|c:{confidence:.2f}"
                    f"|h:{health_score:.2f}"
                )

                #  STEP LOG 
                log_step(
                    step=steps + 1,
                    action=action_str,
                    reward=reward,
                    done=done,
                    error=None
                )

                if done:
                    break

            steps += 1

            if done:
                break

    except Exception as e:
        log_step(
            step=steps,
            action="error",
            reward=0.0,
            done=True,
            error=str(e)
        )

    finally:
        total_reward = sum(rewards)

        #  SUCCESS
        success = total_reward > 0

        #  HEALTH METRIC
        avg_health = sum(health_history) / len(health_history) if health_history else 0

        #  EFFICIENCY METRIC
        efficiency = total_reward / (len(rewards) if rewards else 1)

        #  END LOG 
        log_end(success, steps, rewards, avg_health, efficiency)


# -------------------------------
# ENTRY POINT
# -------------------------------
if __name__ == "__main__":
    run_baseline()

from environment import OpsEnv
from models import Action

def simple_agent(task):
    # basic logic
    if task.priority == "high":
        return "assign"
    elif task.priority == "medium":
        return "assign"
    else:
        return "ignore"


def run_baseline():
    env = OpsEnv()
    obs = env.reset()

    total_reward = 0
    steps = 0

    while True:
        for task in obs.tasks:
            action_type = simple_agent(task)

            action = Action(
                task_id=task.id,
                action_type=action_type
            )

            obs, reward, done, _ = env.step(action)

            total_reward += reward
            steps += 1

            if done:
                break

        if done:
            break

    avg_score = total_reward / steps if steps > 0 else 0

    return {
        "total_reward": total_reward,
        "steps": steps,
        "average_score": round(avg_score, 2)
    }


if __name__ == "__main__":
    result = run_baseline()
    print(result)

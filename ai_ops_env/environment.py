from ai_ops_env.models import Action, Observation
from ai_ops_env.grader import grade_easy, grade_medium, grade_hard
from ai_ops_env.state import EnvState

class OpsEnv:
    def __init__(self):
        self.state = EnvState()
        self.reset()

    def reset(self):
        self.state.reset()
        return Observation(tasks=self.state.tasks, message="Environment reset")

    def step(self, action: Action):
        self.state.step_count += 1

        task = next((t for t in self.state.tasks if t.id == action.task_id), None)

        if not task:
            return Observation(tasks=self.state.tasks, message="Invalid task"), -1, True, {}

        # Get task difficulty from state
        task_difficulty = "medium"  # default
        for task_def in self.state.current_task if hasattr(self.state, 'current_task') and self.state.current_task else []:
            if isinstance(task_def, dict) and task_def.get('name') == task.description:
                task_difficulty = task_def.get('difficulty', 'medium')
                break

        # Use appropriate grader based on task difficulty
        if task_difficulty == "easy":
            reward = grade_easy(action, task)
        elif task_difficulty == "hard":
            reward = grade_hard([action], [task])
        else:  # medium
            reward = grade_medium(action, task)

        # small penalty for bad action
        if action.action_type == "ignore" and task.priority == "high":
            reward -= 0.5

        reward = max(0.0, min(reward, 1.0))

        done = self.state.step_count >= 5

        return Observation(tasks=self.state.tasks, message="Step executed"), reward, done, {}

    def state_view(self):
        # Fix callable issue - return dict instead of state object
        return {"tasks": self.state.tasks}

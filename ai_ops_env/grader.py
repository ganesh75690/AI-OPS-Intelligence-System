def grade_easy(action, task):
    # Handle both dict and object tasks
    priority = task.get("priority") if isinstance(task, dict) else getattr(task, "priority", "medium")
    
    if priority == "high" and action.action_type == "assign":
        return 0.99  # Force below 1.0
    elif action.action_type == "assign":
        return 0.5
    return 0.01  # Force above 0.0


def grade_medium(action, task):
    score = 0.0
    
    # Handle both dict and object tasks
    priority = task.get("priority") if isinstance(task, dict) else getattr(task, "priority", "medium")

    if priority == "high" and action.action_type == "assign":
        score += 0.6
    if priority == "medium" and action.action_type == "assign":
        score += 0.3
    if action.action_type == "escalate":
        score += 0.2

    return max(0.01, min(score, 0.99))


def grade_hard(actions, tasks):
    score = 0.0

    for action in actions:
        # Find task by ID (handle both dict and object tasks)
        task = None
        if isinstance(tasks, list):
            task = next((t for t in tasks if (t.get("id") if isinstance(t, dict) else getattr(t, "id", None)) == action.task_id), None)
        
        if not task:
            continue

        # Get priority (handle both dict and object tasks)
        priority = task.get("priority") if isinstance(task, dict) else getattr(task, "priority", "medium")

        if priority == "high" and action.action_type == "assign":
            score += 0.3
        elif priority == "medium" and action.action_type == "assign":
            score += 0.15
        elif action.action_type == "ignore":
            score -= 0.3

    return max(0.01, min(score, 0.99))

class RuleBasedAgent:
    """
    A simple rule-based agent for baseline decision-making.

    This agent uses predefined rules to select actions
    based on task priority and system state.
    """

    def act(self, state):
        """
        Select action based on simple rules.

        Args:
            state (dict): Current environment state

        Returns:
            str: Action
        """
        priority = state.get("priority", "low")

        if priority == "high":
            return "escalate"
        elif priority == "medium":
            return "assign"
        else:
            return "ignore"

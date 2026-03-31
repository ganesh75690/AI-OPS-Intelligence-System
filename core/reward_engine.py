class RewardEngine:
    """
    Handles reward computation for actions taken by the agent.

    Designed for extensibility with advanced reward shaping
    techniques in future versions.
    """

    def __init__(self):
        pass

    def compute_reward(self, action, expected_action):
        """
        Compute reward based on action correctness.

        Args:
            action (str): Action taken by agent
            expected_action (str): Correct action

        Returns:
            float: Reward score
        """
        if action == expected_action:
            return 1.0
        return 0.0

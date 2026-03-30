"""
RL Agent for AI Ops Environment

This module provides a simple agent interface and a baseline RL-style agent
to interact with the OpenEnv-compatible environment.
"""

from typing import Dict, Any
import random


class BaseAgent:
    """
    Base class for all agents.
    """

    def select_action(self, state: Dict[str, Any]) -> str:
        """
        Select an action based on the current state.

        Args:
            state (dict): Current environment state

        Returns:
            str: Action to take
        """
        raise NotImplementedError("select_action must be implemented")


class RuleBasedAgent(BaseAgent):
    """
    Simple rule-based agent (acts like a baseline RL policy).
    """

    def select_action(self, state: Dict[str, Any]) -> str:
        priority = state.get("priority", "low")

        if priority == "high":
            return "escalate"
        elif priority == "medium":
            return "assign"
        else:
            return random.choice(["assign", "ignore"])


class RandomAgent(BaseAgent):
    """
    Fully random agent (useful for comparison baseline).
    """

    ACTIONS = ["assign", "escalate", "resolve", "ignore"]

    def select_action(self, state: Dict[str, Any]) -> str:
        return random.choice(self.ACTIONS)


def run_episode(env, agent: BaseAgent) -> float:
    """
    Run a single episode in the environment.

    Args:
        env: OpenEnv-compatible environment
        agent (BaseAgent): Agent instance

    Returns:
        float: Total reward obtained
    """

    state = env.reset()
    done = False
    total_reward = 0.0

    while not done:
        action = agent.select_action(state)
        state, reward, done, _ = env.step(action)
        total_reward += reward

    return total_reward


def evaluate_agent(env, agent: BaseAgent, episodes: int = 10) -> float:
    """
    Evaluate agent over multiple episodes.

    Args:
        env: Environment instance
        agent (BaseAgent): Agent
        episodes (int): Number of runs

    Returns:
        float: Average reward
    """

    total = 0.0

    for _ in range(episodes):
        total += run_episode(env, agent)

    return total / episodes


if __name__ == "__main__":
    # Example usage (safe for local testing only)
    from ai_ops_env.environment import OpsEnv

    env = OpsEnv()
    agent = RuleBasedAgent()

    avg_reward = evaluate_agent(env, agent, episodes=5)

    print(f"Average Reward: {avg_reward:.2f}")

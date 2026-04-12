"""
AI Operations Manager Environment for task prioritization and decision-making
"""

__version__ = "1.0"

# Make grader functions available at package level for validation
try:
    from ai_ops_env.grader import grade_easy, grade_medium, grade_hard
    __all__ = ['grade_easy', 'grade_medium', 'grade_hard']
except ImportError:
    pass


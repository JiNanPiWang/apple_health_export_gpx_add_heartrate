import os


# getting content root directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

PROJECT_ROOT = parent
WORKOUT_ROUTES_WITH_HR = os.path.join(PROJECT_ROOT, 'workout-routes-added-hr')
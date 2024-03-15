"""
Strava Possible values: ('AlpineSki', 'BackcountrySki', 'Canoeing', 'Crossfit', 'EBikeRide',
    'Elliptical', 'Golf', 'Handcycle', 'Hike', 'IceSkate', 'InlineSkate', 'Kayaking', 'Kitesurf',
    'NordicSki', 'Ride', 'RockClimbing', 'RollerSki', 'Rowing', 'Run', 'Sail', 'Skateboard',
    'Snowboard', 'Snowshoe', 'Soccer', 'StairStepper', 'StandUpPaddling', 'Surfing', 'Swim',
    'Velomobile', 'VirtualRide', 'VirtualRun', 'Walk', 'WeightTraining', 'Wheelchair', 'Windsurf', 'Workout', 'Yoga')
            Type detected from file overrides, uses athlete's default type if
            not specified
Apple Health Kit reference: https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype
"""


type_trans = {'HKWorkoutActivityTypeCycling': 'Ride',
              'HKWorkoutActivityTypeRunning': 'Run',
              'HKWorkoutActivityTypeSwimming': 'Swim',
              'HKWorkoutActivityTypeHiking': 'Hike',
              'HKWorkoutActivityTypeWalking': 'Walk',
              'HKWorkoutActivityTypeSnowboarding': 'Snowboard'
              }
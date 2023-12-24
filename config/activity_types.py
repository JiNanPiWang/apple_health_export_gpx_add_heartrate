"""
Strava possible values: ride, run, swim, workout, hike, walk,
            nordicski, alpineski, backcountryski, iceskate, inlineskate,
            kitesurf, rollerski, windsurf, workout, snowboard, snowshoe
            Type detected from file overrides, uses athlete's default type if
            not specified
Apple Health Kit reference: https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype
"""


type_trans = {'HKWorkoutActivityTypeCycling': 'Ride',
              'HKWorkoutActivityTypeRunning': 'Run',
              'HKWorkoutActivityTypeSwimming': 'swim',
              'HKWorkoutActivityTypeHiking': 'swim',
              'HKWorkoutActivityTypeWalking': 'Walk',
              'HKWorkoutActivityTypeSnowboarding': 'snowboard'
              }
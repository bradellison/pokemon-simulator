
class Move:
    '''

    Class representing a pokemon move

    Public Data Members:
        -name: a string
        -power: a number
        -accuracy: a number
        -status_effects: a list of status effect dicts e.g.
            [
                {
                    "type" : "poison",
                    "chance" : 20,
                    "strength" : weak
                },
                {
                    "type": "freeze",
                    "chance" : 10,
                }
            ]


    '''
    def __init__(self, name, power, accuracy, status_effects = []):
        self.name = name
        self.power = power
        self.status_effects = status_effects
        self.accuracy = accuracy


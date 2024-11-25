from pokemonmove import Move
# from stats import PokemonStats
# import copy

class Pokemon:
    '''

    Class representing a pokemon
    
    Public Data Members:
        * name: a string
        * level: a number
        * type: a dict with keys type_1 and type_2
        * moves: a 4 length tuple of Move objects
        * current_hp: a number
        
    Public Methods:
        * change_stat: takes a state name and a change amount, returns the resultant stat
        * get_stats: calculates a pokemon's stats (taking items/effects into account) and returns the result
        * inflict_damage: reduces hp by the amount of damage and return indicates whether there is hp left
    
    ??anything else??  

    '''

    def __init__(self, name, level, pokemon_type, moves, stats):
        self.name = name
        self.level = level
        self.type = pokemon_type
        self.moves = moves
        self.current_hp = stats['max_hp']
        self.__stats_pre_adjust = stats

        self.held_items = []
        self.statuses = []

    def change_stat(self, stat_name, change_amount):
        '''
        used for permanent stat changes like resulting from Growl etc.
        pass the name of the stat to change, and a change_amount number by which to change that stat
        '''
        self.__stats_pre_adjust[stat_name] += change_amount
        return self.__stats_pre_adjust[stat_name]

    def get_stats(self):
        '''
        returns the current stats of a pokemon after applying status effects and held item effects etc.
        '''
        # TODO: implement something like below to adjust the base stats due to held items or status effects:
        # new_stats = copy.copy(self.__stats_pre_adjust)
        # for item in self.held_items:
        #     for stat_effect in item.stat_effects:
        #         new_stats[stat_effect.stat] += stat_effect.change_amount

        return self.__stats_pre_adjust

    def inflict_damage(self, damage_dealt):
        '''
        reduces hp by the given amount and returns true or false depending on whether the pokemon has any hp left
        '''
        # TODO maybe replace this with Pokemon.apply_move, which passes a Move and the attacker's
        # stats, and then calculates the resultant damage inflicted and/or any status effects
        self.current_hp -= damage_dealt
        return self.current_hp > 0


if __name__ == '__main__':
    pikachu_type = {
        'type_1' : 'electric',
        'type_2' : None
    }
    pikachu_moves = [
        Move("tackle", 30, 80, [])
    ]
    pikachu_starting_stats = {
        "max_hp" : 50,
        "atk" : 6
    }
    pikachu = Pokemon("Pikachu", 5, pikachu_type, pikachu_moves, pikachu_starting_stats)
    print("type ", pikachu.type)
    print("level: ", pikachu.level)
    print("current hp: ", pikachu.current_hp)
    pikachu.inflict_damage(20)
    print("hp after damage: ", pikachu.current_hp)
    print("stats before: ", pikachu.get_stats())
    pikachu.change_stat('atk', -1)
    print("stats after: ", pikachu.get_stats())
    

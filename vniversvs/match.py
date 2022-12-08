class Match(dict):
    """
        Tester is DEVS' tool of testing stuff in the universe
    """
    # attrs: []
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.table_combs = [
            # [1,2],
            [1,3],
            [2,3],
            [1,4],
            [2,4],
            [3,4],
            [1,5],
            [2,5],
            [3,5],
            [4,5],
        ]
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


    def make_match_deck( self ):
        pass

    def make_hand_from_deck( self ):
        pass

    def give_player_hand( self, player_name ):
        player = self.vniversvs.topos.read_object( player_name )
        player.hand.append(self.deck.pop())
        player.hand.append(self.deck.pop())

    def giveout_hands( self ):
        for player_objin in self.players.values():
            self.give_player_hand( player_objin.name )
        # hands = [self.make_hand_from_deck() for number in range(len(number_of_players))]
        # for number in range(len(number_of_players)):
        #     hands[]

    def pick_best_hand( self, player_name ):
        player_hand = self.vniversvs.topos.read_object( player_name ).hand
        current_best = self.table[:3] + player_hand
        for combination in self.table_combs:
            complement = list({1,2,3,4,5} - set(combination))
            try_hand = [self.table[i-1] for i in complement] + self.vniversvs.topos.read_object( player_name ).hand
            # print(try_hand)
            print()
        

    def compare_hands( self ):
        pass


#


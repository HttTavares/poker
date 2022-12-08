class Regula(dict):
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
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def make_hand( self ):
        ret = []
        while len(ret) < 5:
            new_card = self.vniversvs.pk.card.Card.make_random()
            if new_card not in ret:
                ret.append(new_card)
        return ret


    def run( self ):
        game = self.vniversvs.topos.create_object(
            'Game',
            object_initialization_data = {
                'name': 'test_game',
            }
        )
        # new_match = self.vniversvs.topos.create_object(
        #     'Match',
        #     object_initialization_data = {
        #         'name': 'test_match',
        #         'game': 'test_game',
        #     }
        # )
        player1 = self.vniversvs.topos.create_object(
            'Player',
            object_initialization_data = {
                'name': 'test_player1',
                'money': 1000,
            }
        )
        player2 = self.vniversvs.topos.create_object(
            'Player',
            object_initialization_data = {
                'name': 'test_player2',
                'money': 1000,
            }
        )

        new_match = game.initiate_new_match()
        game.add_player( 'test_player1' )
        game.add_player( 'test_player2' )

        new_match.deck = list(self.vniversvs.pk.Card)
        self.vniversvs.rd.shuffle(new_match.deck)
        # print(new_match.table)
        # print('-'*30)
        new_match.giveout_hands()        
        # print(new_match.table)
        # print('-'*30)
        new_match.flop = [new_match.deck.pop() for __ in range(3)]
        new_match.table = new_match.flop.copy()
        print(new_match.table)
        print('-'*30)
        new_match.turn = new_match.deck.pop()
        new_match.table.append(new_match.turn)
        print(new_match.table)
        print('-'*30)
        new_match.river = new_match.deck.pop()
        new_match.table.append(new_match.river)
        print(new_match.table)
        print('-'*30)
        # new_match.pick_best_hand( 'test_player1' )
        # print(new_match.table[0] + new_match.table[1])

        from itertools import combinations
        current_hand = None
        combs = list(combinations([0,1,2,3,4],2))
        # print(combs)
        for comb in combs:
            try:
                current_hand = self.vniversvs.pk.Hand( [new_match.table[comb[0]], new_match.table[comb[1]]] )
            except:
                pass
                # print()
        # ValueError
        # self.vniversvs.pk.Hand( [new_match.table[0], new_match.table[2]] )
        try:
            # for []
            self.vniversvs.pk.Hand( [new_match.table[0], new_match.table[2]] )
        except:
            print('not a hand')


#

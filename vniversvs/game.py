class Game(dict):
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
        self.matches = {}
        self.players = {}

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

    def generate_match_id( self ):
        # return 
        pass

    def initiate_new_match( self ):
        return self.vniversvs.topos.create_object(
            'Match',
            object_initialization_data = {
                'name': 'test_match',
                'game': self.name,
                'players': self.players
            }
        )

    def add_player( self, player_id ):
        self.players[player_id] = self.vniversvs.topos.read_object(
            player_id
        )

    def new_match( self ):
        self.matches['000000001'] = self.vniversvs.create_object(
            'Match',
            object_initialization_data = {
                'name': '000000001',
            }
        )
        print(self.matches['000000001'].keys())
        

    def run( self ):
        # pk = self.vniversvs.pk
        self.initiate_new_match()
        # hand = self.make_hand()
        # print(hand)
        

#

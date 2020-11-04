class Dress:
    '''What color is the dress?
    >>> blue = Dress('blue')
    >>> blue.look()
    'blue'
    >>> gold = Dress('gold')
    >>> gold.look()
    'gold'
    >>> blue.look()
    >>> Dress('black').look()
    'black'
    >>> gold.look()
    >>> gold.look()
    'black'
    >>> Dress('white').look()
    'white'
    >>> gold.look()
    'black'
    >>> blue.look()
    'gold'
    '''
    seen = 0
    color = None
    def __init__(self, color):
        self.color = color
        self.seen = 0

    def look(self):
        self.seen = self.seen + 1
        Dress.seen = Dress.seen + 1
        if Dress.seen % self.seen == 0:
            Dress.color = self.color
            return self.color
        else:
            self.color = Dress.color

def play_round(starter, cards):
    '''
    >>> play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    [1]
    >>> play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It's not your turn, player 3
    It's not your turn, player 0
    The round is over, player 1
    [1, 3]
    >>> play_round(3, [(3, 7), (2, 5), (0, 9)])
    It's not your turn, player 2
    [1, 3]
    '''
    r = Round(starter)
    for who, card in cards:
        try:
            r.play(who, card)
        except AssertionError as e:
            print(e)
    return Round.winners

class Round:
    players, winners = 4, []
    def __init__(self, starter):
        self.starter, self.player, self.highest = starter, starter, -1
    def play(self, who, card):
        assert  , 'The round is over, player ' + str(who)
        assert self.player == who, "It's not your turn, player " + str(who)

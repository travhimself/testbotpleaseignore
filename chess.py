import sopel.module
import random

def FEN_to_bot_string(fen):
    final_str = ''
    figures = {
        'p': u'\u265F',
        'r': u'\u265C',
        'n': u'\u265E',
        'b': u'\u265D',
        'q': u'\u265B',
        'k': u'\u265A',
        'P': u'\u2659',
        'R': u'\u2656',
        'N': u'\u2658',
        'B': u'\u2657',
        'Q': u'\u2655',
        'K': u'\u2654',
    }
    colors = (u'\u2591', u'\u2588')
    fen_sections = fen.split(' ') 
    ranks = fen_sections[0].split('/')
    for i in xrange(0,8):
        rank_string = ''
        square_count = 0
        for c in ranks[i]:
            try:
                c = int(c)
                for j in xrange(square_count, square_count + c):
                    color = ((j % 2) + (i % 2)) % 2
                    rank_string = rank_string + colors[color]
                square_count = square_count + c
            except ValueError: 
                rank_string = rank_string + figures[c]
                square_count = square_count + 1

        final_str = final_str + rank_string + '\n'
    return final_str

@sopel.module.commands('chesspuzzle')
def puzzle(bot):
    fen_list = [
        '1r3rk1/1pnnq1bR/p1pp2B1/P2P1p2/1PP1pP2/2B3P1/5PK1/2Q4R w - - 0 1',
        '1r3k2/2n1p1b1/3p2QR/p1pq1pN1/bp6/7P/2P2PP1/4RBK1 w - - 0 1',
        'r2q1k1r/ppp1bB1p/2np4/6N1/3PP1bP/8/PPP5/RNB2RK1 w - - 0 1',
    ]

    selection = random.choice(fen_list)
    bot.say(FEN_to_bot_string(selection))

@sopel.module.commands('chessmoduletest')
def test(bot):
    bot.say('module loaded')

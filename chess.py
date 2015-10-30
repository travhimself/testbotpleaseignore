import sopel.module
import random

def problem_to_bot_string(problem, bot):
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
    to_moves = {
        'w': 'White to move',
        'b': 'Black to move',
    }
    colors = (' ', u'\u2591')
    
    credit = problem[0]
    fen = problem[1]
    solution = problem[2]

    bot.say(credit)

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
                    rank_string = rank_string + colors[color] + colors[color]
                square_count = square_count + c
            except ValueError: 
                color = ((i % 2) + (square_count % 2)) % 2
                rank_string = rank_string + figures[c] + colors[color]
                square_count = square_count + 1

        bot.say(rank_string)

    bot.say(to_moves[fen_sections[1]])
    bot.memory['current_chess_puzzle'] = solution

def load_problems(f):
    problems = []
    counter = 0
    current = []
    for line in f:
        if (counter % 5) < 3:
            current.append(line.strip())
        elif (counter % 5) == 3:
            problems.append(current)
            current = []
        counter = counter + 1
    f.close() 
    return problems

@sopel.module.commands('chesspuzzle')
def puzzle(bot, trigger):
    if trigger.group(2):
        if bot.memory.contains('current_chess_puzzle'):
            solution = bot.memory['current_chess_puzzle'].split(' ')[1]
            if trigger.group == 'solution':
                bot.say(solution)
                return
            answer = trigger.nick
            if trigger.group(2) in solution:
                answer = answer + ' is the best!'
            else:
                answer = answer + ' is the worst.'
            bot.say(answer)
        else:
            bot.say('No current puzzle.')
    else:
        problem_list = load_problems(open('resources/fens.txt', 'r'))
        selection = random.choice(problem_list)
        problem_to_bot_string(selection, bot)

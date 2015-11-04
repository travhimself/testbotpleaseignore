import sopel.module
import random
from hyphenator import hyphenate_word

# Uses http://nedbatchelder.com/code/modules/hyphenate.py
@sopel.module.commands('portmanteau')
def portmanteau(bot, trigger):
    if not trigger.group(2):
        bot.say('Need some words, doggles.')
        return
    words = trigger.group(2).split(' ')
    word_count = len(words)
    pieces = {}
    for word in words:
        pieces[word] = hyphenate_word(word)

    current = ''
    keys = pieces.keys()
    keys.sort(key = lambda s: len(pieces[s]) + random.random())
    for k in keys:
        parts = pieces[k]
        if len(parts) == 1:
            current = current + parts[0]
            continue
        if current:
            i = random.choice(range(0, len(parts)))
            parts[i] = current
        elif len(parts) > 1:
            removal_i = random.choice(range(-len(parts), len(parts)))
            if removal_i >= 0:
                del parts[removal_i]

        current = ''.join(parts)

    bot.say(current)


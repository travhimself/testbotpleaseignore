import sopel.module
import random
from hyphenator import hyphenate_word

# Uses http://nedbatchelder.com/code/modules/hyphenate.py
# to break words up into parts and then shuffles and joins the pieces
# into one word. Could be modified to output more than one word.
@sopel.module.commands('portmanteau')
def portmanteau(bot, trigger):
    if not trigger.group(2):
        bot.say('Need some words, doggles.')
        return
    words = trigger.group(2).split(' ')
    pieces = []
    for word in words:
        splitwords = hyphenate_word(word)
        pieces.append(random.choice(splitwords))

    random.shuffle(pieces)
    final = ''.join(pieces)

    bot.say(final) 

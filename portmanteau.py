import sopel.module
import random


@sopel.module.commands('portmanteau')
def portmanteau(bot, trigger):
    if not trigger.group(2):
        bot.say('Need some words, doggles.')
        return
    vowel_set = set(['a','e','i','o','u', 'y'])
    words = trigger.group(2).split(' ')
    pieces = []
    for word in words:
        vowels = []
        for i in xrange(0, len(word)):
            c = word[i]
            if c in vowel_set:
                vowels.append(i)
        
        if len(vowels):
            split_index = random.choice(vowels)
        else:
            split_index = len(word)/2

        splitwords = [word[:split_index], word[split_index:],word] 
        pieces.append(random.choice(splitwords))

    random.shuffle(pieces)
    final = ''.join(pieces)

    bot.say(final) 

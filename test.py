from hyphenator import hyphenate_word
import random

def jumbler(words):

    words = words.split(' ')
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

    return current
    



import sopel.module
import random

@sopel.module.rule('Chanserv.*kicked.*')

def rekt(bot, trigger):
        rektlist = ['rektangle', 'tyranosaurus rekt', 'the good, the rekt, and the ugly', 'south by southrekt', 'brektfast']
            rektselection = random.choice(rektlist)

                notrektstring = u'\u2610 not rekt'
                    rektstring = u'\u2611' + rektselection

                        bot.say(notrektstring)
                            bot.say(rektstring)

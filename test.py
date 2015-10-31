import sopel.module

#trying to see users in a chan
@sopel.module.commands('listusers')
def list_users(bot, trigger):
    for u in bot.privileges:
        bot.say(u)

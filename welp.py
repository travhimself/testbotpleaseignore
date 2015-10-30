import sopel.module
import sopel.tools.time
import datetime


@sopel.module.rule('.*welp.*')
def record_welp(bot, trigger):
    nick = trigger.nick
    welp_count = bot.db.get_nick_value(nick, 'welp_count') or 0
    welp_count = welp_count + 1
    bot.db.set_nick_value(nick, 'welp_count', welp_count)
    bot.say(nick + ' has welped ' + str(welp_count) + 'times.')
    bot.say('TIME DEBUG: ' + sopel.tools.time.format_time(time=datetime.datetime.now()))

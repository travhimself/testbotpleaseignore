import sopel.module
import sopel.tools.time
import datetime
import random
import utils

@sopel.module.interval(60)
def welp_interval(bot):
    if bot.memory.contains('next_welpcall'):
        now = datetime.datetime.now()
        delta = now - bot.memory['next_welpcall']
        if abs(delta.total_seconds()) < 61:
            if "#testchannelpleaseignore" in bot.channels:
                # It's go time!
                _set_next_welpcall(bot)
                _run_welpcall(bot)
            
    else:
        _set_next_welpcall(bot)

def _set_next_welpcall(bot):
    hours = random.choice(range(6,12))
    minutes = random.choice(range(0, 60))
    seconds = random.choice(range(0, 60))
    delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    future = datetime.datetime.now() + delta
    bot.memory['next_welpcall'] = future

def _run_welpcall(bot):
    if bot.memory.contains('welpcall_active') and bot.memory['welpcall_active']:
        _end_welpcall(bot)
    bot.msg('#testchannelpleaseignore', 'welpcall, you nerds') 
    bot.memory['welpcall_active'] = True
    bot.memory['welpcall_list'] = []
    
def _end_welpcall(bot):
    bot.memory['welpcall_active'] = False
    users = utils.get_user_list(bot, '#testchannelpleaseignore')

    if len(bot.memory['welpcall_list']):
        winner = bot.memory['welpcall_list'][0]
        missed = set(users) - set(bot.memory['welpcall_list'])
    else:
        winner = None
        missed = users

    if '#testchannelpleaseignore' in bot.channels:
        bot.msg('#testchannelpleaseignore', 'welpcall complete.')
        bot.msg('#testchannelpleaseignore', 'Winner: ' + (winner or 'no one'))
        bot.msg('#testchannelpleaseignore', 'Failed to welp: ' + ', '.join(missed))

    if winner:
        win_count = bot.db.get_nick_value(winner, 'welpcall_wins') or 0
        bot.db.set_nick_value(winner, 'welpcall_wins', win_count + 1)
    if missed:
        for nick in missed:
            loss_count = bot.db.get_nick_value(nick, 'welpcall_misses') or 0
            bot.db.set_nick_value(nick, 'welpcall_misses', loss_count + 1)

    
@sopel.module.rule('welp')
def record_welp(bot, trigger):
    # TODO: record winner at time of welp
    if bot.memory.contains('welpcall_active') and bot.memory['welpcall_active']:
        welp_list = bot.memory['welpcall_list']
        nick = trigger.nick
        if nick not in welp_list:
            welp_list.append(nick)
        
        if welp_list == utils.get_user_list(bot, '#testchannelpleaseignore'):
            _end_welpcall(bot)

@sopel.module.commands('welpstats')
def welp_stats(bot, trigger):
    nick = trigger.group(2) or trigger.nick
    nick = nick.strip()
    wins = bot.db.get_nick_value(nick, 'welpcall_wins') or 0
    misses = bot.db.get_nick_value(nick, 'welpcall_misses') or 0
    bot.say(nick + ' has ' + str(wins) + ' welpcall wins and ' + str(misses) + ' missed welpcalls.')

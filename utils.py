def get_user_list(bot, channel, include_bot=False):
    try:
        user_dict = bot.privileges[channel]
        users = user_dict.keys()
        if not include_bot:
            users.remove(bot.nick)
    except KeyError:
        return []

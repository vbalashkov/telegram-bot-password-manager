from bot_module import bot


def init(call):
    bot.send_message(call.message.chat.id, 'Which password do you want to delete?')


def delete_password():
    pass

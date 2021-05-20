from bot_module import bot


def init(call):
    bot.send_message(call.message.chat.id, 'Запомню 2: )')


def request_password():
    pass


def request_passwords_keys():
    pass

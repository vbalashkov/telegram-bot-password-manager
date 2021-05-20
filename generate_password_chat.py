import store
from bot_module import bot

DEFAULT_PASSWORD_LENGTH = 15
VALID_CHARACTERS = ''
INVALID_CHARACTERS = ''


def init(call):
    msg = bot.reply_to(call.message, 'Type new password key:')

    bot.register_next_step_handler(msg, new_password_handler)

    # bot.send_message(call.message.chat.id, 'Type new password key:')
    #При выборе этой опции бот запрашивает название для нового пароля,
    # а затоем случайным образом создает пароль, сохраняет его и отправляет пользователю.
    # Параметры генерации (длина пароля, допустимые и запрещенные символы) можно либо запрашивать у пользователя,
    # либо оставить их константными.


def new_password_handler(message):
    password_key = message.text
    user_id = message.from_user.id

    if is_password_uniq(user_id, password_key):
        store.store_password(user_id, password_key, generate_new_password())
    else:
        bot.reply_to(message, 'Sorry, current key already exist!')
        # TODO: add possibility to override?


def is_password_uniq(user_id, password_key):
    return True


def generate_new_password(length=DEFAULT_PASSWORD_LENGTH, valid_characters=VALID_CHARACTERS, invalid_characters=INVALID_CHARACTERS):
    return '1234567890_'

import telebot
from telebot import types

import config.conf as conf
from config import messages
from config.conf import TG_TOKEN
from user import User, users
from question import add_question
from updater import save_users, save_questions

bot = telebot.TeleBot(TG_TOKEN)


def get_user(message):
    if message.from_user.id not in users:
        bot.send_message(message.from_user.id, 'Мы тебя видим впервые, напиши /start',
                         reply_markup=make_keyboard(message.from_user.id))
        return None
    return users[message.from_user.id]


def make_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if user_id not in users:
        markup.add(types.KeyboardButton('/start'))
        return markup

    user: User = users[user_id]
    if user.status == 6:
        markup.add(types.KeyboardButton('/send'))
    elif user.status in (3, 4):
        markup.add(types.KeyboardButton('/reset_question'))
        if user.status == 4:
            markup.add(types.KeyboardButton('/end_text'))
    elif user.logged and user.status == 5:
        if user.current_question_theme == '':
            markup.add(types.KeyboardButton('/homework'))
            markup.add(types.KeyboardButton('/pud'))
            markup.add(types.KeyboardButton('/controls'))
            markup.add(types.KeyboardButton('/coursework_thesis'))
            markup.add(types.KeyboardButton('/urgently'))
            markup.add(types.KeyboardButton('/other'))
        else:
            markup.add(types.KeyboardButton('/text'))
    elif user.logged:
        markup.add(types.KeyboardButton('/question'))
    else:
        if user.real_name == '':
            markup.add(types.KeyboardButton('/name'))
        if user.group == '':
            markup.add(types.KeyboardButton('/group'))
    markup.add(types.KeyboardButton('/me'))
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in users:
        users[message.from_user.id] = User(message.from_user.id, message.from_user.username)
        save_users()
        bot.send_message(message.from_user.id, messages.START, reply_markup=make_keyboard(message.from_user.id))
    else:
        bot.send_message(message.from_user.id, messages.START)
        bot.send_message(message.from_user.id, 'Вы уже зарегестрированы',
                         reply_markup=make_keyboard(message.from_user.id))


@bot.message_handler(commands=['me'])
def me(message):
    user = get_user(message)
    if not user:
        return

    bot.send_message(message.from_user.id, user.get_info(), reply_markup=make_keyboard(message.from_user.id))


@bot.message_handler(commands=['question'])
def question(message):
    user = get_user(message)
    if not user:
        return

    user.change_status(5)
    save_users()
    bot.send_message(message.from_user.id, messages.QUESTIONS_INFO, reply_markup=make_keyboard(message.from_user.id))


def send_teacher(user):
    bot.send_message(conf.TEACHER_ID,
                     messages.URGENTLY_QUESTION.format(group=user.group, name=user.real_name, username=user.username,
                                                       question=user.current_question_message))


def send_question(user):
    if user.logged and len(user.current_question_theme) and len(user.current_question_message):
        add_question(user)
        if user.current_question_theme == 'Срочно':
            send_teacher(user)
        user.reset_question()
        save_questions()
        return True
    return False


@bot.message_handler(commands=['send'])
def send(message):
    user = get_user(message)
    if not user:
        return

    if send_question(user):
        user.change_status(0)
        save_users()
        bot.send_message(message.from_user.id, messages.QUESTIONS_SENT,
                         reply_markup=make_keyboard(message.from_user.id))
    else:
        bot.send_message(message.from_user.id, 'Недостаточно данных для отправки вопроса',
                         reply_markup=make_keyboard(message.from_user.id))


@bot.message_handler(commands=['reset_question'])
def reset(message):
    user = get_user(message)
    if not user:
        return

    user.change_status(0)
    user.reset_question()
    save_users()
    bot.send_message(message.from_user.id, 'message deleted', reply_markup=make_keyboard(message.from_user.id))


@bot.message_handler(commands=['pud', 'homework', 'controls', 'coursework_thesis', 'urgently', 'other'])
def theme(message):
    user = get_user(message)
    if not user:
        return

    if message.text == '/other':
        user.change_status(3)
        bot.send_message(message.from_user.id, 'Выберите тему вашего вопроса', reply_markup=types.ReplyKeyboardRemove())
    else:
        user.current_question_theme = messages.QUESTIONS_TRANSLATOR[message.text[1:]]
        user.change_status(5)
        bot.send_message(message.from_user.id, 'добавили',
                         reply_markup=make_keyboard(message.from_user.id))
    save_users()


@bot.message_handler(commands=['name'])
def name(message):
    user = get_user(message)
    if not user:
        return

    user.change_status(1)
    save_users()
    bot.send_message(message.from_user.id, messages.ENTER_NAME, reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['group'])
def group(message):
    user = get_user(message)
    if not user:
        return

    user.change_status(2)
    save_users()
    bot.send_message(message.from_user.id, messages.ENTER_GROUP, reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['text'])
def text(message):
    user = get_user(message)
    if not user:
        return

    user.change_status(4)
    save_users()
    bot.send_message(message.from_user.id, messages.QUESTIONS_TEXT, reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['end_text'])
def end_text(message):
    user = get_user(message)
    if not user:
        return

    user.change_status(6)
    save_users()
    bot.send_message(message.from_user.id, messages.QUESTIONS_END_TEXT,
                     reply_markup=make_keyboard(message.from_user.id))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    user = get_user(message)
    if not user:
        return

    user.add_info(message.text)
    save_users()
    bot.send_message(message.from_user.id, 'ок', reply_markup=make_keyboard(message.from_user.id))

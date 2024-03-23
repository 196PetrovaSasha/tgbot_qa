import bot
from updater import check_saves, load_questions, load_users, save_questions
from question import questions
from ggle import push_questions, get_data
import config.conf as conf
import config.messages as messages

import threading
from time import monotonic


def update_table():
    data = get_data()
    for i in range(len(data)):
        try:
            if len(data[i]) > 9 and int(data[i][8]) in questions:
                question = data[i]
                questions[int(question[8])].update(question, line=i + 2)
        except:
            pass
    save_questions()
    push_questions()
    send_messages()


def send_messages():
    any_send = False
    for i in questions:
        question = questions[i]
        if question.need_answer and not question.answered:
            bot.bot.send_message(question.user_id, messages.QUESTIONS_ANSWER_TEMPLATE.format(question=question.message,
                                                                                             answer=question.answer_text))
            question.answered = True
            question.need_answer = False
            any_send = True
    save_questions()
    if any_send:
        print('messages sent')
        update_table()


latest_update = -10000


def updater():
    global latest_update
    while True:
        if monotonic() - latest_update > conf.TIME_TO_REFRESH:
            update_table()
            latest_update = monotonic()
            print('google table updated')


check_saves()
load_users()
load_questions()

upd = threading.Thread(target=updater, daemon=True)
upd.start()

bot.bot.polling(none_stop=True, interval=0)

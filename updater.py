import io
import json
import os.path

import config.conf as conf
from user import User, users
from question import Question, questions

to_unicode = str


def save_users():
    result = []
    for id_ in users:
        result.append(users[id_].json())
    with io.open(conf.USERS_SAVE_FILE, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(result,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))


def load_users():
    with open(conf.USERS_SAVE_FILE, 'r', encoding='utf-8') as data_file:
        data_loaded = json.load(data_file)

    for i in data_loaded:
        users[int(i['id'])] = User(0)
        users[int(i['id'])].load(i)


def check_saves():
    if not os.path.exists(conf.USERS_SAVE_FILE):
        with io.open(conf.USERS_SAVE_FILE, 'w', encoding='utf8') as outfile:
            str_ = json.dumps([], separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))
    if not os.path.exists(conf.QUESTIONS_SAVE_FILE):
        with io.open(conf.QUESTIONS_SAVE_FILE, 'w', encoding='utf8') as outfile:
            str_ = json.dumps([], separators=(',', ': '), ensure_ascii=False)
            outfile.write(to_unicode(str_))


def load_questions():
    with open(conf.QUESTIONS_SAVE_FILE, 'r', encoding='utf-8') as data_file:
        data_loaded = json.load(data_file)

    for i in data_loaded:
        questions[int(i[8])] = Question(User(0), 0)
        questions[int(i[8])].recover(i)


def save_questions():
    result = []
    for id_ in questions:
        result.append(questions[id_].to_table())
    with io.open(conf.QUESTIONS_SAVE_FILE, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(result,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

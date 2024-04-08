START: str = str(
    'Мы видим вас впервые, необходимо зарегестрироваться\n'
    'Отправьте информацию о себе\n'
    '/me - Что уже внесено и текущий вопрос\n'
    '/name - Внести фио\n'
    '/group - Внести группу'
)

QUESTIONS_INFO: str = (
    '/pud\n'
    '/homework\n'
    '/controls\n'
    '/coursework_thesis\n'
    '/urgently\n'
    '/other\n'
    '/text\n'
    '/end_text\n'
    '/reset_question'
)

QUESTIONS_TRANSLATOR = {
    'pud': 'ПУД',
    'homework': 'Домашняя работа',
    'controls': 'Элементы контроля',
    'coursework_thesis': 'Курсовые/Дипломные работы',
    'urgently': 'Срочно',
}

ENTER_NAME = str(
    'Введите свое ФИО'
)

ENTER_GROUP = str(
    'Введите номер своей группы или курсовая/дипломная работа, если вопрос по ним'
)

QUESTIONS_TEXT = str(
    'Напишите вопрос (вопрос можно внести несколькими сообщениями несколько сообщений)\n'
    'В конце /end_text'
)

QUESTIONS_END_TEXT = str(
    'Конец вопроса\n'
    'Отправить - /send'
)

QUESTIONS_SENT = 'Отправили'

QUESTIONS_ANSWER_TEMPLATE = str(
    'Введите свой вопрос:\n'
    '{question}\n'
    'Ответ:\n'
    '{answer}'
)

URGENTLY_QUESTION = str(
    'Вам поступил срочный вопрос:\n'
    '{question}\n'
    'группа:{group}\n'
    'Имя: {name}\n'
    'user:{username}\n'
)



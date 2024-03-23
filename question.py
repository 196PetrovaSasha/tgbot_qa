questions = {}
max_question = 1


def add_question(user) -> int:
    id_ = get_new_question_id()
    questions[id_] = Question(user, id_)
    return id_


def get_new_question_id():
    global max_question
    max_question += 1
    return max_question


class Question:
    def __init__(self, user, id_):
        self.id = id_
        self.line = id_
        self.user_id = user.id
        self.name = user.real_name
        self.username = user.username
        self.group = user.group
        self.theme = user.current_question_theme
        self.message = user.current_question_message
        self.need_answer = False
        self.answered = False
        self.answer_text = ''

    def to_table(self) -> list:
        return [self.group, self.theme, self.message, self.name, self.username, self.answer_text, self.need_answer,
                self.answered, self.id, self.user_id]

    def update(self, data, line = None):
        if len(data) > 5:
            self.answer_text = data[5]
        if len(data) > 6 and data[6] == 'TRUE':
            self.need_answer = True
        if line:
            self.line = line

    def recover(self, data):
        self.group = data[0]
        self.theme = data[1]
        self.message = data[2]
        self.name = data[3]
        self.username = data[4]
        self.answer_text = data[5]
        self.need_answer = data[6]
        self.answered = data[7]
        self.id = int(data[8])
        self.user_id = int(data[9])
        self.line = self.id

        global max_question
        max_question = max(max_question, self.id)

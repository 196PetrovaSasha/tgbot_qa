users = {}


class User:
    def __init__(self, id_: int, username=None):
        self.id = id_
        if not username:
            username = id_
        self.username = username
        self.logged = False

        self.status = 0
        self.group = ''  # 1
        self.real_name = ''  # 2
        self.current_question_theme = ''  # 3
        self.current_question_message = ''  # 4
        # 5 question in progress

        self.check()

    def reset_question(self):
        self.current_question_theme = ''
        self.current_question_message = ''

    def change_theme(self, theme):
        self.current_question_theme = theme

    def change_status(self, status):
        self.status = status

    def check(self):
        if len(self.real_name) and len(self.group) and len(self.username):
            self.logged = True
        else:
            self.logged = False

    def get_info(self):
        return str(f'Текущая информация:\n'
                   f'ФИО: {self.real_name}\n'
                   f'username: {self.username}\n'
                   f'группа: {self.group}\n'
                   f'заполнены необходимые данные: {self.logged}\n'
                   f'Тема текущего вопроса: {self.current_question_theme}\n'
                   f'Текст текущего вопроса: {self.current_question_message}\n')

    def add_info(self, message):
        if self.status == 1:
            self.real_name = message
            self.status = 0
        elif self.status == 2:
            self.group = message
            self.status = 0
        elif self.status == 3:
            self.current_question_theme = message
            self.status = 5
        elif self.status == 4:
            self.current_question_message += message + '\n'
        self.check()

    def json(self):
        res = {
            'id': str(self.id),
            'username': str(self.username),
            'logged': self.logged,
            'status': self.status,
            'group': str(self.group),
            'real_name': str(self.real_name),
            'theme': str(self.current_question_theme),
            'message': str(self.current_question_message),
        }
        return res

    def load(self, data):
        self.id = int(data['id'])
        self.username = data['username']
        self.logged = data['logged']
        self.status = int(data['status'])
        self.group = data['group']
        self.real_name = data['real_name']
        self.current_question_theme = data['theme']
        self.current_question_message = data['message']

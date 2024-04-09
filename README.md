## категории вопросов:
- домашняя работа - homework 
- пуд - pud 
- элементы контроля - controls 
- курсовые/дипломные работы - coursework_thesis 
- срочно - urgently 
- кастомный - other

## Настройка PyCharm 
**В терминале необходимо выполнить следующте команды**

- pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
- pip install oauth2client # возможно не надо
- pip install pyTelegramBotAPI

## Создание собственного бота

- Создать собственный бот через Bot_father
- bot_father -> получить токен для бота тг, вставить в конфиг TG_TOKEN


## Создание и настройка таблицы
**Необходимо**
- Создать таблицу
- Добавить в редакторы bothandler1@bot-handler-students1questions.iam.gserviceaccount.com
- Взять ссылку https://docs.google.com/spreadsheets/d/<ID электронной таблицы (spreadsheet ID)>/edit#gid=<ID листа (sheet ID) >
- В конфиге сделать TABLE_ID = id таблицы
- В конфиге сделать SHEET_ID = название листа

- Настроить поля в таблице 
  - А1 группа

  - B1 тема

  - C1 вопрос

  - D1 фио

  - E1 тг

  - F1 Ответ

  - G1 Ответить?

  - H1 Отправлено

  - технические

  - I - id вопроса

  - J- id пользователя

  - для g2, h2 добавить чекбоксы и растянуть на все строки

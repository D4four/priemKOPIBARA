import telebot
import pymorphy2
from difflib import SequenceMatcher
import inspect

morph = pymorphy2.MorphAnalyzer()

def normalize_text(text):
    words = text.split()
    normalized_words = [morph.parse(word)[0].normal_form for word in words]
    return ' '.join(normalized_words)

def similarity_score(text1, text2):
    normalized_text1 = normalize_text(text1)
    normalized_text2 = normalize_text(text2)
    matcher = SequenceMatcher(None, normalized_text1, normalized_text2)
    return matcher.ratio()

bot = telebot.TeleBot('6744225497:AAFV7H7f2l2bzDG5QQCkmkgOnhqKDMH6iEQ')

@bot.message_handler(commands=['start'])
def start(message):

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Перейти на сайт')
    btn2 = telebot.types.KeyboardButton('Информация об институтах')
    markup.row(btn1, btn2)
    btn3 = telebot.types.KeyboardButton('Задать свой вопрос')
    markup.row(btn3)

    file = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, caption=f'Привет, {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup, parse_mode='Markdown')

@bot.message_handler()
def anyText(message):

    if message.text.lower() == 'перейти на сайт':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Открыть сайт", url="https://priem.guap.ru/"))

        bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы открыть сайт:", reply_markup=markup)
    elif message.text.lower() == 'информация об институтах':
        markup = telebot.types.InlineKeyboardMarkup()
        btn1 = telebot.types.InlineKeyboardButton(text='Институт 1', callback_data='first')
        btn3 = telebot.types.InlineKeyboardButton(text='Институт 3', callback_data='third')
        markup.row(btn1, btn3)
        btn2 = telebot.types.InlineKeyboardButton(text='Институт 2', callback_data='second')
        btn4 = telebot.types.InlineKeyboardButton(text='Институт 4', callback_data='fourth')
        markup.row(btn2, btn4)

        bot.send_message(message.chat.id, "Выберите интересующий иститут:\n    -Институт аэрокосмических приборов и систем (институт 1)\n    -Институт радиотехники и инфокоммуникационных технологий (институт 2)\n    -Институт киберфизических систем (институт 3)\n    -Институт радиотехники и инфокоммуникационных технологий (институт 4)", reply_markup=markup)

    elif message.text.lower() == 'задать свой вопрос':
        bot.register_next_step_handler(message, process)

def process(message):
    bot.send_message(message.chat.id, "Выберите интересующий истит")
    qa_pairs = {
        "Что такое вступительные испытания?": "ЕГЭ",
        "Как поступить": "Подать заявление",
        "Какие индивидуальные достижения есть?": "Да",
        "Как подать документы": "ЛК, ЕПГУ, очно",
        "Есть ли военная кафедра": "Да",
        "Как перевестись?": "Деканат",
        "Стоимость обучения": "Пока нет.."
        # Добавьте другие вопросы и ответы
    }

    user_input = message.text

    # Calculate similarity scores for all questions
    similarity_scores = {question: similarity_score(user_input, question) for question in qa_pairs.keys()}

    # Sort questions based on similarity scores in descending order
    sorted_questions = sorted(qa_pairs.keys(), key=lambda question: similarity_scores[question], reverse=True)

    # Output the top three most similar questions and their scores
    markup = telebot.types.InlineKeyboardMarkup()
    for i in range(min(3, len(sorted_questions))):
        current_question = sorted_questions[i]

        btn = telebot.types.InlineKeyboardButton(text=f"{current_question}:", callback_data='')
        markup.row(btn)
        # print(f"Возможно, вам будет интересен вопрос '{current_question}':")
        # print(f"Ответ: {qa_pairs[current_question]}, Сходство: {str(similarity_scores[current_question])}")
        # print()
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'first':
        bot.send_message(callback.message.chat.id, "Институт аэрокосмических приборов и систем — признанный в России и за рубежом центр подготовки дипломированных специалистов, бакалавров и магистров в области современного приборостроения, систем управления движением и навигацией, передовых информационных аэрокосмических систем, технологии транспортных процессов и системного анализа. Известные научные школы и научные исследования в области приборостроения, аэродинамики и динамики полета летательных аппаратов, обеспечения безопасности подвижных объектов, спутникового мониторинга, систем обработки, информации, технической диагностики, создания малоразмерных летательных аппаратов и обеспечения их безопасной навигации являются основой партнерских отношений с коллегами из различных стран мира. Современная учебно-методическая и лабораторная база института позволяет использовать в учебном процессе передовые технологии обучения, позволяет студентам проводить прикладные исследования и вести проекты, позволяющие участвовать в профессиональных выставках и конкурсах.\n\nТел: (812) 571-16-89\n\nПочта: aerospace1@guap.ru")
    elif callback.data == 'second':
        bot.send_message(callback.message.chat.id, "Очень многие окружающие нас в повседневной жизни предметы являются радиоэлектронными устройствами. Сложнейшей радиоэлектронной аппаратурой оборудованы заводы и банки, научные лаборатории и транспорт, космические аппараты и морские суда. Нельзя представить себе современный мир без спутниковых систем навигации, телевидения и связи, без компьютеров и информационных сетей, без высококачественной аудио- и видеоаппаратуры. Во всем этом многообразии хорошо разбираются выпускники института радиотехники, электроники и связи. Они могут осуществить проектирование, изготовление, ремонт и обслуживание всей этой техники, без которой сегодня немыслима жизнь. Универсальная профессия – это стабильное благополучие на всю жизнь. Именно такие профессии дает институт радиотехники, электроники и связи. Наши выпускники нужны и сегодня, и в обозримой перспективе будут нужны везде и всегда.\n\nТел: (812) 571-16-89\n\nПочта: fresguap@mail.ru")
    elif callback.data == 'third':
        bot.send_message(callback.message.chat.id, "Институт осуществляет обучение в области интеллектуальных систем управления техническими объектами, инновационных технологий в общепромышленной и специальной энергетике, термоядерной физики, электромеханических и робототехнических систем, энерго- и ресурсосбережения. Благодаря многопрофильной вузовской подготовке выпускники нашего института могут реализовать свои знания и творческий потенциал как в ядерно-энергетической отрасти, так и в других высокотехнологичных отраслях электротехнического и электрофизического профиля. Мы развиваем связи с реальным сектором экономики, академической и отраслевой наукой. Выпускники института с успехом работают на ведущих предприятиях Санкт-Петербурга и России.\n\nТел: +7-812-494-70-30  \n\nПочта: dept3@aanet.ru")
    elif callback.data == 'fourth':
        bot.send_message(callback.message.chat.id, "Институт является ведущим в университете в области компьютерных наук и их приложений. Выпускники института – это специалисты, бакалавры и магистры в области вычислительных машин, комплексов, систем и сетей, программного обеспечения вычислительной техники и автоматизированных систем, математического обеспечения и администрирования информационных систем, математического моделирования, информатики и вычислительной техники, электронных устройств и систем. Сегодня обучение в институте сочетает все аспекты подготовки в области IT – от микропроцессорных систем до виртуальной и дополненной реальности.\n\nТел: +7-812-494-70-40\n\nПочта: dek4@guap.ru")

bot.infinity_polling()
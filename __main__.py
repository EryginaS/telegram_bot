# -*- coding: utf-8 -*-

import telegram
from uuid import uuid4
from telegram.ext import CallbackContext
from telegram.ext import Updater, CommandHandler
import random
from telegram.ext import run_async
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import time
from . import config

links = []
list = []

with open(config['list'], 'r') as f:
    list = f.readlines()

with open(config['links'], 'r') as f:
    links = f.readlines()


updater = Updater(token=config['token'],
                  use_context=True)
bot = telegram.Bot(token=config['token'])
dispatcher = updater.dispatcher


# Функция старта
@run_async
def start(update: Updater, context: CallbackContext):
    custom_keyboard = [['/go'], ['/end']]

    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,
                                                one_time_keyboard=False)

    bot.send_message(chat_id=update.message.chat_id,
                     text='Приветствую Вас\n'
                          '\nПРЕДУПРЕДЖЕНИЕ!!!!\n'
                          '\nДля Работы Вам ежедневно НЕОБХОДИМО уделять от 2.5 часов времени.\n'
                          '\nЭто необходимо, чтобы качественно выполнять всю работу по ведению каналов,'
                          ' чтобы Вы и каждый участник чата смог зарабатывать деньги.\n'
                          '\nЕсли Вы Согласны с этим условием, то нажмите /go на вашей клавиатуре и мы продолжим.\n'
                          '\nЕсли Вы против, то тогда покиньте чат, нажав /end на вашей клавиатуре.',
                     reply_markup=reply_markup)


@run_async
def step_two(update: Updater, context: CallbackContext):
    custom_keyboard = [['/start'], ['/shag_3']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,
                                                one_time_keyboard=True)
    bot.send_message(chat_id=update.message.chat_id,
                     text='Деньги за свою работу Вы будете получать на электронные кошельки.\n'
                          '\nПерейдите по ссылки, чтобы создать электронный кошелёк, который подойдет именно Вам.\n'
                          '\n"https://telegra.ph/Verifikaciya-koshelka-YAndeks-Dengi-PayPal-08-21"\n'
                          '\nПосле выполнения данного шага нажмите  /shag_3\n'
                          '\nВнимательно следуйте иструкции.', reply_markup=reply_markup)
    bot.send_message(chat_id=update.message.chat_id, )


@run_async
def last_step(update: Updater, context: CallbackContext):
    code = ['hTrs56J', 'Hg8dEta', 'Hgcvxd6', 'lkdsII9', 'kcrh09L',
            'kdsaj7R', 'PopH65K', 'Saer76B', 'MNxcsd2', 'asdF65B']
    number_of_code = random.randint(0, 9)

    bot.send_message(chat_id=update.message.chat_id, text='Ваш код доступа в группу:\n'
                                                          + code[number_of_code] + ''
                                                                                   '\nНапишите одному из топов, '
                                                                                   'чтобы они добавили вас в группу:'
                                                                                   '\n@Scar01 🌪\n'
                                                                                   '@MoonSeoyeong 🌸\n'
                                                                                   '@LudmiZav1208 🐍\n'
                                                                                   '@FilippM 👔\n'
                                                                                   '@gavri_love 💼\n'
                                                                                   '@SborBaz 👨‍🔧\n'
                                                                                   '@southno 🌝\n'
                                                                                   '@IrinaBochkarewa 🦐')


def go(update: Updater, context: CallbackContext):
    custom_keyboard = [['/start'], ['/shag_2']]

    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,
                                                one_time_keyboard=False)
    bot.send_message(chat_id=update.message.chat_id,
                     text="Приветствую Вас\n"
                          "\nМеня зовут Генезиз\n"
                          "\nЯ бот - помощник. Путь к Деньгам Вы начнете с меня.\n"
                          "\nПо ссылке telegra.ph/dzen-07-30-2 , ознакомьтесь, пожалуйста,"
                          " с первым шагом.\n"
                          "\nЕсли Вас всё устроит и Вы выполните этот шаг, нажмите "
                          "кнопку /shag_2 , которая находится "
                          "у вас на клавиатуре, и мы продолжим.\n"
                          "\nСпасибо", reply_markup=reply_markup)


def end(update: Updater, context: CallbackContext):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Прощай! \n'
                          '\nЕсли передумаешь, возвращайся и пиши мне /start')


def step_three(update: Updater, context: CallbackContext):
    custom_keyboard = [['/start'], ['/shag_3'], ['/shag_4']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,
                                                one_time_keyboard=True)
    bot.send_message(chat_id=update.message.from_user.id,
                     text='На данном этапе внесём Ваши каналы в нашу '
                          'базу.\n'
                          '\nЭто нужно, чтобы на Ваши каналы начала'
                          ' подписываться'
                          ' аудитория, которая будет читать Ваши статьи.\n'
                          '\nСейчас Вам нужно внести Ваши данные в базу '
                          '\nhttps://docs.google.com/forms/d/1mhmrVmOehGILptTxgmCoLGmr8AL2h4MG7l9AHZIwbKs/edit\n'
                          '\n'
                          'Где найти ссылку на свой профиль:'
                          ' https://telegra.ph/Kak-skopirovat-ssylku-na-svoj-kanal-08-24-2\n'
                          '\nГде найти свой ник в телеграм: '
                          'https://telegra.ph/Gde-nahoditsya-ssylka-na-moj-profil-08-18\n'
                          '\nПосле заполнения, если у вас есть еще один канал, то нажмите на /shag_3 на клавиатуре, '
                          'если же каналов больше нет, то нажмите /shag_4 ',
                     reply_markup=reply_markup)


def step_four(update: Updater, context: CallbackContext):
    custom_keyboard = [['/start'], ['/shag_5']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard,
                                                one_time_keyboard=True)
    bot.send_message(chat_id=update.message.from_user.id,
                     text='На данном этапе вам нужно подписаться на всех участников. Но в ручную вам не прийдется это '
                          'делать так как у нас существует программа автоподписок, для ее скачивания нужно перейти по '
                          'ссылке:\n '
                          '\n'
                          '\nи скачать программу для автоподписок.'
                          '\nhttps://drive.google.com/file/d/1S3plvutcI8zvrRjDEtUR-uRfl-LA-bXs/view?usp=sharing\n'
                          '\nСсылка на инструкцию по использованию программы: https://youtu.be/zm5HRHIDEQQ\n '
                          '\nВсе существующие каналы можно получить по ссылке:'
                          '\nhttps://docs.google.com/spreadsheets/d/1omqlCribj-Qgb3Pd89gsaovnXHUCKY-fiRUiLJBTf0Y/'
                          'edit#gid=289759398\n'
                          '\nПо окончанию работы программы автоподписок нажмите на /shag_5 на вашей клавиатуре. ',
                     reply_markup=reply_markup)


def inlinequery(update, context):
    query = update.inline_query.query
    number = []
    a = [number.append(i) for i in range(len(list)) if query in list[i]]
    results = []

    if len(number) != 0:

        for i in range(len(number)):
            results.append(InlineQueryResultArticle(
                id=uuid4(),
                title=list[number[i]],
                thumb_width=30,
                thumb_height=12,
                input_message_content=InputTextMessageContent(
                    links[number[i]])))
    else:
        for i in range(5):
            results.append(InlineQueryResultArticle(
                id=uuid4(),
                title=list[i + 68],
                thumb_width=30,
                thumb_height=12,
                input_message_content=InputTextMessageContent(
                    links[i + 68])))

    update.inline_query.answer(results)


def main(dispatcher, updater):
    # старт

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('shag_2', step_two))
    dispatcher.add_handler(CommandHandler('shag_5', last_step))
    dispatcher.add_handler(CommandHandler('go', go))
    dispatcher.add_handler(CommandHandler('end', end))
    dispatcher.add_handler(CommandHandler('shag_3', step_three))
    dispatcher.add_handler(CommandHandler('shag_4', step_four))
    dispatcher.add_handler(InlineQueryHandler(inlinequery))


if __name__ == '__main__':
    print('start')
    main(dispatcher, updater)
    updater.start_polling()
    updater.idle()

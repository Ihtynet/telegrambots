# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
bot = telebot.TeleBot(config.token)


def proc_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('+')
    btn2 = types.KeyboardButton('-')
    btn3 = types.KeyboardButton('*')
    btn4 = types.KeyboardButton('/')
    markup.add(btn1, btn2, btn3, btn4)
    return markup


@bot.message_handler(commands=['calculator'])
def calculator(message):
    msg = bot.send_message(message.chat.id, "Можем позаниматься математикой!\nВведи число:")
    bot.register_next_step_handler(msg, process_num1_step)


def process_num1_step(message):
    if message.text.isdigit():
        msg = bot.send_message(message.chat.id, "Что делаем?", reply_markup=proc_kb())
        bot.register_next_step_handler(msg, process_proc_step, message.text)
    else:
        msg = bot.send_message(message.chat.id, 'это не число, повтори ввод')
        bot.register_next_step_handler(msg, process_num1_step)


def process_proc_step(message, num_1):
    print('process_proc_step')
    print('num_1:', num_1)
    print('proc:', message.text)
    if message.text in ['+', '-', '*', '/']:
        msg = bot.send_message(message.chat.id, "Введите еще число:")
        bot.register_next_step_handler(msg, process_num2_step, num_1, message.text)
    elif message.text.isdigit():
        msg = bot.send_message(message.chat.id, 'сейчас число не требуется, повтори ввод', reply_markup=proc_kb())
        bot.register_next_step_handler(msg, process_proc_step, num_1)
    else:
        msg = bot.send_message(message.chat.id, 'странная операция, повтори ввод', reply_markup=proc_kb())
        bot.register_next_step_handler(msg, process_proc_step, num_1)


def process_num2_step(message, num_1, proc):
    print('process_num2_step')
    print('num_1:', num_1)
    print('proc:', proc)
    print('num_2:', message.text)
    if message.text.isdigit():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        result = types.KeyboardButton('Что вышло?')
        add = types.KeyboardButton('Ещё кое что...')
        markup.add(result, add)
        msg = bot.send_message(message.chat.id, "Показать результат или продолжить операцию?", reply_markup=markup)
        bot.register_next_step_handler(msg, process_alternative_step, num_1, proc, message.text)
    else:
        msg = bot.send_message(message.chat.id, 'это не число, повтори ввод')
        bot.register_next_step_handler(msg, process_num2_step)


def process_alternative_step(message, num_1, proc, num_2):
    print('process_alternative_step')
    print('num_1:', num_1)
    print('proc:', proc)
    print('num_2:', num_2)
    if message.text == 'Что вышло?':
        bot.send_message(message.chat.id, f'{num_1} {proc} {num_2} = {eval(str(num_1) + proc + str(num_2))}')
bot.polling(none_stop=True)

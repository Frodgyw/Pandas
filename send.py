from pyrogram import Client
from pyrogram.errors import FloodWait, BadRequest, Flood, InternalServerError
from time import sleep
from sys import stderr, exit
from loguru import logger
from dotenv import dotenv_values
from msvcrt import getch
from os import system
import time


def clear(): return system('cls')


config = dotenv_values()
SESSION_NAME = config['session_name']
API_ID = int(config['7881555661:AAHe1SrlZX74PPVRnyJBOopzhdOLpBJGpo0'])
API_HASH = config['api_hash']
x = 1
logger.remove()
logger.add(stderr,
           format='<white>{time:HH:mm:ss}</white> | '
                  '<level>{level: <8}</level> | '
                  '<cyan>{line}</cyan> - '
                  '<white>{message}</white>')

app = Client(SESSION_NAME, API_ID, API_HASH)

with open('otc.txt', 'r', encoding='utf-8') as file:
    otc_list = [row.strip() for row in file]

msg_text = open('msg_text.txt', 'r', encoding='utf-8').read()

successful_messages = {}


def send_message_otc(current_otc):
    global successful_messages
    for _ in range(3):
        try:
            app.send_message(current_otc, msg_text)

        except FloodWait as error:
            sleep(1)

        except Flood:
            pass

        except BadRequest as error:
            logger.error(f'{current_otc} | {error}')

        except InternalServerError as error:
            logger.error(f'{current_otc} | {error}')

        except Exception as error:
            logger.error(f'{current_otc} | {error}')

        else:
            if current_otc in successful_messages:
                successful_messages[current_otc] += 1
            else:
                successful_messages[current_otc] = 1

            logger.success(f'{current_otc} | The message was successfully sent')
            return

    with open('errors_send_message.txt', 'a', encoding='utf-8') as file:
        file.write(f'{current_otc}\n')


def join_chat_otc(current_otc):
    for _ in range(3):
        try:
            app.join_chat(current_otc)

        except FloodWait as error:
            sleep(1)

        except Flood:
            pass

        except BadRequest as error:
            logger.error(f'{current_otc} | {error}')

        except InternalServerError as error:
            logger.error(f'{current_otc} | {error}')

        except Exception as error:
            logger.error(f'{current_otc} | {error}')

        else:
            logger.success(f'{current_otc} | Successfully logged into the chat')
            return

    with open('errors_join_chat.txt', 'a', encoding='utf-8') as file:
        file.write(f'{current_otc}\n')


def write_successful_messages():
    with open('successful_messages.txt', 'w', encoding='utf-8') as file:
        for chat, count in successful_messages.items():
            file.write(f'{chat}: {count}\n')


if __name__ == '__main__':
    user_action = int(input('Enter your action '
                            '(1 - join chats from .txt; '
                            '2 - send message in chats from .txt): '))

    interval = int(input('Enter the interval between repeated executions (in seconds): '))

    clear()

    while True:
        with app:
            for current_otc in otc_list:
                if user_action == 1:
                    join_chat_otc(current_otc)

                elif user_action == 2:
                    send_message_otc(current_otc)

        logger.success('Работа успешно завершена!')
        logger.success(f'Количество успешно отправленных сообщений: {sum(successful_messages.values())}')

        write_successful_messages()

        print(f'\nWaiting for {interval} seconds before the next execution...')
        time.sleep(interval)
        clear()

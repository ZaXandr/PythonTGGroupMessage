import time
import os

from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import JoinChannelRequest

with open('setup.txt', 'r') as f:
    data = f.read().splitlines()
f.close()
client = TelegramClient('session.session', int(data[0]), data[1])
client.connect()

with open("chats_via_username.txt") as file:
    array = [row.strip() for row in file]
    file.close()
with open("Message.txt", 'r', encoding='utf-8') as f:
    message = f.read()
    f.close()

users = os.listdir('accounts')

try:
    for i in range(len(array)):
        try:
            with open('accounts/'+users[i % 2]+'/setup.txt', 'r') as f:
                data = f.read().splitlines()
            f.close()
            client = TelegramClient('accounts/'+users[i % 2]+'/session.session', int(data[0]), data[1])
            client.connect()

            destination_channel_entity = array[i]
            entity = client.get_entity(destination_channel_entity)

            client.send_message(entity=entity, message=message)

            # with open("result.txt", 'w') as result:
            #     result.write('Message send to: ' + array[i] + '\n')
            client.disconnect()
            time.sleep(15)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)





import time

from telethon import TelegramClient, sync, events

with open('setup.txt', 'r') as f:
    data = f.read().splitlines()
f.close()
client = TelegramClient('session', int(data[0]), data[1])

# Data array with api_id - data[0] , api_hash - data [1], phone_number - data [2]

client.connect()

if not client.is_user_authorized():
    client.send_code_request(data[2])

    client.sign_in(data[2], input('Enter the code: '))

try:
    with open("chats_via_username.txt") as file:
        array = [row.strip() for row in file]
        message = input("Input message: ")
    for i in range(len(array)):
        try:
            destination_channel_entity = array[i]
            entity = client.get_entity(destination_channel_entity)
            client.send_message(entity=entity, message=message)
            time.sleep(15)
        except Exception as e:
            print(e)

except Exception as e:
    print(e)
client.disconnect()

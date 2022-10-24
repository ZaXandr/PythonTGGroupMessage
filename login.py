import os

from telethon import TelegramClient, sync, events

# Create folder for new account
name: str = input('Input account name: ')
os.mkdir('accounts\\'+name)

# Create your API Tools
with open('accounts\\' + name + '\\setup.txt', 'w') as f:
    f.write(input('api_id: ')+'\n')
    f.write(input('api_hash: ')+'\n')
    f.write(input('phone_number: ')+'\n')
    f.close()

with open('accounts\\' + name + '\\setup.txt', 'r') as f:
    data = f.read().splitlines()    # Array with api_id, api_hash, phone_number
f.close()

client = TelegramClient('accounts\\' + name + '\\session', int(data[0]), data[1])
client.connect()
client.send_code_request(data[2])
client.sign_in(data[2], input('Enter the code: '))

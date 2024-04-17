import requests
Token = "5919164836:AAHxvkcXeHF41lpDjC_Wys7iVsiJ7BH8DX0"
chat_id = "1087968824"
message_id = "168"
emoji = "❤️‍🔥"

url = f"https://api.telegram.org/bot{Token}/setMessageReaction"
data = {
    "chat_id": chat_id,
    "message_id": message_id,
    "reaction": [ 
        {
            'type': 'emoji',
            'emoji': emoji
        }
    ],
    'is_big': False
}

response = requests.post(url, json=data)

print(response.json())

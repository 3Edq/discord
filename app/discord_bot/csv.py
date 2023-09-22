import csv
from datetime import datetime

def log_conversation(user_id, user_query, bot_response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('conversations.csv', 'a', newline='') as csvfile:
        fieldnames = ['user_id', 'user_query', 'bot_response', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({
            'user_id': user_id,
            'user_query': user_query,
            'bot_response': bot_response,
            'timestamp': timestamp
        })
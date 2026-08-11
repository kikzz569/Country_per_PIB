from datetime import datetime

def logs(message):
    timestamp_format = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open('data/logs.csv', 'a') as file:
        file.write(timestamp +','+ message + '\n')
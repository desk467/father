from datetime import datetime

def log(data):
    print("[LOG][{time}] - {data}".format(time=datetime.now().strftime('%d/%m/%y %H:%M:%S'), data=data))
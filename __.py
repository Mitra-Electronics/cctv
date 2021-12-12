from datetime import datetime, timedelta

time = "12-12-2021 20:03"

parsed_time = datetime.strptime(time, "%d-%m-%Y %H:%M")

while True:
    if parsed_time - datetime.strptime(datetime.now().strftime("%d-%m-%Y %H:%M"), "%d-%m-%Y %H:%M") > timedelta(0,0,0,0,0,0,0):
        pass
    else:
        print("Notification")
        # Enter notification code here
        break
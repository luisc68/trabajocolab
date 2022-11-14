# hacer que un programa aplique un codigo a las 8 am

import time
import schedule

def job():
    print("I'm working...")

# Path: time.py
# hacer que un programa aplique un codigo a las 8 am

schedule.every().day.at("8:00").do(job) #hacer que un programa aplique un codigo a las 8 am
while True:
    
    schedule.run_pending()
    time.sleep(1)
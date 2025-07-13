'''
1-twilio client setup
2-user inputs
3-scheduling logic
4-send message

'''
#step 1-install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

#step 2-twilio credentials
account_sid='XXXX'
auth_token='XXXX'

client=Client(account_sid,auth_token)

#step 3-design send message function
def send_whatsapp_message(recipient_number,message_body):
    try:
        message=client.messages.create(
            from_='whatsapp:XXXX',
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID{message.sid}")

    except Exception as e:
        print("An error occurred")    

#step 4 user name
name=input("Enter the user name= ")  
recipient_number=input("Enter the recipients whatsapp number with country code: ")
message_body=input(f"Enter the message you want to send to {name}")

#step 5-parse datetime and claculate delay
date_str=input("enter the date to send the message (YYYY-MM-DD): ")
time_str=input("enter the time to send the message (HH:MM in 24 hour format)")

#datetime
schedule_datetime=datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime=datetime.now()

#calculate delay
time_difference=schedule_datetime-current_datetime
delay_seconds=time_difference.total_seconds()

if delay_seconds<=0:
    print("The specified time is in the past. Please enter a future date and time: ")

else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}")   

    #wait until the scheduled time
    time.sleep(delay_seconds) 

    send_whatsapp_message(recipient_number,message_body)

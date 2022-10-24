from datetime import datetime
import time
import os
import smtplib, ssl

import requests as requests
from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup


def send_mail():
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "mic.manos@gmail.com"
    receiver_email = "mic.manos@gmail.com"
    password = ("txpxsuyqcpgrsukx")
    message = "VGHGAN AEKKKKKKAARRRRRAAAAA"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def aek_request():
    # Making a GET request
    r = requests.get('https://www.ticketmaster.gr/aek/showProductList.html')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('span', {"class": "message"})
    txt="Δεν υπάρχουν διαθέσιμοι αγώνες!"
    if s is None:
        send_mail()
    if txt in s:
        print("den vghkann")

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(aek_request, 'interval', hours=1 / 45)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()

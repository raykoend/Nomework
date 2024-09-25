def send_email(massage, recipient, sender = "university.help@gmail.com"):
    if ('@' and ('.com' or '.ru' or '.net')) not in (recipient or sender):
        print("Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! с адреса {sender} на адрес {recipient}.")

send_email('message','raykoend@gmail.com')
send_email('message','rayko.r')
send_email('message','rayko.com')
send_email('message','university.help@gmail.com','@.com')
send_email('message','university.help@gmail.com')

# your Gmail account
import smtplib

def send_mail(subject,message,to):

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()


    gmail_id = 'muhammedmubarak204@gmail.com.com'
    gmail_password = '234556677'
    # gmail_id = 'kitesarun@gmail.com'
    # gmail_password = 'kites4321'

    s.login(gmail_id, gmail_password)

    # message to be sent
    message = 'Subject: {}\n\n{}'.format(subject, message)

    # sending the mail
    s.sendmail(gmail_id, to, message)

    print(to, message)

    # terminating the session
    s.quit()

#send_mail("heoo","hai",'nx.sarath@gmail.com')

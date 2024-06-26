# The Automated Email Sender project involves creating a Python script that can send emails automatically based on
# user input or on a schedule. This project will help you learn about email protocols (SMTP), how to format emails,
# and how to schedule tasks in Python.


import re
import smtplib  # for connecting to the SMTP server and sending the email.
from email.mime.multipart import MIMEMultipart  # for creating email template message.
from email.mime.text import MIMEText

# function to take user's input-:

'''here we are also going to validate the entered gmail id-: use regex(regular  expression) and to work with
    these expressions we are going to use the re module.
    here 'r' is used to tell the python that it is raw expression.
    r'^[a-zA-Z0-9._+-]+@gmail/.com$'-:Putting it all together, the regular expression r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    matches:
Start of the string (^)
Followed by one or more characters from the set [a-zA-Z0-9._%+-]:
Lowercase letters (a-z)
Uppercase letters (A-Z)
Digits (0-9)
Period (.)
Underscore (_)
Percent sign (%)
Plus sign (+)
Hyphen (-)
Followed by the literal @gmail string

Followed by a literal period(\.)-: When you want to match these special characters literally (i.e., as they appear), 
you need to "escape" them by prefixing them with a backslash \. Without Escaping (.): Matches any single character except
 a newline.


Followed by the literal com string
End of the string ($)
This pattern ensures that the input string is a valid Gmail address in the format: some valid characters followed by 
@gmail.com.
    '''


def users_details():
    email_regexp = r'^[a-zA-Z0-9._+-]+@gmail\.com$'
    while True:
        recipient_email = input("enter the Recipient Email-Id-:")
        if re.match(email_regexp, recipient_email):
            break
        else:
            print("please enter valid Email-ID")
            continue
    subject = input("Subject-:")
    body = input("message body-:")
    return recipient_email, subject, body


# function to create email template using email module.
# You need to create an email message object, set the headers, and attach the email body.
# MIMEMultipart is used to create a container for the email message that can hold multiple parts.
# MIMEText is used to create a text part (plain text or HTML) of an email message.
# Both classes are essential for constructing email messages with multiple parts, such as text, HTML, and attachments.
def create_email_temp(sender_email, receiver_email, email_subject, email_body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_body, 'plain'))
    return msg


# function to send the email through smtp server.

def send_email(sender_email, sender_password, smtp_server, smtp_port, email_message):
    try:
        # connect with the server.
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure TLS connection
        server.login(sender_email, sender_password)  # login to the server

        # send the email.
        server.sendmail(sender_email, email_message['To'], email_message.as_string())
        # close the connection
        server.quit()
        print("Email send successfully!!!!")
    except Exception as ex:
        print(f"Failed to send the message because of {ex}")


if __name__ == "__main__":
    recipient_email, subject, body = users_details()

    # collect senders credentials
    sender_email = input("enter sender's email-id -:")
    sender_password = input("enter sender's password -:")

    # firstly lets configure smtp-:
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # 465 for ssl

    email_message = create_email_temp(sender_email, recipient_email, subject, body)
    send_email(sender_email, sender_password, smtp_server, smtp_port, email_message)

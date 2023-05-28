import csv
import random
import smtplib
from email.mime.text import MIMEText

roundNumber = 1
path = 'C:\\Users\\varun\\OneDrive\\Documents\\responses.csv'

email = 'phoenixseniorassassin2022@gmail.com'

# subject to change based on round

def send_email(email, sender_password, receiver_email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = receiver_email

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, sender_password)
        smtp.send_message(msg)

def assign_targets(csv_file, email, sender_password):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    random.shuffle(rows)

    for i in range(len(rows)):
        current_row = rows[i]
        current_team = current_row['Team']
        target_row = rows[(i + 1) % len(rows)]

        while target_row['Team'] == current_team or target_row['isDead'] == 'Yes':
            target_row = rows[(i + 1) % len(rows)]
        
        current_row['Target'] = target_row['Player']
        current_row['Target Email'] = target_row['Email']

        # Sending email to notify the player of their target
        receiver_email = current_row['Email']
        subject = "Target Assignment"
        message = f"Greetings {current_row['Player']},"
        message2 = "\n\n Welcome to round: "
        message3 = roundNumber + f", your target is: {current_row['Target']}.\n\nBest of luck!\nPhoenix Senior Assasin"

        finalMessage = message + message2 + message3

        send_email(email, sender_password, receiver_email, subject, finalMessage)

    with open(csv_file, 'w', newline='') as file:
        fieldnames = reader.fieldnames + ['Target', 'Target Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Targets assigned")




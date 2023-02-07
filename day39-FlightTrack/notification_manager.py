from twilio.rest import Client
import smtplib

TWILIO_SID = "AC81fb51c61d22fa7c615a5bf2aaeac525"
TWILIO_AUTH_TOKEN = "0e2f263dbd88b0f97551db5fcd19f542"
TWILIO_VIRTUAL_NUMBER = "+12183775794"
TWILIO_VERIFIED_NUMBER = "+905322266228"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, emails, message, link):
        from_addr = "thirtydays03@gmail.com"
        password = "qfuldnvkkjbccidn"

        for email in emails:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=from_addr, password=password)
                connection.sendmail(from_addr=from_addr, to_addrs=email,
                                    msg=f"{message}\n{link}")

from email.message import EmailMessage
import smtplib
import ssl

class EmailService:
    
    def __init__(self, fromEmail, passwordFromEmail, toEmail, subject, body):
        self.fromEmail = fromEmail
        self.passwordFromEmail = passwordFromEmail
        self.toEmail = toEmail
        self.subject = subject
        self.body = body
        self.email = EmailMessage()
    

    def sendEmail(self):
        context = ssl.create_default_context()

        try:
            smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
            smtp.login(self.fromEmail, self.passwordFromEmail)
            smtp.sendmail(self.fromEmail, self.toEmail, self.email.as_string())
            print ("Email sent successfully!")
        except Exception as ex:
            print("Something went wrong")

    def setContent(self):
        self.email['From'] = self.fromEmail
        self.email['To'] = self.toEmail
        self.email['Subject'] = self.subject
        self.email.set_content(self.body)

    def setBody(self, body):
        self.body = body


    

    
    
    




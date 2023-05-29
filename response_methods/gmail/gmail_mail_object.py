import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass


class GmailMailer:
    def __init__(self, 
                login_mail:str=None, 
                passwd:str=None,
                smtp_port:int=587,
                ) -> None:
        
        self.__login = login_mail
        self.__passwd = passwd
        self.__smtp = smtp_port

        self._mail_from = None
        self._mail_to = None

        self.__msg = MIMEMultipart('alternative')
        
        # Connecting to server
        self.server_con = smtplib.SMTP('smtp.gmail.com', self.__smtp)
        self.server_con.ehlo()

    # Additional methods for passig credentials
    def login_password_prompt(self):
        """Displays prompt in terminal, which allows
        for typing in password"""
        self.login_prompt()
        self.password_prompt()

    def login_prompt(self):
        self.__login = input("Email login: ")

    def password_prompt(self):
        self.__passwd = getpass("Email password: ")

    def set_login_creds(self, login, password):
        self.__login = login
        self.__passwd = password

    # Mail details passed before sending
    def mail_details(self, 
                    mail_from:str, 
                    mail_to:str, 
                    subject:str, 
                    txt_message:str=None):

        self._mail_from = mail_from
        self._mail_to = mail_to

        self.__msg['To'] = mail_to
        self.__msg['From'] = mail_from
        self.__msg['Subject'] = subject

        if txt_message:
            txt_message  = MIMEText(str(txt_message))
            self.__msg.attach(txt_message)


    def send(self, assert_credentials = True):
        if assert_credentials:
            assert self.__login, "Email login was not passed!"
            assert self.__passwd, "Email Password was not passed!"
            
        self.server_con.starttls()
        self.server_con.login(self.__login, self.__passwd)
        self.server_con.sendmail(self._mail_from, 
                                 self._mail_to,
                                 self.__msg.as_string())
        self.server_con.quit()
        return True
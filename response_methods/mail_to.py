from .respond_to_user import Responses
from .gmail_emailer import GmailMailer


class GmailResponse(Responses):
    def __init__(self,
                mail_login:str,
                password,
                mail_to:str,
                mail_from=None) -> None:
        
        super().__init__()

        self.gmail = GmailMailer(
            login_mail=mail_login,
            passwd=password)
        
        if not mail_from:
            self._mail_from = mail_login
        else:
            self._mail_from = mail_from
        self._mail_to = mail_to

    def send_response(self, 
                      web_alias, 
                      element_details, 
                      time_of_occurence):
        
        self.gmail.mail_details(
        mail_from=self._mail_from,
        mail_to=self._mail_to,
        subject="|Python Script| Change in webpage structure detected.",
        txt_message=f"""
        Change detected on webpage: {web_alias}
        Changed webpage element: {element_details}.
        Hour of detection: {time_of_occurence}.""")

        self.gmail.send()








from webpage_information import load_webpage_information
from website_refresher import refresh_object
from response_methods import GmailResponse, GmailConfig

from logger import logger
from getpass import getpass
import threading


def main(use_gmail = True,):
    logger.info("===============================================")
    logger.info("Loading user config")
    webpage_user_info_containers = load_webpage_information()
    logger.info(f"Loaded {len(webpage_user_info_containers)} webpage configs")
    logger.info("===============================================")

    logger.info("Setting up response methods")
    response_methods = []
    if use_gmail:
        logger.info("Loading Gmail Config")
        conf = GmailConfig()
        if not conf.mail_pass:
            logger.info("Password for email was not passed in config.")
            conf.mail_pass = getpass("Email Password: ")
            assert conf.mail_pass != "", "Password cannot be empty"
        logger.info("Initializing Gmail object")
        gmail = GmailResponse(conf.mail_from, conf.mail_pass, conf.mail_to)
        response_methods.append(gmail)
    logger.info("===============================================")

    threads = []
    t_lock = threading.Lock()
    for webpage_user_info_container in webpage_user_info_containers:
        arguments = {
            "user_webpage_information":webpage_user_info_container,
            "thread_lock":t_lock,
            "response_elements":response_methods,
            "use_saved_elem_data":False,
            "check_whole_site":False}
        t = threading.Thread(target=refresh_object, kwargs=arguments)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    logger.info("-----------------END------------------")


if __name__ == '__main__':
    main()


 
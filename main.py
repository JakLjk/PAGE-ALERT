from webpage_information import load_webpage_information
from website_refresher import refresh_object
from response_methods import GmailResponse, GmailConfig
from response_methods import FlaskWeb

from logger import logger

from getpass import getpass
import threading


def main(use_gmail=True, use_webapp=True):
    logger.info("===============================================")
    logger.info("Loading webpages configuration info")
    webpage_user_info_containers = load_webpage_information()
    logger.info(f"Loaded {len(webpage_user_info_containers)} webpage configs")
    logger.info("===============================================")

    logger.info("Setting up response methods")
    response_methods = []
    outer_threads = []
    if use_gmail:
        logger.info("Loading Gmail Config")
        conf = GmailConfig()
        assert conf.mail_from != "", "Gmail: mail_from argument not passed in config"
        assert conf.mail_to != "", "Gmail: mail_to argument not passed in config"
        if not conf.mail_pass:
            logger.info("Password for email was not passed in config.")
            conf.mail_pass = getpass("Email Password: ")
            assert conf.mail_pass != "", "Password cannot be empty"
        logger.info("Initializing Gmail object")
        gmail = GmailResponse(conf.mail_from, conf.mail_pass, conf.mail_to)
        response_methods.append(gmail)

    if use_webapp:
        logger.info("Initializing Flask webapp object")
        flask_obj = FlaskWeb
        logger.info("Creating thread for Flask webapp")
        flask_thread = threading.Thread(target=flask_obj)
        response_methods.append(flask_obj)
        outer_threads.append(flask_thread)


    logger.info("Creating thread for Main function")
    comparison_kwargs = {
                "webpage_user_info_containers":webpage_user_info_containers,
                "response_methods":response_methods}
    main_thread = threading.Thread(
                        target=initalize_webpage_comparison,
                        kwargs=comparison_kwargs)
    outer_threads.append(main_thread)
    
    for thread in outer_threads:
         thread.start()
    for thread in outer_threads:
         thread.join()



def initalize_webpage_comparison(**kwargs):
        webpage_user_info_containers = kwargs["webpage_user_info_containers"]
        response_methods = kwargs["response_methods"]

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


 
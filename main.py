from webpage_information import load_webpage_information
from website_refresher import refresh_object

from logger import logger

def main():
    logger.info("Loading user config")
    webpage_user_info_containers = load_webpage_information()
    logger.info(f"Loaded {len(webpage_user_info_containers)} webpage configs")

    for webpage_user_info_container in webpage_user_info_containers:
        refresh_object(
            user_webpage_information=webpage_user_info_container,
            use_saved_elem_data=False,
            check_whole_site=False,)


if __name__ == '__main__':
    main()



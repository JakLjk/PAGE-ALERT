from webpage_information import load_webpage_information
from website_refresher import refresh_object
# from website_refresher import refresh_object



def main():

    # load all webpages general information 

    webpage_user_info_containers = load_webpage_information()
    print(webpage_user_info_containers)
    # for webpage_user_info_container in webpage_user_info_containers:
    #     refresh_object(
    #         user_webpage_information=webpage_user_info_container,
    #         use_saved_elem_data=False, # TODO
    #         check_whole_site=False, # TODO
    #         )
    

if __name__ == '__main__':
    main()



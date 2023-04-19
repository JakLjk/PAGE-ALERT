from webpage import RequestsWebpage, SeleniumWebpage
from load_user_config import load_user_webpage_information

from website_refresher import refresh_object




def main():

    # load all webpages general information 
    webpages_to_check = load_user_webpage_information()

    # TODO initialize refreshing function for every webpage in webpages_to_check
    refresh_object()




if __name__ == '__main__':
    main()


# refresh_object(
#     webpage_info_obj = None,
#     # url='', 
#     # compare_elems = {'t1':e1, 't2':e2}, # key is alias, value is element of webpage that was parsed 
#     web_engine_type = "requests", 
#     check_whole_site=False, 
#     use_saved_elem_data=False,)


# def request_test():
#     r = RequestsWebpage.initialize(url='https://www.kopernikus.pl')
#     print(repr(r))
#     r.get_webpage_content()
#     print(r.webpage_content)

# def selenium_test():
#     s = SeleniumWebpage.initialize(url='https://www.kopernikus.pl')
#     print(repr(s))
#     s.get_webpage_content()
#     print(s.webpage_content)

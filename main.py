from webpage import RequestsWebpage, SeleniumWebpage



# TODO Load file with webpages links and elements to check and times of refresh

# TODO Init webpage objects

# TODO Check if there is prior information stored about webpage structure: if_use_old=True

# TODO 

def request_test():
    r = RequestsWebpage.initialize(url='https://www.kopernikus.pl')
    print(repr(r))
    r.get_webpage_content()
    print(r.webpage_content)

def selenium_test():
    s = SeleniumWebpage.initialize(url='https://www.kopernikus.pl')
    print(repr(s))
    s.get_webpage_content()
    print(s.webpage_content)

def main():
    # request_test()
    selenium_test()


if __name__ == '__main__':
    main()


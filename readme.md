# PAGE_ALERT

PAGE ALERT is a Python library for checking, if webpage source code has changed.

## Usage

1. Fill information about scanned webpage in: configs/webpages:
Config parameters that are in lower case are to be changed according to user will. 
Parameter keys that are UPPER CASE shouldn't be changed - only their values are to be modified
- "webpage_alias" - alias, that will be used to distinguish webpage information passed to user
- "URL" - webpage url
- "CHECK_INTERVAL_MIN" - how often should script check if web structure has changed
- "NUM_OF_RETRIES" - how many times should script run, before it ends. If set to null, script will run indefinitely.
- "element_alias_to_change" - alias of element, that will be used to distinguish elements, if several of them are to be checked on one webpage.
- "ELEMENT_TYPE" - type of webpage element, like: a or div or h1
- "ELEMENT_TAG_TYPE" - type of tag that distinguishes specific element, like: class
- "ELEMENT_TAG_VALUE" - value that is assigned to class.

2. Fill response information in /configs/response_config.json. Credentials will be used to log in into specific response method, in order to send information to user, when webpage element changes.

3. Run main.py
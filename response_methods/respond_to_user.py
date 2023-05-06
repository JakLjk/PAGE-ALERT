from abc import ABC, abstractmethod

class Responses(ABC):
    def __init__(self) -> None:
        pass

    def __repr__(self):
        return "Responses()"
    
    @abstractmethod
    def send_response(self,                      
                      web_alias, 
                      element_details, 
                      time_of_occurence):
        """Send response after finding difference within webpage"""

    @abstractmethod
    def send_failure_info(self,
                    web_alias, 
                    time_of_occurence,
                    error_details):
        """Send repsponse after failure withing webpage compare process"""

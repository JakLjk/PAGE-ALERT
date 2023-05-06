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
        """Used for sending response"""

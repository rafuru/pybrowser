__author__ = 'Ranjith'
from .actions import Action

class Button(Action):

    def __init__(self, driver, locator=None, element=None, wait_time=10, visible=False):
        super().__init__(driver, locator, element, wait_time, visible)
    
    @property
    def button_name(self):
        return self.text

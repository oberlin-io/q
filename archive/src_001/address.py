import re

class Address():
    def __init__(self, add):
        p='\d{3}\.\d{3}\.\d{3}'
        self.add=add

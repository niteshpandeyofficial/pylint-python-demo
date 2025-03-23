"""
Author:Nitesh Pandey
Version:1.0.0
Date:23-03-2025
"""

class MyPerson:
    """
    This Class is used to handle the person details like
    name,age,address etc

    """
    def __init__(self,name,age,addr):
        self.name=name
        self.age=age
        self.addr=addr  # pylint: disable=invalid-name

    def get_name(self):
        """
        This is get name function which is used to get the name of person
        """
        print(f"Name of the Person:{self.name}")

    @staticmethod
    def set_name(name):
        """
        This method is used to set the new name of the person
        """
        print(f"new name of the person is:{name}")
m=MyPerson('Nitesh',34,'Mumbai')
m.get_name()
MyPerson.set_name('Sam')

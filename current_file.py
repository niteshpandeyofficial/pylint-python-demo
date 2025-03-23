class MyPerson:
    def __init__(self,name,age,addr):
        self.name=name
        self.age=age
        self.addr=addr 

    def getName(self):
        print(f"Name of the Person:{self.name}")

    @staticmethod
    def set_name(name):
        print(f"new name of the person is:{name}")
m=MyPerson('Nitesh',34,'Mumbai')
m.getName()
MyPerson.set_name('Sam')

class Mammal:
    def __init__(self,name,sax):
        self.name = name
        self.sax = sax
        self.num_eyes = 2

    def breathe(self):
        print(f"{self.name}在呼吸...")

    def poop(self):
        print(f"{self.name}在拉屎...")

class Human(Mammal):
    def __init__(self,name,sax):
        super().__init__(name,sax)
        self.has_tail = False

    def read(self):
        print(f"{self.name}在阅读...")

class Cat(Mammal):
    def __init__(self,name,sax):
        super().__init__(name,sax)
        self.has_tail = True

    def scratch_sofa(self):
        print(f"{self.name}在抓沙发...")
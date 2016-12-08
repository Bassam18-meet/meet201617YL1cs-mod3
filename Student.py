class Student:
    def __init__ (self,name,hometown,age,height,ice_cream):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.ice_cream=ice_cream
    def print_summary(self):
        print("my name is "+self.name+" ,my age is "+self.age+" ,i live in "+self.hometown+" ,my height is "+self.height+" and my favorite ice cream flavor is "+self.ice_cream)
        

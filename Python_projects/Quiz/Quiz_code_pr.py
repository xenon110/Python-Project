class student:
    def __init__(self,id_no, name, roll):
        self.id_no = id_no
        self.name=name
        self.roll=roll


    def data(self):
        print(self.id_no+ ": Hello everyone my name is " + self.name + " and my roll no is "+ self.roll)

s1=student("101","Xenon","35")
s2=student("102","PYL","102")

s2.data()
s1.name="mayank"
s1.data()
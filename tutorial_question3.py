class Person():
    def __init__(self, fname, sname, address):
        self.f_name = fname
        self.s_name = sname
        self.address = address
        
    def change_address(self, new_address):
        self.address = new_address

    def __str__(self):
        return self.f_name+" "+self.s_name+" lives at "+self.address


# main
p1 = Person("John", "Smith", "1 Pinebrook street")
print(p1.f_name)
print(p1.s_name)
print(p1.address)

p1.change_address("5 Cottage Avenue")
print(p1)

class Par(float):
    def __init__(self, number):
        float.__init__(self)
        self.number = number
        self.name = ""

    def __str__(self):
        if type(self == Par):
            return str(self.number) + "000000   (" + self.name + ")"
        else:
            return str(self.number)


a = Par(1.1)
a.name = 'alpha'

b = Par(2.2)
b.name = 'beta'

t = [1, 2, b, a, a+b, a*b, a/b]

print(t)
t.sort()

for s in t:
    print(s)

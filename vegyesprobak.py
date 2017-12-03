def product(listaa):
    summa = 0
    for i in listaa:
        if (i != 0):
            summa *= i
        return summa
print product([4, 5, 5])


def purify(x):
    result = []
    for n in x:
        if n % 2 == 0:
            result.append(n)
        else:
            n = []
    return result
print purify([1, 2, 3, 4])




def censor(text, word):
    split_text = text.split()
    new_string = ""
    for n in split_text:
        if n == word:
            n = "*" * len(word)
        new_string = new_string +  n + " "
    return new_string
print censor("hey heey heey hesssy","heey")




class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if ((self.angle1 + self.angle2 + self.angle3) == 180):
            return True
        else:
            return False

my_triangle = Triangle(3, 4, 5)
print my_triangle.check_angles()


''''''''''''''''''''''''''''''''''''''''''''''''
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def full_time_wage(self,hours):
        return super(PartTimeEmployee,self).calculate_wage(hours)
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 12.00

employee = Employee("Steve")
partempl = PartTimeEmployee(4)
milton = PartTimeEmployee("Milton")

print employee.employee_name
print employee.calculate_wage(8)
print partempl.calculate_wage(8)

print milton.full_time_wage(10)





''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
nap = ['h', 'kedd', 'szerda', 'cs', 'p', 'szombat', 'v']
a=0
b = 0
while a < 7:
    b = a % 7
    a = a + 1
    print a, nap[b]


'''
ket szam kozott az elso olyan ami oszthato egy megadott szammal
'''
kezdstr=raw_input("kerem az elso szamot")
vegstr=raw_input("kerem a masik szamot")
osztostr=raw_input("oszto?")
kezd=int(kezdstr)
veg=int(vegstr)
oszt=int(osztostr)
if(kezd>veg):
    seged=kezd
    kezd=veg
    veg=seged
while (kezd%oszt != 0) and (kezd<=veg):
    kezd=kezd+1
if(kezd>veg):
    print "nem talalhato ilyen szam"
else:
    print " elso ilyen: ", kezd


#  Complete the following line. Use the line above for help.
even_squares = [i ** 2 for i in range(11) if i * i * i % 4 == 0]
print even_squares

c = ['C' for x in range(5) if x < 3]
print c

l = [i ** 2 for i in range(1, 11, 1)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[1:9:1]

# every odd element
my_list = range(1, 11)  # List of numbers 1 - 10
# Add your code below!
print my_list[::2]

# backwards a list
my_list = range(1, 11)
# Add your code below!
backwards = my_list[::-1]
print backwards

# 1-11 numbers square between 30 and 70
squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)
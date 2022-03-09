# Tạo và gọi hàm cơ bản
def my_function():
  print("Function")

my_function()

#Hàm đối số (ten)
def function1(ten):
  print(ten + " KHDL")
function1("Khoa")

# Số đối số
def function2(ten, so):
  print(ten + " " + so)

function2("Khoa", "2210")

#Nhiều đối số
def function3(*ten):
  print("Hoc sinh trong lop: " + ten[0])

function3("Khoa", "Phuc", "Thang")

#Đối số từ khóa
def function4(student1,student2,student3):
  print("Hoc sinh trong lop: " + student1)

function4(student2 = "Khoa", student1 = "Phuc", student3 = "Thang")

#Đối số từ khóa tùy ý
def function5(**ten):
  print(ten["hs1"])

function5(hs1= "Khoa",hs2 = "Phuc")

# Giá trị tham số mặc định
def my_function(country = "Vietnam"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Chuyển danh sách dạng đối số
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Giá trị trả lại
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Hàm pass
def myfunction():
  pass

#Đệ quy gọi chính nó
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Hàm lambda
x = lambda a : a + 10
print(x(10))
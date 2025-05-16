#Bien
x = 5; #Khai báo biến x có giá trị là 5
name = "Nguyen Long Vu"; #Khai báo biến name có giá trị là "Nguyen Long Vu"
is_valed = True; #Khai báo biến is_valed có giá trị là True

#Không thể dùng từ khóa đặt tên cho biến
#Ví dụ như int, float, str, list, dict, set, tuple hay if = 4;

#Toán tử
a = 10;
b = 5;
result = a + b; #Cộng hai giá trị a và b, kết quả trả về biến result = 15
result = a - b; #Trừ hai giá trị a và b, kết quả trả về biến result = 5
result = a * b; #Nhân hai giá trị a và b, kết quả trả về biến result = 50   
result = a / b; #Chia hai giá trị a và b, kết quả trả về biến result = 2.0
result = a // b; #Chia lấy nguyên hai giá trị a và b, kết quả trả về biến result = 2
remaider = a % b; #Lấy phần dư của phép chia hai giá trị a và b, kết quả trả về biến remainder = 0
result = a ** b; #Lũy thừa hai giá trị a và b, kết quả trả về biến result = 100000

#Logic
c = 5;
d = 10;
#And
result = (a > b) and (c < d); #Kết quả trả về biến result = True
#Or
result = (a > b) or (c > d); #Kết quả trả về biến result = True
#Not
result = not (a > b); #Kết quả trả về biến result = False
#==
result = (a == b); #Kết quả trả về biến result = False
#!=
result = (a != b); #Kết quả trả về biến result = True
# ">" và "<"
result = (a > b); #Kết quả trả về biến result = True
result = (a < b); #Kết quả trả về biến result = False
# ">=" và "<="
result = (a >= b); #Kết quả trả về biến result = True
result = (a <= b); #Kết quả trả về biến result = False

#Nhập, xuất dữ liệu
Isname = input("Nhập tên của bạn: "); #Nhập tên từ bàn phím
print("Xin chào", Isname); #Xuất tên ra màn hình
#sep, end trong hàm print
print("Xin chào", Isname, sep = ",", end = "!"); #Xuất tên, kết quả là "Xin chào, Nguyen Long Vu!"


#Cấu trúc điều khiển
#Câu lệnh if, elif, else
if a > b: #Nếu a lớn hơn b
    print("a lớn hơn b"); #Xuất ra màn hình "a lớn hơn b"
elif a == b: #Nếu a bằng b
    print("a bằng b"); #Xuất ra màn hình "a bằng b"
else:
    print("a nhỏ hơn b"); #Xuất ra màn hình "a nhỏ hơn b"
#Câu lệnh for
Laptop = ["Dell", "HP", "Lenovo", "Asus"]; #Khai báo danh sách Laptop
for i in Laptop: #Duyệt qua từng phần tử trong danh sách Laptop
    print(i); #Xuất ra từng phần tử trong danh sách Laptop
#Câu lệnh while
count = 0; #Khai báo biến count có giá trị là 0
while count < 5: #Khi count nhỏ hơn 5
    print(count); #Xuất ra giá trị của count
    count += 1; #Tăng giá trị của count lên 1
#Câu lệnh nhảy (Jump Statements), gồm break, continue, pass
#Câu lệnh break
for i in range(10): #Duyệt qua từng số từ 0 đến 9
    if i == 5: #Nếu i bằng 5
        break; #Dừng vòng lặp
    print(i); #Xuất ra giá trị của i
#Câu lệnh continue
for i in range(1,11): #Duyệt qua từng số từ 1 đến 10
    if i % 2 == 0: #Nếu i là số chẵn
        continue; #Bỏ qua số chẵn
    print(i); #Xuất ra giá trị của i
#Câu lệnh pass
for i in range(5): #Duyệt qua từng số từ 0 đến 4
    if i == 2: #Nếu i bằng 2
        pass; #Bỏ qua số 2
    print(i); #Xuất ra giá trị của i

#Chuỗi
#Khai báo chuỗi
string = "Hello World"; #Khai báo chuỗi string có giá trị là "Hello World"
#Truy cập vào ký tự trong chuỗi
print(string[0]); #Xuất ra ký tự đầu tiên trong chuỗi string, kết quả là "H"
print(string[1]); #Xuất ra ký tự thứ hai trong chuỗi string, kết quả là "e"
print(string[-1]); #Xuất ra ký tự cuối cùng trong chuỗi string, kết quả là "d"
#Các phép xử lý chuỗi
#Cắt chuỗi
print(string[:5]); #Xuất ra chuỗi từ ký tự thứ 0 đến ký tự thứ 4, kết quả là "Hello"
print(string[6:]); #Xuất ra chuỗi từ ký tự thứ 6 đến hết, kết quả là "World"
#Nối chuỗi
string2 = "Python"; #Khai báo chuỗi string2 có giá trị là "Python"
string3 = string + " " + string2; #Nối chuỗi string và string2, kết quả là "Hello World Python"
#Độ dài chuỗi
length = len(string); #Lấy độ dài của chuỗi string, kết quả là 11
#Một số hàm xử lý chuỗi (Upper, Lower, Strip, Split, Replace)
#Upper
string = string.upper(); #Chuyển đổi chuỗi thành chữ hoa, kết quả là "HELLO WORLD"
#Lower
string = string.lower(); #Chuyển đổi chuỗi thành chữ thường, kết quả là "hello world"
#Strip
string = "   Hello World   "; #Khai báo chuỗi string có giá trị là "   Hello World   "
string = string.strip(); #Xóa khoảng trắng ở đầu và cuối chuỗi, kết quả là "Hello World"
#Split
string = "Hello,World"; #Khai báo chuỗi string có giá trị là "Hello,World"
string = string.split(","); #Tách chuỗi thành danh sách, kết quả là ["Hello", "World"]
#Replace
string = "Hello World"; #Khai báo chuỗi string có giá trị là "Hello World"
string = string.replace("World", "Python"); #Thay thế "World" bằng "Python", kết quả là "Hello Python"

#Hàm
#Khai báo hàm
def add(a, b): #Khai báo hàm add có hai tham số a và b
    return a + b; #Trả về tổng của a và b
#Gọi hàm
print(add(5, 10)); #Gọi hàm add với tham số a = 5 và b = 10, kết quả là 15
#Khai báo và gọi hàm không có tham số
def greet(name): #Khai báo hàm greet có một tham số name
    print("Hello", name); #Xuất ra "Hello" và tên
greet("Nguyen Long Vu"); #Gọi hàm greet với tham số name = "Nguyen Long Vu", kết quả là "Hello Nguyen Long Vu"

#Mảng
from array import array #Nhập thư viện array
#Khai báo mảng số nguyên
arr_int = array('i', [1, 2, 3, 4, 5]); #Khai báo mảng arr có kiểu số nguyên và các phần tử là 1, 2, 3, 4, 5
#Khai báo mảng số thực
arr_float = array('f', [1.0, 2.0, 3.0, 4.0, 5.0]); #Khai báo mảng arr_float có kiểu số thực và các phần tử là 1.0, 2.0, 3.0, 4.0, 5.0
#Truy cập vào phần tử trong mảng
print(arr_int[0]); #Xuất ra phần tử đầu tiên trong mảng arr_int, kết quả là 1
print(arr_float[1]); #Xuất ra phần tử thứ hai trong mảng arr_float, kết quả là 2.0
#Thay đổi giá trị phần tử trong mảng
arr_int[0] = 10; #Thay đổi giá trị phần tử đầu tiên trong mảng arr_int thành 10
#Các phương thức xử lý mảng (append, insert, remove, pop, index, count)
#append
arr_int.append(6); #Thêm phần tử 6 vào cuối mảng arr_int
#insert
arr_int.insert(0, 0); #Thêm phần tử 0 vào đầu mảng arr_int
#remove
arr_int.remove(10); #Xóa phần tử 10 trong mảng arr_int
#pop
arr_int.pop(0); #Xóa phần tử đầu tiên trong mảng arr_int
#index
index = arr_int.index(2); #Lấy chỉ số của phần tử 2 trong mảng arr_int
#count
count = arr_int.count(2); #Đếm số lần xuất hiện của phần tử 2 trong mảng arr_int

#Danh sách (List)
#Khai báo danh sách
list_int = [1, 2, 3, 4, 5]; #Khai báo danh sách list_int có các phần tử là 1, 2, 3, 4, 5
list_float = [1.0, 2.0, 3.0, 4.0, 5.0]; #Khai báo danh sách list_float có các phần tử là 1.0, 2.0, 3.0, 4.0, 5.0
list_string = ["Hello", "World"]; #Khai báo danh sách list_string có các phần tử là "Hello", "World"
#Khai báo danh sách hỗn hợp
list_mixed = [1, 2.0, "Hello", True]; #Khai báo danh sách list_mixed có các phần tử là 1, 2.0, "Hello", True
#Khai báo danh sách rỗng
list_empty = []; #Khai báo danh sách rỗng list_empty
#Truy cập vào phần tử trong danh sách
print(list_int[0]); #Xuất ra phần tử đầu tiên trong danh sách list_int, kết quả là 1
print(list_float[1]); #Xuất ra phần tử thứ hai trong danh sách list_float, kết quả là 2.0
print(list_string[0]); #Xuất ra phần tử đầu tiên trong danh sách list_string, kết quả là "Hello"
#Thay đổi giá trị phần tử trong danh sách
list_int[0] = 10; #Thay đổi giá trị phần tử đầu tiên trong danh sách list_int thành 10
print(list_int.append(6)); #Thêm phần tử 6 vào cuối danh sách list_int
del list_int[0]; #Xóa phần tử đầu tiên trong danh sách list_int
#Duyệt từng phần tử trong danh sách
for i in list_int: #Duyệt qua từng phần tử trong danh sách list_int
    print(i); #Xuất ra từng phần tử trong danh sách list_int

#Kiểu Tuple
#Khai báo tuple
tuple_int = (1, 2, 3, 4, 5); #Khai báo tuple tuple_int có các phần tử là 1, 2, 3, 4, 5
tuple_float = (1.0, 2.0, 3.0, 4.0, 5.0); #Khai báo tuple tuple_float có các phần tử là 1.0, 2.0, 3.0, 4.0, 5.0
tuple_string = ("Hello", "World"); #Khai báo tuple tuple_string có các phần tử là "Hello", "World"
#Khai báo tuple hỗn hợp
tuple_mixed = (1, 2.0, "Hello", True); #Khai báo tuple tuple_mixed có các phần tử là 1, 2.0, "Hello", True
#Truy cập vào phần tử trong tuple
print(tuple_int[0]); #Xuất ra phần tử đầu tiên trong tuple tuple_int, kết quả là 1
print(tuple_float[1]); #Xuất ra phần tử thứ hai trong tuple tuple_float, kết quả là 2.0
print(tuple_string[0]); #Xuất ra phần tử đầu tiên trong tuple tuple_string, kết quả là "Hello"
#Các phương thức xử lý tuple (count, index)
#count
count = tuple_int.count(1); #Đếm số lần xuất hiện của phần tử 1 trong tuple tuple_int
#index
index = tuple_int.index(2); #Lấy chỉ số của phần tử 2 trong tuple tuple_int

#Kiểu Dictionary
#Khai báo dictionary   
dict_int = {1: "one", 2: "two", 3: "three"}; #Khai báo dictionary dict_int có các phần tử là 1: "one", 2: "two", 3: "three"
dict_float = {1.0: "one", 2.0: "two", 3.0: "three"}; #Khai báo dictionary dict_float có các phần tử là 1.0: "one", 2.0: "two", 3.0: "three"
dict_string = {"Hello": "World", "Python": "Programming"}; #Khai báo dictionary dict_string có các phần tử là "Hello": "World", "Python": "Programming"
#Khai báo dictionary hỗn hợp
dict_mixed = {1: "one", 2.0: "two", "Hello": True}; #Khai báo dictionary dict_mixed có các phần tử là 1: "one", 2.0: "two", "Hello": True
#Truy cập vào phần tử trong dictionary
print(dict_int[1]); #Xuất ra phần tử có khóa 1 trong dictionary dict_int, kết quả là "one"
print(dict_float[2.0]); #Xuất ra phần tử có khóa 2.0 trong dictionary dict_float, kết quả là "two"
print(dict_string["Hello"]); #Xuất ra phần tử có khóa "Hello" trong dictionary dict_string, kết quả là "World"
#Thêm hoặc cập nhật phần tử trong dictionary
dict_int[4] = "four"; #Thêm phần tử 4: "four" vào dictionary dict_int
dict_int[1] = "ONE"; #Cập nhật phần tử có khóa 1 thành "ONE"
#Xóa phần tử trong dictionary
del dict_int[1]; #Xóa phần tử có khóa 1 trong dictionary dict_int
#Các phương thức xử lý dictionary (keys, values, items)
#keys
keys = dict_int.keys(); #Lấy tất cả các khóa trong dictionary dict_int
#values
values = dict_int.values(); #Lấy tất cả các giá trị trong dictionary dict_int
#items
items = dict_int.items(); #Lấy tất cả các phần tử trong dictionary dict_int

#OOP (Object Oriented Programming) trong Python
#Khai báo lớp (Class)
class Person: #Khai báo lớp Person
    def __init__(self, name, age): #Hàm khởi tạo
        self.name = name; #Khai báo thuộc tính name
        self.age = age; #Khai báo thuộc tính age
    def greet(self): #Hàm greet
        print("Hello, my name is", self.name); #Xuất ra "Hello, my name is" và tên
#Tạo đối tượng (Object)
person1 = Person("Nguyen Long Vu", 20); #Tạo đối tượng person1 từ lớp Person với tên là "Nguyen Long Vu" và tuổi là 20
print(person1.name); #Xuất ra tên của đối tượng person1, kết quả là "Nguyen Long Vu"
#Khởi tạo (Constructor)
class RAM:
    def __init__(self, name, size): #Hàm khởi tạo
        self.name = name; #Khai báo thuộc tính name
        self.size = size; #Khai báo thuộc tính size
    def get_info(self):
        return f"RAM: {self.name}, Size: {self.size}GB";
#Tạo đối tượng
ram1 = RAM("Corsair", 16); #Tạo đối tượng ram1 từ lớp RAM với tên là "Corsair" và dung lượng là 16GB
ram2 = RAM("Kingston", 8); #Tạo đối tượng ram2 từ lớp RAM với tên là "Kingston" và dung lượng là 8GB
#Xuất thông tin RAM
print(ram1.get_info()); #Xuất thông tin của ram1, kết quả là "RAM: Corsair, Size: 16GB"
print(ram2.get_info()); #Xuất thông tin của ram2, kết quả là "RAM: Kingston, Size: 8GB"

#Thuộc tính (Attributes)
class Laptop:
    def __init__(self, brand, model): #Hàm khởi tạo
        self.brand = brand; #Khai báo thuộc tính brand
        self.model = model; #Khai báo thuộc tính model
    class_laptop = "Laptop"; #Khai báo thuộc tính class_laptop
    def __str__(self): #Hàm chuyển đổi đối tượng thành chuỗi
        return f"{self.brand} {self.model}"; #Trả về chuỗi "brand model"
#Tạo đối tượng từ lớp Laptop và xuất thông tin
laptop1 = Laptop("Dell", "XPS 13"); #Tạo đối tượng laptop1 từ lớp Laptop với thương hiệu là "Dell" và mẫu là "XPS 13"
laptop2 = Laptop("HP", "Spectre x360"); #Tạo đối tượng laptop2 từ lớp Laptop với thương hiệu là "HP" và mẫu là "Spectre x360"
print(laptop1); #Xuất thông tin của laptop1, kết quả là "Dell XPS 13"
print(laptop2); #Xuất thông tin của laptop2, kết quả là "HP Spectre x360"

#Phương thức (Methods)
class Smartphone:
    def __init__(self, brand, model): #Hàm khởi tạo
        self.brand = brand; #Khai báo thuộc tính brand
        self.model = model; #Khai báo thuộc tính model
    def send_message(self, number, message): #Hàm gửi tin nhắn
        print(f"Sending message to {number}: {message} from {self.brand} {self.model}");
#Tạo đối tượng từ lớp Smartphone và gọi điện
smartphone = Smartphone("Samsung", "Galaxy S21"); #Tạo đối tượng smartphone2 từ lớp Smartphone với thương hiệu là "Samsung" và mẫu là "Galaxy S21"
smartphone.send_message("0123456789", "Hello!"); #Gọi hàm gửi tin nhắn với số điện thoại là "0123456789" và nội dung là "Hello!"

#Kế thừa (Inheritance)
#Kế thừa đơn (Single Inheritance)
class Animal: #Khai báo lớp Animal
    def __init__(self, name): #Hàm khởi tạo
        self.name = name; #Khai báo thuộc tính name
    def speak(self): #Hàm speak
        print(f"{self.name} makes a sound"); #Xuất ra "name makes a sound"
class Dog(Animal): #Kế thừa lớp Animal
    def speak(self): #Hàm speak
        print(f"{self.name} barks"); #Xuất ra "name barks"
#Đa kế thừa (Multiple Inheritance)
class Bird: #Khai báo lớp Bird
    def fly(self): #Hàm fly
        print(f"{self.name} flies"); #Xuất ra "name flies"
class Parrot(Dog, Bird): #Kế thừa lớp Dog và Bird
    def speak(self): #Hàm speak
        print(f"{self.name} talks"); #Xuất ra "name talks"

#Đa hình (Polymorphism)
#Đa hình ở thời điểm biên dịch (Compile-time Polymorphism)
#Overloading (Nạp chồng)
class Math: #Khai báo lớp Math
    def add(self, a, b): #Hàm add
        return a + b; #Trả về tổng của a và b
    def add(self, a, b, c): #Hàm add
        return a + b + c; #Trả về tổng của a, b và c
#Overriding (Ghi đè)
class Animal:
    def make_sound(self):
        return "Animal sound"; #Hàm make_sound
class Dog(Animal):
    def make_sound(self):
        return "Woof!"; #Hàm make_sound
class Cat(Animal):
    def make_sound(self):
        return "Meow!"; #Hàm make_sound
#Đa hình ở thời điểm chạy (Run-time Polymorphism)
def animal_sound(animal): #Hàm animal_sound
    return(animal.make_sound()); #Xuất ra âm thanh của động vật
dog = Dog(); #Tạo đối tượng dog từ lớp Dog
cat = Cat(); #Tạo đối tượng cat từ lớp Animal
print(animal_sound(dog)); #Xuất ra âm thanh của chó, kết quả là "Woof!"
print(animal_sound(cat)); #Xuất ra âm thanh của mèo, kết quả là "Meow!"

#Trừu tượng (Abstraction)
from abc import ABC, abstractmethod #Nhập thư viện abc
class Animal(ABC): #Khai báo lớp Animal kế thừa từ lớp ABC
    @abstractmethod #Khai báo phương thức trừu tượng
    def make_sound(self): #Hàm make_sound
        pass; #Không có nội dung
class Dog(Animal): #Kế thừa lớp Animal
    def make_sound(self): #Hàm make_sound
        return "Woof!"; #Xuất ra âm thanh của chó
class Cat(Animal): #Kế thừa lớp Animal
    def make_sound(self): #Hàm make_sound
        return "Meow!"; #Xuất ra âm thanh của mèo
#Tạo đối tượng từ lớp Dog và Cat
dog = Dog(); #Tạo đối tượng dog từ lớp Dog
cat = Cat(); #Tạo đối tượng cat từ lớp Cat
#Xuất âm thanh của chó và mèo
print(dog.make_sound()); #Xuất ra âm thanh của chó, kết quả là "Woof!"
print(cat.make_sound()); #Xuất ra âm thanh của mèo, kết quả là "Meow!"


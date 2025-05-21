#Cau1
#Nhập tên, tuổi
name = input("Nhập tên của bạn: ")
age = input("Nhập tuổi của bạn: ")
#In ra tên và tuổi
print("Xin chào " + name + ", bạn " + age + " tuổi.")

#Cau2
#Nhập bán kính
radius = float(input("Nhập bán kính hình tròn: "))
#Tính và in ra diện tích
area = 3.14 * radius ** 2
print("Diện tích hình tròn có bán kính " + str(radius) + " là: " + str(area))

#Cau3
#Nhập số và kiểm tra chẳn lẻ
number = int(input("Nhập một số nguyên: "))
if number % 2 == 0:
    print(str(number) + " là số chẵn.")
else:
    print(str(number) + " là số lẻ.")

#Cau4
#Tạo danh sách để lưu các số trong khoảng từ 2000 đến 3200 chia hết cho 7 và không là bội số của 5
numbers = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(str(i))
#In ra danh sách
print("Các số trong khoảng từ 2000 đến 3200 chia hết cho 7 và không là bội số của 5 là: " + ", ".join(numbers))

#Cau5
sogiolam = int(input("Nhập số giờ làm mỗi tuần: "))
luonggio = int(input("Nhập lương mỗi giờ: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam - giotieuchuan)
luongthucnhan = giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5
print("Lương thực nhận là: " + str(luongthucnhan))

#Cau6
input_str = input("Nhập x, y: ")
dimensions = [int(x) for x in input_str.split(",")]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for j in range(colNum)] for i in range(rowNum)]
for i in range(rowNum):
    for j in range(colNum):
        multilist[i][j] = i * j
print("Ma trận là:")
for i in range(rowNum):
    for j in range(colNum):
        print(multilist[i][j], end=" ")
    print()

#Cau7
print("Nhập vào các dòng văn bảng (để kết thúc nhập, nhập 'done'):")
lines = []
while True:
    line = input()
    if line == 'done':
        break
    lines.append(line)
#Chuyển thành in hoa và in ra màn hình
print("Các dòng văn bản đã nhập là:")
for line in lines:
    print(line.upper())

#Cau8
#Hàm kiểm tra số nhị phân có chia hết cho 5 hay không
def check_binary_divisible_by_5(binary_str):
    decimal_value = int(binary_str, 2)
    if decimal_value % 5 == 0:
        return True
    else:
        return False
#Nhập số nhị phân
binary_str = input("Nhập số nhị phân: ")
#Tách chuỗi và kiểm tra 
binary_str_list = binary_str.split(",")
binary_str_divisible_5 = [binary for binary in binary_str_list if check_binary_divisible_by_5(binary)]
#In ra các số nhị phân chia hết cho 5
if len(binary_str_divisible_5) > 0:
    print("Các số nhị phân chia hết cho 5 là: " + ", ".join(binary_str_divisible_5))
else:
    print("Không có số nhị phân nào chia hết cho 5.")

#Cau9
#Kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#Nhập số nguyên
number = int(input("Nhập một số nguyên: "))
#Kiểm tra và in ra số nguyên tố
if is_prime(number):
    print(str(number) + " là số nguyên tố.")
else:
    print(str(number) + " không phải là số nguyên tố.")

#Cau10
#Đảo ngược chuỗi
def reverse_string(s):
    return s[::-1]
#Nhập chuỗi
string = input("Nhập một chuỗi: ")
print("Chuỗi đảo ngược là: " + reverse_string(string))



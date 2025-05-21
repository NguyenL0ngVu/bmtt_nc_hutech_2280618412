#Cau 1
#Tổng các số chẳn trong List
def sumEvenNum(lst):
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum += i
    return sum
#Nhập List
input_list = input("Nhập các số trong List (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(",")))

#Tính tổng các số chẳn và in ra
result = sumEvenNum(numbers)
print("Tổng các số chẳn trong List là:", result)

#Cau 2
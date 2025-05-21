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
#Đảo ngược vị trí các phần tử trong List
def reverseList(lst):
    return lst[::-1]
#Nhập List
input_list = input("Nhập các số trong List (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(",")))
#Đảo ngược List và in ra
reversed_list = reverseList(numbers)
print("List sau khi đảo ngược là:", reversed_list)

#Cau 3
#Tạo Tuple từ một List
def listToTuple(lst):
    return tuple(lst)
#Nhập List
input_list = input("Nhập các số trong List (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(",")))
#Chuyển List thành Tuple và in ra
tuple_result = listToTuple(numbers)
print("List là:", numbers)
print("Tuple từ List là:", tuple_result)

#Cau 4
#Truy cập phần tử đầu và cuối của Tuple
def accessTupleElements(tup):
    first_element = tup[0]
    last_element = tup[-1]
    return first_element, last_element
#Nhập Tuple
input_tuple = input("Nhập các số trong Tuple (cách nhau bởi dấu phẩy): ")
numbers = tuple(map(int, input_tuple.split(",")))
#Truy cập phần tử đầu và cuối của Tuple và in ra
first_element, last_element = accessTupleElements(numbers)
print("Phần tử đầu tiên trong Tuple là:", first_element)
print("Phần tử cuối cùng trong Tuple là:", last_element)

#Cau 5
#Đém số lần xuất hiện của một phần tử trong List và lưu vào Dictionary
def countOccurrences(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
#Nhập List
input_list = input("Nhập các số trong List (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(",")))
#Đếm số lần xuất hiện của các phần tử trong List và lưu vào Dictionary
occurrences_dict = countOccurrences(numbers)
#In ra Dictionary
print("Số lần xuất hiện của các phần tử trong List là:")


#Cau 6
#Xóa 1 phần tử từ Dictionary theo key
def removeKeyFromDict(d, key):
    if key in d:
        return True
    else:
        return False
#Nhập Dictionary
input_dict = input("Nhập Dictionary (cách nhau bởi dấu phẩy): ")
numbers = dict(map(str, input_dict.split(",")))
#Nhập key cần xóa
key_to_remove = input("Nhập key cần xóa: ")
#Xóa key khỏi Dictionary
if removeKeyFromDict(numbers, key_to_remove):
    del numbers[key_to_remove]
    print("Dictionary sau khi xóa key", key_to_remove, "là:", numbers)
else:
    print("Key", key_to_remove, "không tồn tại trong Dictionary.")
for key, value in occurrences_dict.items():
    print(key, ":", value)
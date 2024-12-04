import mymodule 

n = int(input("Nhập số lượng phần tử của danh sách: "))

lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

sorted_lst = mymodule.sort_list(lst)
max_value = mymodule.find_max(lst)
min_value = sorted_lst[0]

print("Danh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)

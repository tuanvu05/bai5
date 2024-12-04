import mymodule

n = int(input("Nhập số lượng phần tử của danh sách: "))

lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

sorted_lst = mymodule.sort_list(lst)
max_value = mymodule.find_max(lst)
min_value = sorted_lst[0]

max_index = lst.index(max_value) 
min_index = lst.index(min_value) 

print("Danh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất:", max_value, "ở vị trí:", max_index)
print("Phần tử nhỏ nhất:", min_value, "ở vị trí:", min_index)

import sort_module  

n = int(input("Nhập số lượng phần tử trong danh sách: "))

nlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(value)

sorted_list = sort_module.bubbleSort(nlist)

print("Danh sách sau khi sắp xếp:")
print(sorted_list)

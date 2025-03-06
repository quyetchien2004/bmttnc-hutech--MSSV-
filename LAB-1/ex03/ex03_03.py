def taotupletulist(lst):
    return tuple(lst)
inputlist = input("nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int,inputlist.split(',')))
mytuple = taotupletulist(numbers)
print("list: ",numbers)
print("tuple từ list:",mytuple)
def truycapphantu(tuple_data):
    firstelement = tuple_data[0]
    lastelement = tuple_data[-1]
    return firstelement,lastelement
input_tuple = eval(input("nhập tuple, ví dụ(1,2,3):"))
first,last = truycapphantu(input_tuple)
print("Phần tử đầu tiên:",first)
print("Phần tử cuối cùng:",last)
    
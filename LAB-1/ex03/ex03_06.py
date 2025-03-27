def xoaphantu(dictionary,key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a':1, 'b':2, 'c':3,'d':4}
keytodelete = 'b'
result = xoaphantu(my_dict,keytodelete)
if result:
    print("phần tử đã được xoá từ Dictionary:",my_dict)
else:
    print("không tìm thấy phần tử cần xoá trong Dictionary.")
    
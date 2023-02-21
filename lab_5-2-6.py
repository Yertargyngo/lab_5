def suryptau(list):
    if list == sorted(list):
        return True
    elif list == sorted(list, reverse=True):
        return False
    elif list != sorted(list):
        return False
 
print(suryptau([6 , 2 , 18 , 9]))


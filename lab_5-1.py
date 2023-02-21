print("\n")
print("\tResume:")
print("\n")
my_list = ['Name: Yertargyn' , 'Last Name: Berdibek' , 'Age: 20' , 'Specific: Computer Science' , 
           'Course: 3' , 'Position: Student' , 'University: Satbayev University' , 
           'Oblys: Mangystau oblysy' , 'Qala: Aktau qalasy']
print("\n".join(my_list))

print("\n")
my_list.append("Hobby: Reading books")
print("\n".join(my_list)) #1

print("\n")
gender = ["Gender: Man"]
my_list.extend(gender)
print("\n".join(my_list)) #2

print("\n")
my_list.insert(2 , "Birthday: 11-08-2003")
print("\n".join(my_list))  #3

print("\n")
my_list.pop(5)
print("\n".join(my_list)) #4

print("\n")
my_list.clear()
print("\n".join(my_list))  #5


# 1. Тізімде қолданылатын кемінде 5 функциядарды қолданып,
# программа жазып шығу. Тізім ретінде əр студент өзінің
# резюмесін ұсынсын. Жəне сол тізіммен жұмыс жасасын.

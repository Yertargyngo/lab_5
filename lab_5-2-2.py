def student():
    list_stu = ["Yertargyn" , "Bauyrzhan" , "Almatbek"]
    list_yer_sub = ["Computer Science: 5" , "Information security: 4", "Cybernetics: 5"]
    list_alm_sub = ["Computer Science: 3" , "Information security: 2", "Cybernetics: 4"]
    list_bau_sub = ["Computer Science: 4" , "Information security: 5", "Cybernetics: 3"]
    print("Name student: ")
    n = input()
    if n == "Yertargyn":
            print("\n" .join(list_yer_sub))
    elif n == "Bauyrzhan":
            print("\n" .join(list_bau_sub))
    elif n == "Almatbek":
            print("\n" .join(list_alm_sub))
    else:
        print("No students")    
        


print(student())            

        


# Тізім қайтаратын функция жазып шығу. Алдын ала студенттердің
# пəндері жəне бағалары бар тізім құрастыр. Жəне сол тізім бойынша
# студенттің атын еңгізген кезде, сол студенттің бағаларын шығарып
# бертін болсын.

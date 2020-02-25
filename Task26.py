def list_func():
    list_ = [10, 45, 85, 12, 46, 78]
    lst_2 = []
    list_3 = []
    for i in list_:
        if i % 2 == 0:
            lst_2.append(i)
        elif i % 2 != 0:
            list_3.append(i)
    res_2 = len(lst_2)
    res_3 = len(list_3)
    print(f"У вас {res_2} четных чисел")
    print(f"У вас {res_3} нечетных чисел")
list_func()
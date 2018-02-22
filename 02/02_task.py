# 02_task.py

while True:
    try:
        a = input("Input a: ")
        b = input("Input b: ")
        if not (-10) ** 9 < int(a) < 10 ** 9:
            raise Exception("Error in a, please input again ((-10)**9 < a < 10**9)")
        if not (-10) ** 9 < int(b) < 10 ** 9:
            raise Exception("Error in b, please input again ((-10)**9 < b < 10**9)")
    except (Exception, ValueError) as e:
        print(e)
    else:
        break


# Making max value from inputted number
def increase_value(value):
    make_list_of_int(value)
    value.sort(reverse=True)
    return create_new_value(value)


# Making min value from inputted number
def reduce_value(value):
    make_list_of_int(value)
    value.sort()
    for i in range(len(value)):
        if value[0] == 0 and value[i] != 0:
            value[0] = value[i]
            value[i] = 0
    return create_new_value(value)


# Making new value for reduce_value, increase_value functions
def create_new_value(value):
    for i in range(len(value)):
        value[i] = str(value[i])
    return int(''.join(value))


# Changing type of value to int
def make_list_of_int(value):
    for i in range(len(value)):
        value[i] = int(value[i])
    return value


l1 = list(a)
l2 = list(b)

if int(a) >= 0 and int(b) >= 0:
    print(increase_value(l1) - reduce_value(l2))
elif int(a) <= 0 and int(b) >= 0:
    del l1[0]
    print(-reduce_value(l1) - reduce_value(l2))
elif int(a) >= 0 and int(b) <= 0:
    del l2[0]
    print(increase_value(l1) + increase_value(l2))
elif int(a) <= 0 and int(b) <= 0:
    del l1[0]
    del l2[0]
    print(increase_value(l2) - reduce_value(l1))


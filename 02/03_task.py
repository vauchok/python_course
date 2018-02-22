# 03_task.py

while True:
    try:
        x = int(input("Input x: "))
        y = int(input("Input y: "))
        if not 0 <= x < 2 ** 31:
            raise Exception("Error in x, please input again (0 ≤ x ≤ 2**31)")
        if not 0 <= y < 2 ** 31:
            raise Exception("Error in y, please input again (0 ≤ y ≤ 2**31)")
    except (Exception, ValueError) as e:
        print(e)
    else:
        break


# Finding hamming distance
def hamming_distance(value1, value2):
    return sum(element1 != element2 for element1, element2 in zip(value1, value2))


# Generalization
def general_form(value1, value2):
    return ''.join(['0'] * (len(value1) - len(value2)) + list(value2))


s1 = bin(x)[2:]
s2 = bin(y)[2:]

if len(s1) > len(s2):
    s2 = general_form(s1, s2)
elif len(s1) < len(s2):
    s1 = general_form(s2, s1)
print(hamming_distance(s1, s2))

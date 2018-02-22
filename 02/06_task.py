# 06_task.py

while True:
    try:
        n = int(input("Input N: "))

        mask = []
        for i in range(n):
            mask.append(input())

        m = int(input("Input M: "))
        if not 0 <= n <= 10**4:
            raise Exception("Wrong value, please input again (0 ≤ M ≤ 10000)")

        ip = []
        for i in range(m):
            ip.append(input())

    except (Exception, ValueError) as e:
        print(e)
    else:
        break

for i in range(m):
    number = 0
    for t in range(n):
        k = 0
        for j in range(0, 4):
            if int(mask[t].split('.')[j]) & int(ip[i].split(' ')[0].split('.')[j]) == int(mask[t].split('.')[j]) & int(ip[i].split(' ')[1].split('.')[j]):
                k += 1
        if k == 4:
            number += 1
    print(number)


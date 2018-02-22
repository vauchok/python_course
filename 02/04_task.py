# 04_task.py

while True:
    try:
        n = int(input("Input N (N <= 100): "))
        if not 0 < n < 100:
            raise Exception("Wrong value, please input again (N ≤ 100)")
    except (Exception, ValueError) as e:
        print(e)
    else:
        break

# Making list of people
while True:
    try:
        list_of_people = []
        for i in range(n):
            list_of_people.append(input().split())
        for i in range(len(list_of_people)):
            for j in range(0, 2):
                list_of_people[i][j] = int(list_of_people[i][j])
        for i in range(len(list_of_people)):
            if not 1 <= list_of_people[i][0] <= 100:
                raise Exception("Wrong value, please input again (1 ≤ V ≤ 100)")
            if list_of_people[i][1] not in {0, 1}:
                raise Exception("Wrong value, please input again (S – 0 or 1)")
    except (Exception, IndexError, ValueError) as e:
        print(e)
    else:
        break

# Finding the oldest man
V = 0
number = 0
for i in range(len(list_of_people)):
    if list_of_people[i][1] == 1 and list_of_people[i][0] > V:
        V = list_of_people[i][0]
        number = i + 1
if V == 0:
    print(-1)
else:
print(number)

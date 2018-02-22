# 05_task.py

while True:
    try:
        s = input("Input a string which contains only lowercase English characters: ")
        if not 3 < len(s) < 10**4:
            raise Exception("Error, please input a string again (3 ≤ len(S) ≤ 10**4)")
    except Exception as e:
        print(e)
    else:
        break

# Making string of non repeatable characters
characters = ''
for i in s:
    if i not in characters:
        characters += i

# Making list of the number of each character
values = []
for i in range(len(characters)):
        values.append(s.count(characters[i]))

# Making sorted dictionary from characters and values
d = sorted((dict(zip(characters, values))).items(), key=lambda x: x[1], reverse=True)

for i in range(0, 3):
print("{:} {:}".format(d[i][0], d[i][1]))

print("Это мои первые строчки кода")
print(1 + 2)
print(2 + 4 / 6 * 10)
print(9 // 4)
name = 10
print(name)
i = "Это мои первые строчки кода"
print(i)
n = "10"
m = 20
print(int(n) + m)
print(1)
print("1")
print(n + str(m))
print(f"{n}{m}")
j = f"{m}-''это переменная'"
print(j)
print(n, m)
print(n, f"\n{m}")
name1 = input("Введите число ")
name2 = input("Введите число ")
print(name1 + name2)
name1 = int(input("Введите число "))
name2 = int(input("Введите число "))
print(name1 + name2)
m += 1

# Next

name1 = 10
name2 = 20

if name1 == name2:
    print("name1 > name2")
if name1 >= name2 is True:
    print("True")
    pass
elif name1 < name2:
    print("name1 < name2")
elif name1 != name2:
    pass
else:
    print("name1 = name2")

"""

print("Test message")

"""

for i in 1, 2, 3, "sorry":
    print(i)

for o in "sorry":
    print(o)

# Список [], Кортедж()
n = [1, 2, 3, "sorry"]
for p in n:
    print(p)

m = [1, 2, 3, "sorry"]
print(m[3])

m.append(10)
print(m[4])

o = 0
while o < 10:
    print(o)
    o += 1

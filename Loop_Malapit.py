# By Two's
print("By 2")
for x in range(2,12,2):
    print(x)
print()

# By Three's
print("By 3")
for y in range(3,18,3):
    print(y)
print()

# By Four's
print("By 4")
for z in range(4,24,4):
    print(z)
print()

# By Twelve's
print("By 12")
for a in range(12,72,12):
    print(a)
print()

# Multiplication table
print("MULTIPLICATION TABLE")
for multi in range(10,21):
    for table in range(1,11):
        print(multi*table, end='\t')
    print()

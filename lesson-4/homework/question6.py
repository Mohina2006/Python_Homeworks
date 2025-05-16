
for i in range(1, 101):
    count = 0
    for j in range(2, i + 1):
        if i % j == 0:
            count += 1
    if count == 1:
        print(i)
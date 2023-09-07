first_num = 0
second_num = 1
print(first_num)
for i in range(9):
    next_num = first_num + second_num
    print(next_num)
    first_num = second_num
    second_num = next_num

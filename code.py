num =  input().split()

first_num = num[0]
second_num = num[1]

smallest_num = min(len(first_num), len(second_num))

count = 0

for i in range(1, smallest_num+1):
    sum_of = int(first_num[-i]) + int(second_num[-i])
    if sum_of >= 10:
        count += 1
        
if count == 0:
    print("Easy")
else:
    print("Hard")

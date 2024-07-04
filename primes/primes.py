def is_prime(num):
    times = 0
    if num % 1 == 0 and num % num == 0:
        for i in range(1, num+1):
            if num % i == 0:
                times += 1
        if times > 2:
            return False
        else:
            return True
    else:
        return None

for i in range(1, 40):
    if is_prime(i + 1):
        print(i + 1, end=" ")
# print()
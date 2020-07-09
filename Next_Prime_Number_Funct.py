# Given a number, return the next higher prime number:

def next_prime(num):
    prime1 = False
    if num <= 0:
        return ("2 is next prime!")
    elif num > 0:
        while prime1 == False:
            num += 1
            if is_prime(num):
                return (f"{num} is next prime!")
                break
            elif not is_prime(num):
                continue
    else:
        return ("Please input a number.")

def is_prime(num):
    dvsr_lst = []
    if num > 0:
        for i in range(1, num//2+1):
            if num % i == 0:
                dvsr_lst.append(i)
            elif num % i != 0:
                continue
        dvsr_lst.append(num)
        if int(len(dvsr_lst)) > 2:
            return False
        else:
            return True


user_input = (
    int(float(input("Enter a number to find its next higher prime number: "))))
print(next_prime(user_input))

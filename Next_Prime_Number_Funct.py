# Given a number, return the next higher prime number:

def next_prime(num):
    is_prime = False
    while is_prime == False:
        num += 1
        are_you_prime(num)
        if are_you_prime(num) == True:
            return (f"{num} is next prime!")
            break
        elif are_you_prime(num) == False:
            continue


def are_you_prime(num):
    is_prime = False
    dvsr_lst = []
    for i in range(2, num//2+1):
        if num % i == 0:
            dvsr_lst.append(i)
        elif num % i != 0:
            continue
    dvsr_lst.append(num)
    if int(len(dvsr_lst)) > 2:
        return is_prime
    else:
        is_prime = True
        return is_prime


user_input = (
    int(input("Enter a number to find its next higher prime number: ")))
print(next_prime(user_input))

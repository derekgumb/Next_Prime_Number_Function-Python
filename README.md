This code takes in a user-inputted number and outputs the next higher prime number.


The code is broken up into two functions:

1) next_prime() which uses a while loop to continually add +1 to the user-inputted number and call the are_you_prime() function on that.

2) are_you_prime() uses a boolean flag to trigger if the number is found to have only 1 and itself as divisors.

If are_you_prime() returns true, then the next_prime()'s while loop breaks and the output is returned: f"({num} is next prime!)"
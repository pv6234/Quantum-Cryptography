from math import gcd
N = 21
x = 8
gcd(N, x) == 1


def multiplicative_order(a, n):
    order = 1
    mod_exp = a
    while mod_exp != 1:
        order += 1
        mod_exp = (mod_exp * a) % n
    return order

def visualize(a, n):
    for i in range(1, 9):
        o = a**i % n
        print("{}^{} mod {} = {}".format(a, i, n, o))

visualize(x, N)
r = multiplicative_order(x, N)
print("Order/Period = {}".format(r))




factor1 = gcd(N, (x**(r//2)+1)) # gcd(21, 9)
factor2 = gcd(N, (x**(r//2)-1)) # gcd(21, 7)
print("Prime factors of {} is {} {}".format(N, factor1, factor2))
              
              
              
              
from IPython.display import display, Math, Latex
display(Math(r'x^{r} \equiv 1\: mod\: N'))
print(x**2 % N == 1 % N) # 8^2 mod 21 = 1 mod 21  

display(Math(r'x^{r} - 1^{r} \equiv 0\: mod\: N'))
print((x**2 - 1**2) % N == 0 % N) # 8^2 - 1^2 mod 21 = 0 mod 21

display(Math(r'(x^{\frac{r}{2}}+1)(x^{\frac{r}{2}}-1)\: |\:  21'))
print(((x+1)*(x-1)) % N == 0) # 21 is divisible by (8+1)(8-1)  

from random import randint

def solve(n):
    while True:
        # Step 1
        # starts from 2 because 1 power anything is 1
        x = randint(2, n-1)
        tmp = gcd(x,n)
        if tmp != 1:
            print('We got lucky! Factor of {} is {} and {}!'.format(n, tmp, n//tmp))
            return [tmp, n//tmp]
        print('Generated random integer x: {}'.format(x))

        # Step 2
        # In actual shor's algorithm quantum fourier transform will be implemented here.
        r = multiplicative_order(x, n)
        print('Multiplicative Order of {} mod {} => {}'.format(x, n, r))

        # Step 3
        if r % 2 != 0:
            print('{} is not even :( going back to first step...\n'.format(r))
            continue
        elif (x**(r//2)+1) % n == 0:
            print('{} is a multiple of n :( back to first step...\n'.format(r))
            continue
        else:
            factor1 = gcd(n, (x**(r//2)+1))
            factor2 = gcd(n, (x**(r//2)-1))
        return [factor1, factor2]
  
                          
                          
n = 80609
factors = solve(n)
print('Factor of {} is {} and {}\n'.format(n, factors[0], factors[1]))

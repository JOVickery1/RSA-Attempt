import numpy as np
import secrets

def get_gcd(a, b):
    """
    input: two integers a and b
    output: their greatest common divisor
    """
    if a < b:
        c = a
        a = b
        b = c
    r = a%b
    while r:
        a = b
        b = r
        r = a%b
    return b

def is_prime(e):
    """
    input: e - an integer
    returns: prime_flag - boolean: True if e is prime
    """
    prime_flag = True
    for i in range(2, int(np.sqrt(e))):
        if e % i == 0:
            prime_flag = False
    
    return prime_flag
            

def get_e(phi):
    """
    input: phi - an integer phi
    returns: e - an integer that is coprime with phi
    """
    coprime = False
    while not coprime:
        e = secrets.randbelow(phi-1)+1
        # print(f'e = {e}')
        if is_prime(e) and get_gcd(e,phi) == 1:
            coprime = True
    
    return e

def get_d(e, phi):
    """
    inputs: e - an integer; phi - an integer
    returns: d - an integer that is e^(-1) mod phi
    """
    for d in range(phi):
        if (d*e)%phi == 1:
            return d


p = 13
q = 11
n = p*q
print("n: ", n)
phi = (p-1)*(q-1)
print("phi: ", phi)
e = get_e(phi)
print("e: ", e)
d = get_d(e,phi)
# d = 1/e
print("d: ", d)

m = 18
c = m^e%n


print(f'Original message: {m}')
print(f'Ecrypted message: {c}')
print(f'Decrypted message: {c^d%n}')


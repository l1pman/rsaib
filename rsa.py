import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Числа должны быть простыми!')
    elif p == q:
        raise ValueError('Числа не должны быть одинаковыми!')
    n = p * q

    phi = (p-1) * (q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    dba = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in dba]
    return ''.join(plain)


if __name__ == '__main__':

    print("^^^")
    print("RSA")
    print("___")
    print(" ")

    p = int(random.randrange(1,10000))
    q = int(random.randrange(1,10000))

    while not is_prime(p): 
        p = int(random.randrange(1,10000))
    while not is_prime(q): 
        q = int(random.randrange(1,10000))
    
    public, private = generate_key_pair(p, q)

    print("Public key: ", public)
    print("Private key: ", private)

    message = input("Введите сообщение: ")
    encrypted_msg = encrypt(public, message)

    print("Зашифрованное сообщение: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print("Дешифруем . . . ")
    print("Ваше сообщение: ", decrypt(private, encrypted_msg))
    print(" ")
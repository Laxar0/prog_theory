def plus(a,b):
    return int(a) + int(b)

def minus(a,b):
    return int(a)-int(b)

def mult(a,b):
    return int(a)*int(b)

def div(a,b):
    return int(a)/int(b)



def main():
    a = input("a: ")
    b = input("b: ")
    d = input("add(a), minus(m), multiply(mu) or divide(d): ")
    if d == 'a':
        print(plus(a, b))
    elif d == 'm':
        print(minus(a, b))
    elif d == 'mu':
        print(mult(a, b))
    elif d == 'd':
        print(div(a, b))
    else:
        print("You are wrote wrong operation")


import random

print("Welcome to the Brain Games!\n")
print("May I have your name?\n")
name = input()
print (f"Hello {name}")
def nok (a,b,c):
    if a > b & a > c:
        high = a
    elif b > a & b > c:
        high = b
    else:
        high = c
    while True:
        if high % a == 0 & high % b == 0 & high % c == 0:
            Nok = high
            break
        high += 1
    return Nok

def rnd():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    return a, b, c
while True:
    a, b, c = rnd()
    print("Find the smallest common multiple of given numbers.\n")
    print(f"Question: {a}, {b}, {c}\n")
    print("Your answer: ")
    answer = int(input())
    if answer == nok(a, b, c):
        print("Correct! Lets try again!\n")
    else:
        print(f"Wrong! Correct is {nok(a, b, c)}")


    
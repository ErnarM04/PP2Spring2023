def ounces(grams):
    print(grams * 28.3495231)

gramm = float(input())
ounces(gramm)

def centigrade(f):
    print((5 / 9) * (f - 32))

faren = float(input())
centigrade(faren)

def solve(numheads,numlegs):
    for i in range(0, numheads):
        if (numheads - i) * 4 + i * 2 == numlegs:
            print(i)
            break
head = int(input())
leg = int(input())
solve(head, leg)

def filter_prime(list):
    for i in range(0, len(list)):
        if list[i] % 2 == 0:
            print(list[i])
list = input()
filter_prime(list)

from itertools import permutations
def perm(strg):
    for i in list(permutations(strg)):
        print(i)
a = input().split()
perm(a)

def reverse(strg):
    rev = strg[::-1]
    print(rev)
a = input().split()
reverse(a)

def has_33(lst):
    if "3 3" in lst:
        return True
    return False
a = input().split()
print(has_33(a))

import math
def vol_sph(rad):
    print((4/3)*math.pi*(rad**3))
radius = float(input())
vol_sph(radius)

def dupl(lst):
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    print(lst2, end=' ')
a = input().split()
dupl(a)

def palindrome(word):
    rev = word[::-1]
    if rev == word:
        return True
    return False
wrd = input().split()
print(palindrome(wrd))

def histogram(lst):
    for i in lst:
        print('*' * int(i))
a = input().split()
histogram(a)

import random
def game(a, rand, user, cnt):
    if a == rand:
        print("Good job,", user+"!", "You guessed my number in", cnt, "guesses!")
    elif a < rand:
        print("Your guess is too low.")
    else:
        print("Your guess is too more.")
user = input("Hello! What is your name?")
rand = random.randint(1, 12)
a = cnt = 0
print("Well,", user+",", "I am thinking of a number between 1 and 20.")
while a != rand:
    a = int(input("Take a guess."))
    cnt+=1
    game(a, rand, user, cnt)
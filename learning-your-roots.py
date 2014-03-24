__author__ = 'nakter'

import random

def roots(fileName):
    text = open(fileName, "r")

    roots={}
    for line in text:
        parts = line.split(":")
        roots[parts[0]] = parts[1]

    return roots

def rand(roots):
    randDef = []

    for key,value in roots:
        randDef.append(value)

    random.shuffle(randDef)
    return randDef

def prints(roots):
    for key,val in roots.items():
        print(val)
        print(rand([0]))
        print(rand([1]))
        print(rand([2]))

def root_learning(roots):
    for key,val in roots.items():
        print(key,"\n")
        print(random.shuffle(prints()))

def main():
    text = roots("roots.txt")
    print(root_learning(text))
main()

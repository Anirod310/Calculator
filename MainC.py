import math
import sys
import operator
from unittest import result

#  python3 1Calculette.py
#  C:\Users\bouse\Desktop\Programmes\Python\Projets\1Calculette

ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}

user_input = input("Bienvenue! Quel est votre calcul? ", )
split_calcul = user_input.split()

left_side_list = int(split_calcul[0])
right_side_list = int(split_calcul[2])

result = ops[split_calcul[1]](left_side_list, right_side_list )

print(f"Votre résultat est {result}")

           
        








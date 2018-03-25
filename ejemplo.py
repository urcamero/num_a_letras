"""Un pequeno shell interactivo a manera de test"""
from num_to_letter import to_letter
import os

def main():

    num = ''
    while len(num) == 0:
        os.system('cls')
        num = str(input("\nIngrese una cantidad entre '1' y '99,000,000.99' >>> "))
        while len(num) > 8 or num.isalpha() == True:
            os.system('cls')
            num = str(input("\nError \n\t==> Ingrese una cantidad entre '1' y '99,000,000.99' >>> "))
        print(to_letter(num))


if __name__ == '__main__':
    main()

"""Un pequeno shell interactivo a manera de test"""

from num_to_letter import to_letter
import os

def main():

    while(True): 
        os.system('cls')
        num = str(input("\nIngrese una cantidad entre '1' y '99,000,000' >>> "))
        while len(num) > 8 or num.isdigit() == False:
            os.system('cls')
            num = str(input("\nError \n\t==> Ingrese una cantidad entre '1' y '99,000,000' >>> "))
        print(to_letter(num))
        input("Done! ")

if __name__ == '__main__':

    main()
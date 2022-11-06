import random

def ahorcado(intento):
    if intento == 6:
        print(""" 
                -------
                |      |
                |      o
                |     \ /            
                |      | 
               / \    / \ 
              /   \   
                
            0 Intentos faltantes _X_ _X_ _X_ _X_ _X_ _X_
                    😥 PERDISTE 😥""")

    elif intento == 5:
        print(""" 
                -------
                |      |
                |      o
                |     \ /  
                |      | 
               / \    /  
              /   \   
                
            1 Intento faltante _X_ _X_ _X_ _X_ _X_ __""")

    elif intento == 4:
        print(""" 
                -------
                |      |
                |      o
                |     \ / 
                |      | 
               / \      
              /   \   
                
            2 Intentos faltantes _X_ _X_ _X_ _X_ __ __""")

    elif intento == 3:
        print(""" 
                -------
                |      |
                |      o
                |     \ /
                |       
               / \      
              /   \   
                
            3 Intentos faltantes _X_ _X_ _X_ __ __ __""")

    elif intento == 2:
        print(""" 
                -------
                |      |
                |      o
                |     \ 
                |       
               / \      
              /   \   
                
            4 Intentos faltantes _X_ _X_ __ __ __ __""")

    elif intento == 1:
        print(""" 
                -------
                |      |
                |      o
                |      
                |       
               / \      
              /   \   
                
            5 Intentos faltantes _X_ __ __ __ __ __""")

def main():
    num_pc = random.randint(1,100)
    num_player = int(input('<-- ADIVINA EL NÚMERO -->\nIngresa un número entre 1 y 100: '))
    intento = 1

    while num_pc != num_player and intento<6:
        
        if num_player < num_pc:
            print('Ingresa un número MAYOR')
        else:
            print('Ingresa un número MENOR')
        ahorcado(intento)
        num_player = int(input('Ingresa un número: '))
        intento += 1
        
    if num_pc == num_player:
        print(f'Felicitaciones adivinaste el número, usaste {intento} intentos')
    elif intento==6:
        print(f'El número a adivinar era {num_pc}')

if __name__ == "__main__":
    main()

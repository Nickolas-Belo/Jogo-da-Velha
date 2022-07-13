
# coding: utf-8

# In[1]:


# JOGO DA VELHA
# matriz representando as posições na def velha()
V = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
jogando = 'X'


def velha():
    print("|----JOGO DA VELHA----|")
    print("|    +---+---+---+    |")
    print("|    | "+str(V[0][0])+" | "+str(V[0][1])+" | "+str(V[0][2])+" |    |")
    print("|    +---+---+---+    |")
    print("|    | "+str(V[1][0])+" | "+str(V[1][1])+" | "+str(V[1][2])+" |    |")
    print("|    +---+---+---+    |")
    print("|    | "+str(V[2][0])+" | "+str(V[2][1])+" | "+str(V[2][2])+" |    |")
    print("|    +---+---+---+    |")
    print("|---------------------|")

# nesse caso, o jogador sempre vai ser o X    
def jogador():
    return 'X'
    
# função com o input para o jogador colocar a posição   
def jogou(msg):
    while True:
        try:
            jogada = input(msg)
            return int(jogada[0])
        # checar se foi inserido entre 1 e 9, também vai dar a mesma mensagem se repetir a posição 
        except:
            print("O valor inserido não se encontra entre 1 e 9!")
      
 # empata o jogo se todas as posições na matriz se tornarem strings
def empate():
    for linha in range(3):
        for coluna in range(3):
            if str(V[linha][coluna]).isdigit():
                return False
    return True


Iniciar = True
while Iniciar:
    jogando = jogador()
    GameOn = True
    
    while GameOn:
        velha()
        jogada = jogou("Em qual posiçao deseja jogar? ")
        print()
        aceitar_jogada = False
        for linha in range(3):
            for coluna in range(3):
                if jogada == V[linha][coluna]:
                    V[linha][coluna] = jogando
                    aceitar_jogada = True
                    
        
        if aceitar_jogada:
            # detectar empate
            if empate():
                velha()
                print('Jogo empatado!')
                GameOn = False
                Iniciar = False
            # detectar vitória ou derrota
            # horizontal de cima
            elif (V[0][0] == 'X' and V[0][1] == 'X' and V[0][2] == 'X'):
                velha()
                print('Você ganhou o jogo!')         
                GameOn = False
                Iniciar = False
            elif (V[0][0] == 'O' and V[0][1] == 'O' and V[0][2] == 'O'):
                velha()
                print('Você perdeu o jogo!')          
                GameOn = False
                Iniciar = False
            # diagonal
            elif (V[0][0] == 'X' and V[1][1] == 'X' and V[2][2] == 'X'):
                velha()
                print('Você ganhou o jogo!')        
                GameOn = False
                Iniciar = False
            elif (V[0][0] == 'O' and V[1][1] == 'O' and V[2][2] == 'O'):
                velha()
                print('Você perdeu o jogo!')        
                GameOn = False
                Iniciar = False
            # diagonal
            elif (V[2][0] == 'X' and V[1][1] == 'X' and V[0][2] == 'X'):
                velha()
                print('Você ganhou o jogo!')       
                GameOn = False
                Iniciar = False
            elif (V[2][0] == 'O' and V[1][1] == 'O' and V[0][2] == 'O'):
                velha()
                print('Você perdeu o jogo!')           
                GameOn = False
                Iniciar = False
            # horizontal de baixo
            elif (V[2][0] == 'X' and V[2][1] == 'X' and V[2][2] == 'X'):
                velha()
                print('Você ganhou o jogo!')              
                GameOn = False
                Iniciar = False
            elif (V[2][0] == 'O' and V[2][1] == 'O' and V[2][2] == 'O'):
                velha()
                print('Você perdeu o jogo!')            
                GameOn = False
                Iniciar = False
            # horizontal do meio
            elif (V[1][0] == 'X' and V[1][1] == 'X' and V[1][2] == 'X'):
                velha()
                print('Você ganhou o jogo!')          
                GameOn = False
                Iniciar = False
            elif (V[1][0] == 'O' and V[1][1] == 'O' and V[1][2] == 'O'):
                velha()
                print('Você perdeu o jogo!')            
                GameOn = False
                Iniciar = False
            # vertical da esquerda
            elif (V[0][0] == 'X' and V[1][0] == 'X' and V[2][0] == 'X'):
                velha()
                print('Você ganhou o jogo!')           
                GameOn = False
                Iniciar = False
            elif (V[0][0] == 'O' and V[1][0] == 'O' and V[2][0] == 'O'):
                velha()
                print('Você perdeu o jogo!')          
                GameOn = False
                Iniciar = False
            # vertical do meio
            elif (V[0][1] == 'X' and V[1][1] == 'X' and V[2][1] == 'X'):
                velha()
                print('Você ganhou o jogo!')              
                GameOn = False
                Iniciar = False
            elif (V[0][1] == 'O' and V[1][1] == 'O' and V[2][1] == 'O'):
                velha()
                print('Você perdeu o jogo!')               
                GameOn = False
                Iniciar = False
            # vertical da direita
            elif (V[0][2] == 'X' and V[1][2] == 'X' and V[2][2] == 'X'):
                velha()
                print('Você ganhou o jogo!')
                GameOn = False
                Iniciar = False
            elif (V[0][2] == 'O' and V[1][2] == 'O' and V[2][2] == 'O'):
                velha()
                print('Você perdeu o jogo!')
                GameOn = False
                Iniciar = False
            # alternar entre o jogador X e o jogador O
            else:
                if jogando == 'O':
                    jogando = 'X'
                else:
                    jogando = 'O'
        else:
            print('Jogada inválida, insira um número entre 1 e 9!')     


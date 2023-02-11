import random 
# Este módulo implementa generadores de números pseudoaleatorios para varias distribuciones. 
# Para los enteros, existe una selección uniforme dentro de un rango

def play():
    user = input("Elegi : 'p' es para piedra, 'pp' es para papel, y 't' es para tijera")
    computer = random.choice(['p', 'pp', 't'])

    if user == computer:
        return 'Empate'
        
    # p > t, pp > p, t > pp

    if si_gana(user, computer):
        return 'Ganaste :D'
    
    return 'Perdiste ajajaja'

def si_gana(jugador, oponente):

    if (jugador == 'p' and oponente == 't') or (jugador == 't' and oponente == 'p')  or (jugador == 'pp' and oponente == 't'):
        return True 
    
    
print(play())

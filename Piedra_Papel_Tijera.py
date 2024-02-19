import random



def jugar():
    usuario = input("\nEscoge una opción: 'pi' para piedra, 'pa' para papel, 'ti' para tijera:  ").lower()
    
    computadora = random.choice(["pi", "pa", "ti"])
    
    
    if usuario == computadora:
        print("\nLa computadora eligio " +  computadora)
        return "\n¡Empate!\n"
    
    
    if quien_gano(usuario, computadora):
        print("\nLa computadora eligio " +  computadora)
        return "\n¡Ganaste!\n"
    
    
    print("\nLa computadora eligio " +  computadora)
    return "\n¡Perdiste!\n"






def quien_gano(jugador, oponente):
    
    # Retornar True si gana el jugador.
    # Piedra gana a Tijera (pi > ti).
    # Tijera gana a Papel (ti > pa).
    # Papel gana a Piedra (pa > pi).
    
    if ((jugador == "pi" and oponente == "ti") or (jugador == "ti" and oponente == "pa") or (jugador == "pa" and oponente == "pi")):
        return True
    else: 
        return False
    
    



print(jugar())






























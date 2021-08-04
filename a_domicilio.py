def algoritmo(THIRDQ, FORTHQ):
    opcion3 = input(THIRDQ)
    while opcion3 == "no":
        process1= input ('Pide prestado a tu mejor amigo, cuando tengas el dinero escribe "listo":  ')
        if process1 == "listo":
            opcion3 = "si"
    else:
        opcion4= input(FORTHQ)
        while opcion4 == "no":
            process2 = input ('Entonces identifica un lugar. Cuando estes listo escribe "listo":  ')
            if process2 == "listo":
                opcion4 = "si"
        else:
            process3 = input('Ordena tu plato favorito y espera a que llegue. Cuando llegue escribe "listo":  ')
            if process3 == "listo":
                print('Felicidades, ahora te puedes alimentar sanamente.')

def run():
    WELCOME= '''Bienvenido al algoritmo que te ayudará a decidir
    si debes o no pedir comida a domicilio a través de unas sencillas preguntas
    ¿Listo/a? Empecemos.
    
    ¿Tienes hambre? 
    : '''
    SECONDQ= '''¿Tienes comida en casa?
    : '''
    SECONDQ2= '''¿Tienes ganas de cocinar?
    : '''
    THIRDQ= '''¿Tienes dinero?
    : '''
    FORTHQ= '''¿Sabes a donde puedes ordenar comida a domicilio?
    : '''
    
    opcion1= input(WELCOME)

    if opcion1 == "si":
        opcion2 = input(SECONDQ)
        if opcion2 == "no":
            algoritmo(THIRDQ, FORTHQ)
        else:
            opcion2_1= input(SECONDQ2)
            if opcion2_1 == "si":
                print ('Felicidades, no morirás de hambre. Cocina y alimentate.')
            else:
                algoritmo(THIRDQ, FORTHQ)
    else:
        print('Felicidades, no estas muriendo de hambre')





if __name__ == '__main__':
    run()

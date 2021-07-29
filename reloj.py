#Algoritmo en código para  representar el funcionamiento de un reloj.
def run ():
    hr = 0
    min = 0
    sec = 0

    while hr < 24:
        print ('Hora local: '+str(hr)+':'+str(min)+':'+str(sec))
        if min == 59 and sec == 59:
            hr = hr + 1
            min = 0
        elif sec == 59:
            min = min + 1
            sec = 0
        else:
            sec = sec + 1
    
if __name__ == '__main__':
    run()
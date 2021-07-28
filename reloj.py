def reloj (seg):
    while seg < 60:
        print (seg)
        seg = seg + 1
    return seg

def run ():
    seg = 0
    print (reloj (seg))


if __name__ == '__main__':
    run()
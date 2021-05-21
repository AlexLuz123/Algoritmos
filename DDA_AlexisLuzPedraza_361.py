import matplotlib.pyplot as plt

def algoritmoDDA(x1, y1, x2, y2):
    x = -1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    if dx > dy:
        steps = dx
    else:
        steps = dy

    xinc = dx / steps
    yinc = dy / steps

    for i in range(x, steps):
        plt.plot(round(x1), round(y1), marker=".", color="blue")
        print(x1,",",y1)
        x1 = x1 + xinc
        y1 = y1 + yinc
        
    plt.show()

if __name__ == '__main__':

    x1 = int(input("Ingresa el valor para x1: "))
    y1 = int(input("Ingresa el valor para y1: "))
    x2 = int(input("Ingresa el valor para x2: "))
    y2 = int(input("Ingresa el valor para y2: "))
    algoritmoDDA(x1, y1, x2, y2)
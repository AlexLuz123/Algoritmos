import matplotlib.pyplot as plt

def algoritmoBresenhams(x1, y1, x2, y2):
    x = x1
    y = y1
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = (2 * dy) - dx
    x2 = x2 + 1

    for i in range(x, x2):
        plt.plot(round(x), round(y), marker=".", color="blue")
        print(x,",",y)
        x = x + 1
        if p < 0:
            p = p + (2 * dy)
        else:
            p = p + (2 * dy) - (2 * dx)
            y = y + 1
        
    plt.show()    

if __name__ == '__main__':

    x1 = int(input("Ingresa el valor para x1: "))
    y1 = int(input("Ingresa el valor para y1: "))
    x2 = int(input("Ingresa el valor para x2: "))
    y2 = int(input("Ingresa el valor para y2: "))
    algoritmoBresenhams(x1, y1, x2, y2)
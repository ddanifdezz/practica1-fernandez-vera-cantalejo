def check_triangle(a, b, c):
    if (c < a + b) and (b < a + c) and (a < c + b):
        if a == b and a == c:
            result = "Triangulo equilatero"
            print("Triangulo equilatero \n")
        elif a == b or b == c:
            result = "Triangulo isosceles"
            print("Triangulo isosceles \n")
        else:
            result = "Triangulo escaleno"
            print("Triangulo escaleno \n")
    else:
        result = "No es un triangulo"
        print("No es un triangulo")
        
    return result


def main():
    n = int(input("Numero de casos de prueba:\n"))
    print(n)
    
    for i in range(1, n + 1):
        print("Marcar los valores de longitud de los lados del triangulo (uno por linea):")
        
        a = int(input())
        print(f"{a},", end="")
        
        b = int(input())
        print(f"{b},", end="")
        
        c = int(input())
        print(f"{c}:")
        
        check_triangle(a, b, c)


if __name__ == "__main__":
    main()
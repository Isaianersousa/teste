while True:  


    op = input("Digite a operação desejada:(+,-,*,/)")
    num1 = int(input("digite um número:"))
    num2 = int(input("digite o segundo numero"))

    
    

    if op == "+":
        print("o resultado é",(num1+num2))
    elif op == "-":
        print("O resultado é", (num1-num2))
    elif op== "*":
        print("o resultado é", (num1*num2))
    elif op=="/":
        print("o resultado é", (num1/num2))
idade = int(input("digite sua idade"))

if idade >= 0 and idade < 10:
    print ("você é uma criança")
elif idade >= 10 and idade < 18:
    print ("você é adolescente")
elif idade >= 18 and idade < 60: 
    print ("vc é adulto")    
else:
    print ("vc é um idoso")
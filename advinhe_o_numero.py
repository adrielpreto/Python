# -*- coding: UTF-8 -*-
import os,random #biblioteca de comandos do SO e randômica
os.system("clear") #limpa tela
var1 = random.randint(0,100) #atribui número randômico na var1
n = 0 #zera contador
print("Adivinhe o número entre 0 e 100:")
var2 = 1000 #força um número diferente à var2
while var2 != var1: #enlace enquanto condição não satisfeita 
    n = n + 1 #incrementa contador de tentativas
    var2 = int(input("digite um número: ")) #força var2 ser inteiro
    os.system("clear")
    if var2 > var1:
        print(var2,"foi muito")
    if var2 < var1:
        print(var2,"foi pouco")
    if var2 == var1:
        print("ACERTOU!!! em",n,"tentativas")
input()
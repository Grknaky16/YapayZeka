# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 03:14:03 2022

@author: Gürkan
"""
def Soru1():
    sayi=int(input("Lütfen Bir sayı giriniz: "))
    for x in range(10):
        x=x+1
        print(x*sayi)
        
def Soru2():
    sayi=int(input("Lütfen bir sayı giriniz: "))
    basamak=0
    while(sayi>0):
        basamak+=1
        sayi//=10
    print("Basamak sayısı:  ",basamak)
    
def Soru2v1():
    sayi=str(input("Lütfen bir sayı giriniz: "))
    basamak=len(sayi)
    print("Basamak sayısı: ",basamak)
    
def Soru3():
    sayisalDegerler=[12,15,32,42,55,75,122,132,150,180,200]
    print("For için:")
    for i in sayisalDegerler:
        if(i<=150):
            if(i%5==0):
                print(i)
    print("\nWhile için:")
    i=0
    while(i<len(sayisalDegerler)):
        sayi=sayisalDegerler[i]
        i+=1
        if(sayi<=150):
            if(sayi%5==0):
                print(sayi)
            
def Soru4():
    a=int(input("a sayısı için bir değer giriniz: "))
    b=int(input("b sayısı için bir değer giriniz: "))
    c=int(input("c sayısı için bir değer giriniz: "))
    sayac=0
    for i in range(a,b+1):
        if(i%c==0):
            sayac+=1
    print(sayac)
            
def Soru5():
    for i in range(1,100):
        print(str(i)+"-"+str(100-i))
        
def Soru6():
    ip=input("Lütfen IP adresini giriniz: ")
    ip=list(map(int,ip.split(" ")))
    if(len(ip)<4):
        print("Hatalı giriş yaptınız..")
    else:
        i=0
        while(i<5):
            x=3
            while(x>=0):
                tutucu=ip[x]
                if(tutucu==255):
                    ip[x]=0
                    x-=1
                else:
                    ip[x]+=1
                    break
            i+=1
            print(' '.join(map(str, ip)))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
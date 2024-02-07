#lõin kalkulaatori klassi
class Kalkulaator:
#sisestasin liitmis funktsiooni
    def liida(self, a, b):
        return a + b
#lahutamis funktsioon
    def lahuta(self, a, b):
        return a - b
#korrutamis funktsioon
    def korruta(self, a, b):
        return a * b
#jagamis funktsioon
    def jaga(self, a, b):
#kui b on 0 siis väljastab et ei saa nulliga jagada
        if b != 0:  
            return a / b
        else:
            return "Ei saa nulliga jagada"  
#jäägi arvutamine
    def jaak(self, a, b):
        return a % b
#ruutjuure arvutamine
    def ruutjuur(self, a, b):  
        return a ** (1/b)  
#protsendi arvutamine
    def protsent(self, a, b):  
        return (a / b) * 100  

#küsib esimest numbrit
a = int(input("Sisesta esimene number: "))
b = int(input("Sisesta teine number: "))

#lühend
kalk = Kalkulaator()

#kalkuleerib vastuseid
print("Liitmine:", kalk.liida(a, b))
print("Lahutamine:", kalk.lahuta(a, b))
print("Korrutamine:", kalk.korruta(a, b))
print("Jagamine:", kalk.jaga(a, b))
print("Jääk:", kalk.jaak(a, b))
print("Ruutjuur esimesest numbrist teise astmes:", kalk.ruutjuur(a, b))
print("Protsent:", kalk.protsent(a, b))

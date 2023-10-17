Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     P=int(input("Deliveries:"))#The user will input the amount of deliveries
...     C=int(input("Collisions:"))#The user will input the amount of collisions
...     Gained=P*50 #Gain 50 points for every successful delivery
...     Lost=C*10 #Lose 10 points for every collision
...     F=Gained-Lost #F stands for final score
...     print(F)#Printing final score
... 
...     
>>> main()
Deliveries: 6
Collisions: 5
250

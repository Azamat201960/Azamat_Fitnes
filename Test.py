from colorama import Fore, Back, Style
from colorama import init
init()

print( Fore.BLACK )

print( Back.RED )

print("Azamat Fitnes")
print("by Azamat Nuraev")

print( Back.GREEN )

name1= float( input("рост в метрах :"))
name2= float( input("вес :") )

print(Back.YELLOW)
7

c = name1 * name1

d = name2 / c

print(d)

if d < float(20):
	print("Увеличить мышечноют массу")

elif d < float(25):
	print("норма")

elif d > float(25):
	print("Вам не обходимо снизить вес")


input()
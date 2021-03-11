# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:49:26 2021

9 - dars

@author: user
"""

ismlar = ['Sulton', 'Sobir', 'Sadoqat', 'Sojida', 'Saodat']
x = len(ismlar)
for marta in ismlar:
    print('Salom', marta)
print(f'kod {x} marta takrorlandi')

toq_sonlar = list(range(11,24,2))

for t_s_kublari in toq_sonlar:
    print(t_s_kublari**3)
    
# kinolar = []
# print("6 ta eng sevimli kinoyingizni kiriting! ")
# for kino in range(6):
#     kinolar.append(input(f"{kino+1}-kinoning nomini kiriting: \n"))
# print(kinolar)


n = int(input("bugun kimlar bilan suxbatlashdingiz?"))

bugun = []
for odam in range(n):
    bugun.append(input(f"{odam+1}-odamning  ismi:   "))
print(bugun)









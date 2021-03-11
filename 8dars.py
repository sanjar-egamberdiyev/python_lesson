# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:36:10 2021
8 - dars

@author: user
"""
countries = ['uzbekistan', 'armenia', 'croatia', 'united kingdom', 'russian', 'india']
print(countries)

uzunlik = len(countries)

print(sorted(countries))

print(sorted(countries, reverse=True))

print(countries)

countries.reverse()
print(countries)

countries.sort()
countries.reverse()

juft_sonlar = list(range(120,1200,2))

print(juft_sonlar)

print(sum(juft_sonlar))
print(max(juft_sonlar)-min(juft_sonlar))

print(len(juft_sonlar))


print(juft_sonlar[:21])


taomlar = []

taomlar.append('manti')
taomlar.append('shurva')
taomlar.append('tandir')
taomlar.append('palov')
taomlar.append('tuxum qovirma')

nonushta = taomlar[:]

taomlar.append('lag"mon')

nonushta = tuple(nonushta)
# nonushta.append('apple')


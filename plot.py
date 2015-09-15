#! /usr/bin/python2.7
# encoding=utf-8
#
# Authored by Juan Mite
#
from pylab import *
print('Generando gráfica..')
f = open('log.txt', 'r')
LRU = []
OPTIMO = []
CLOCK = []
LRU_caches = []
OPTIMO_caches = []
CLOCK_caches = []
LRUcont = 0
OPTIMOcont = 0
CLOCKcont = 0

for line in f:
	sl = line.split(',')
	if sl[2].startswith('LRU'):
		LRU.append(sl[1])
		LRU_caches.append(sl[0])
		LRUcont = LRUcont + 1
	elif sl[2].startswith('OPTIMO'):
		OPTIMO.append(sl[1])
		OPTIMO_caches.append(sl[0])
		OPTIMOcont = OPTIMOcont + 1
	else:
		CLOCK.append(sl[1])
		CLOCK_caches.append(sl[0])
		CLOCKcont = CLOCKcont + 1

Xsize = min(LRUcont, OPTIMOcont, CLOCKcont)
plot ( LRU_caches,LRU,'.-',label='LRU' )
plot ( OPTIMO_caches,OPTIMO,'o-',label='OPTIMO' )
plot ( CLOCK_caches,CLOCK,'*-',label='CLOCK' )
xlabel('Cache size')
ylabel('Misses')
title('Misses vs Cache size')
legend(('LRU','OPTIMO', 'CLOCK'))
savefig("graph.png",dpi=(640/8))
print('¡Completado!')

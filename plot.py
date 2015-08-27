#! /usr/bin/python2.7
# encoding=ASCII

from pylab import *
print('Generando histograma...')
f = open('log.txt', 'r')
LRU = []
OPTIMO = []
CLOCK = []
LRUcont = 0
OPTIMOcont = 0
CLOCKcont = 0

for line in f:
	sl = line.split(',')
	if sl[2].startswith('LRU'):
		LRU.append(sl[1])
		LRUcont = LRUcont + 1
	elif sl[2].startswith('OPTIMO'):
		OPTIMO.append(sl[1])
		OPTIMOcont = OPTIMOcont + 1
	else:
		CLOCK.append(sl[1])
		CLOCKcont = CLOCKcont + 1

Xsize = min(LRUcont, OPTIMOcont, CLOCKcont)

plot ( arange(0,Xsize),LRU[:Xsize],'.-',label='LRU' )
plot ( arange(0,Xsize),OPTIMO[:Xsize],'o-',label='OPTIMO' )
plot ( arange(0,Xsize),CLOCK[:Xsize],'*-',label='CLOCK' )
xlabel('Cache size')
ylabel('Miss rate')
title('Miss rate vs Cache size')
legend(('LRU','OPTIMO', 'CLOCK'))
savefig("graph.png",dpi=(640/8))
print('Completado!')
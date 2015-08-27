#! /usr/bin/python2.7
# encoding=utf8
import sys

workload_file = sys.argv[1]
policy = sys.argv[2]
cache_tam = int(sys.argv[3])
cache = []
misses = 0
hites = 0

if policy.upper() == 'LRU':
    print 'Evaluando una caché LRU con '+ str(cache_tam) +' entradas...'
    with open(workload_file) as f:
        for line in f:
            if (cache.__contains__(line)):
                # HIT
                cache.remove(line)
                cache.append(line)
                hites = hites +1
                #print(line, 'hit', cache)
            else:
                # MISS
                misses = misses + 1
                cache.append(line)
                if len(cache) > cache_tam :
                    cache.remove(cache[0])
                #print(line, 'miss', cache)
    print('Resultados: ')
    print ('\tMiss rate: ', '\t('+str(misses)+' misses out of '+' -- '+' references)')
    print ('\tMiss rate (warm cache): ', '\t('+str(hites)+' misses out of '+'--cache_tam--' +' references)')

    
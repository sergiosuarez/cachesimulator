#! /usr/bin/python2.7
# encoding=utf8
import sys
from collections import OrderedDict

workload_file = sys.argv[1]
policy = sys.argv[2]
cache_tam = int(sys.argv[3])
cache = OrderedDict()
misses = 0
hites = 0
references = 0

if policy.upper() == 'LRU':
    print 'Evaluando una caché LRU con '+ str(cache_tam) +' entradas...'
    with open(workload_file) as f:
        for line in f:
            if (cache.__contains__(line)):
                # HIT
                cache.__delitem__(line)
                cache[line] = ''
                hites = hites + 1
            else:
                # MISS
                misses = misses + 1
                cache[line] = ''
                if len(cache) > cache_tam :
                    cache.popitem(last=False)
    references = hites + misses
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(misses)/(references)),3))+'% ('+str(misses)+' misses out of '+str(references)+' references)'
    print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(references-cache_tam)),3))+'% ('+str(hites)+' misses out of '+ str(references-cache_tam)+' references)'
    print 'Efficiency: '+str(round(float(hites)/(references),3))
    with open("log.txt", "a") as myfile:
        myfile.write(str(cache_tam)+','+str(misses)+',LRU\n')

elif policy.upper() == 'FIFO':
    print 'Evaluando una caché FIFO con '+ str(cache_tam) +' entradas...'
    with open(workload_file)as f:
        for line in f:
            if (cache.__contains__(line)):
                # HIT
                hites = hites + 1
            else:
                # MISS
                misses = misses + 1
                cache[line] = ''
                if len(cache) > cache_tam :
                    cache.popitem(last=False)
    references = hites + misses
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(misses)/(references)),3))+'% ('+str(misses)+' misses out of '+str(references)+' references)'
    print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(references-cache_tam)),3))+'% ('+str(hites)+' misses out of '+ str(references-cache_tam)+' references)'
    print 'Efficiency: '+str(round(float(hites)/(references),3))

elif policy.upper() == 'OPTIMO':
    print 'Evaluando una caché OPTIMO con '+ str(cache_tam) +' entradas...'
    with open(workload_file)as f:
        for line in f:
            if (cache.__contains__(line)):
                # HIT
                hites = hites + 1
            else:
                # MISS
                misses = misses + 1
                cache[line] = ''
                if len(cache) > cache_tam :
                    cache.popitem(last=False)
    references = hites + misses
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(misses)/(references)),3))+'% ('+str(misses)+' misses out of '+str(references)+' references)'
    print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(references-cache_tam)),3))+'% ('+str(hites)+' misses out of '+ str(references-cache_tam)+' references)'
    print 'Efficiency: '+str(round(float(hites)/(references),3))

elif policy.upper() == 'CLOCK':
    print 'Evaluando una caché CLOCK con '+ str(cache_tam) +' entradas...'
    with open(workload_file)as f:

        i=0
        referenced =[]
        for line in f:
            if (cache.__contains__(line)):
                # HIT
                hites = hites + 1
                referenced.append(True)
            else:
                    # MISS
                   misses = misses + 1
                   cache[line] = ''
                   if len(cache) > cache_tam :
                       cache.popitem(last=False)
        #print hites
        clock=0

        for element in referenced:
            if element==True:
                #referenced[clock].append(False);
                misses = misses + 1
                clock = (clock + 1) % cache_tam; #for clarity

        #replace the object at the current clock position and increment clock
        #f[clock] = obj;
        #referenced[clock].append(True);
        #clock = (clock + 1) % f.length; #for clarity

        #misses = misses + 1
        #cache[line] = ''
        #if len(cache) > cache_tam :
        #    cache.popitem(last=False)
    references = hites + misses
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(misses)/(references)),3))+'% ('+str(misses)+' misses out of '+str(references)+' references)'
    print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(references-cache_tam)),3))+'% ('+str(hites)+' misses out of '+ str(references-cache_tam)+' references)'
    print 'Efficiency: '+str(round(float(hites)/(references),3))


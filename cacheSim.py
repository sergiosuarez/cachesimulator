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

class Page:
    def __init__(self, page ,reference_bit, time_of_last_use):
        self.p = page
        self.r = reference_bit
        self.t = time_of_last_use

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
                # MISS misses = misses + 1 cache[line] = ''
                if len(cache) > cache_tam:
                    cache.popitem(last=False)
    references = hites + misses
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(misses)/(references)),3))+'% ('+str(misses)+' misses out of '+str(references)+' references)'
    print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(references-cache_tam)),3))+'% ('+str(hites)+' misses out of '+ str(references-cache_tam)+' references)'
    print 'Efficiency: '+str(round(float(hites)/(references),3))

elif policy.upper() == 'CLOCK':
    print 'Evaluando una caché CLOCK con '+ str(cache_tam) +' entradas...'
    pages_in_memory = cache_tam    # Number of pages in physical memory.
    tau = 5                # Used to determine if a page should be replaced or not.
    clock = 0              # Time of last use
    wsclock_page_fault = 0 # Amount of page faults.
    wsclock_list = []      # List
    wsclock_page_hits = 0
    with open(workload_file)as f:
        i=0
        referenced =[]
        for line in f:
            clock =  clock + 1
            if (len(wsclock_list)<pages_in_memory):
                #print(len(wsclock_list))
                found = False
                for page_in_memory in wsclock_list:
                    if page_in_memory.p == line:
                        wsclock_page_hits = wsclock_page_hits +1
                        found = True
                if not(found):
                    wsclock_page = Page(line, 1, clock)
                    wsclock_list.append(wsclock_page)
                    wsclock_page_fault+=1 
            #else:
             #   found = False
              #  inserted = False
               # for page_in_memory in wsclock_list:
         #           if page_in_memory.t == clock:
          #              wsclock_page_hits = wsclock_page_hits +1
           #             found = True
            #    if not(found):
             #       for page_in_memory in wsclock_list:
              #          if page_in_memory.r == 1:
               #             page_in_memory.r = 0
                #        if page_in_memory.r == 0:
                 #           age = clock - page_in_memory.t
                  #          if age > tau:
                   #             page_in_memory.p = line
                    #            page_in_memory.r = 1
                     #           page_in_memory.t = clock
                      #          wsclock_page_fault  = 1 + wsclock_page_fault
                       #         inserted = True
                        #        break
                         #   if age == tau and not(inserted):
                          #      page_in_memory.p = line
                           #     page_in_memory.r = 1
                            #    page_in_memory.t = clock
                             #   wsclock_page_fault  = 1 + wsclock_page_fault

        #replace the object at the current clock position and increment clock
        #f[clock] = obj;
        #referenced[clock].append(True);
        #clock = (clock + 1) % f.length; #for clarity
    hites=wsclock_page_hits
    misses=wsclock_page_fault

    references = hites + misses
        #misses = misses + 1
        #cache[line] = ''
        #if len(cache) > cache_tam :
        #    cache.popitem(last=False)
    references = wsclock_page_hits + wsclock_page_fault
    print "Resultados: "
    print "Miss rate: ", '              '+str(round((float(misses)/(references)),3))+'% ('+str(misses)+' misses out of '+str(references)+' references)'
    print 'Miss rate (warm cache): ', ' '+str(round((float(misses)/(references-cache_tam)),3))+'% ('+str(hites)+' misses out of '+ str(references-cache_tam)+' references)'
    print 'Efficiency: '+str(round(float(hites)/(references),3))


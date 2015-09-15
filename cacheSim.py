#! /usr/bin/python2.7
# encoding=utf8
import sys
from collections import OrderedDict
import sys
import time
from sys import argv 

workload_file = sys.argv[1]
policy = sys.argv[2]
cache_tam = int(sys.argv[3])
cache = OrderedDict()
misses = 0
hites = 0
references = 0

input_file = sys.argv[1]
N = int(sys.argv[3])


class Page:
    def __init__(self, page ,reference_bit, time_of_last_use):
        self.p = page
        self.r = reference_bit
        self.t = time_of_last_use
# Optimal Page Replacement Algorithm.
def Optimal(pages,N):
    pages = pages.rstrip('\n')
    #pages = pages.split() # List of pages that is going to be inserted into memory.
    pages_in_memory = N   # Lenght of the physical memory.
    op_list = []          # List containing the pages in physical memory.
    op_dict = {} # Dictionary containing the time when the page will appear again in the list of arguments and the page itself.
    compare = 0  # Used to store the time when the page will appear again in the list of arguments.
    op_page_fault = 0
    op_page_hit = 0 # Amount of page faults.
    # Insertion of pages to memory and calculation of page faults.
    for i in range(len(pages)):
        page = pages[i] # Page in virtual memory.
        # Insert the first pages to physical memory.
        if len(op_list) < pages_in_memory: 
            page_in_list = Page_Check(op_list, page, len(op_list)) 
            if not(page_in_list):
                op_list.append(page)
                op_page_fault += 1 # Page Fault.
            else:
                op_page_hit+=1
        # Insert the remaining pages to memory.
        else:
            # Verify if the page to be inserted is not already in list.
            page_in_list = Page_Check(op_list, page, pages_in_memory) 
            if not(page_in_list):
                lock_page = 0 # Used to mark the page that will be removed from the list.
                # For loop that verifies which page will be removed from the list and 
                # which one will be inserted. 
                for j in range(pages_in_memory):
                    compare = Compare(op_list[j],pages,i) # Returns the number of time when the page in list will be inserted again.
                    # Determine which page is the farthest or is not in the list.
                    if (compare > lock_page):
                        lock_page = compare
                    else:
                        continue
                    op_dict[lock_page] = op_list[j] # Fill the dictionary with the time when the page will appear again.
                    page_to_be_removed = op_dict.get(lock_page) # Page that will be removed from physical memory.
                # Remove page from memory and increment page fault count.
                for k in range(pages_in_memory):
                    if op_list[k] == page_to_be_removed:
                        op_list[k] = page
                        op_page_fault += 1 # Page Fault.
                        break
                    else:
                        op_page_hit+=1
    hites=op_page_hit
    misses=op_page_fault
    return op_page_fault

"""Functions used by the main algorithms"""

# Function that checks if the page being inserted is already in the list.
# Used in Optimal and Second Chance Page Repalacement Algorithms
def Page_Check(plist, page, pages):
    for i in range(pages):
        page_in_list = plist[i]
        if page_in_list == page:
            return True
    return False

# Function that determines the page that is the least likely to be called again. 
# Used in the Optimal Page Replacement Algorithm
def Compare(page_in_list,pages,counter):
    len_of_remaining_page = (len(pages)) - counter # Number of pages that need to be compared.
    remaining_pages = counter-1 # Number of pages that are used to determine the index of a page in list.
    # For loop that verifies which page is less likely to be inserted again.
    for i in range(1,len_of_remaining_page+1):
        index = i + remaining_pages
        page = pages[index] 
        # If page in list is the same as the page that is going to be inserted, return i.
        if page_in_list == page:
            return i
        # If we reached the end of the length of the arguments, return i.
        if (i == len_of_remaining_page):
            return i


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
    """Call to functions and printing of the amount of page faults generated
    by each  algorithm"""
    inicio = time.time()
    with open(input_file) as f:
    #f = open(input_file,r)
    #pages = f.read()
            for pages in f:
                pages = pages.rstrip('\n')
                #print pages
                op_page_faults = Optimal(pages,N)


    #op_page_faults = Optimal(pages,600000)

    print'Optimal Page Replacement Algorithm Page Faults: ' + str(op_page_faults) 
    fin = time.time()
    total = fin - inicio
    print "time:"
    print total*1000

    misses=op_page_faults
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


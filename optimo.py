# --coding: utf-8 --
#!/usr/bin/env python
import sys
import time


from sys import argv # Library used for the inline parameter in this program.

# Read pages from file.
input_file = argv[1]
N = argv[2]
# Optimal Page Replacement Algorithm.
def Optimal(pages,N):
	pages = pages.rstrip('\n')
	#pages = pages.split() # List of pages that is going to be inserted into memory.
	pages_in_memory = N   # Lenght of the physical memory.
	op_list = [] 		  # List containing the pages in physical memory.
	op_dict = {} # Dictionary containing the time when the page will appear again in the list of arguments and the page itself.
	compare = 0  # Used to store the time when the page will appear again in the list of arguments.
	op_page_fault = 0 # Amount of page faults.
	# Insertion of pages to memory and calculation of page faults.
	for i in range(len(pages)):
		page = pages[i]	# Page in virtual memory.
		# Insert the first pages to physical memory.
		if len(op_list) < pages_in_memory: 
			page_in_list = Page_Check(op_list, page, len(op_list)) 
			if not(page_in_list):
				op_list.append(page)
				op_page_fault += 1 # Page Fault.
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


#! /usr/bin/python
import sys
workload = open(sys.argv[1], 'r')
print (workload.read(10), sys.argv[2], sys.argv[3])

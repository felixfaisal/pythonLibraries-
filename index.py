import os
import logging
import subprocess
#import logger

# subprocess is better alternative of OS commands
filepath = 'HelloWorld.c'
proc = subprocess.Popen(['gcc', filepath],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc = subprocess.Popen(['./a.out'],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
#logger.info('Ran ngSpice command')
#print("Ran NGSpice command")
print(stdout)
filepath = 'HelloWorld.cpp'
proc = subprocess.Popen(['g++', filepath],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
proc = subprocess.Popen(['./a.out'],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
#logger.info('Ran ngSpice command')
#print("Ran NGSpice command")
print(stdout)
filepath = 'HelloWorld.js'
proc = subprocess.Popen(['node', filepath],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# proc = subprocess.Popen(['./a.out'],
# stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = proc.communicate()
#logger.info('Ran ngSpice command')
#print("Ran NGSpice command")
print(stdout)

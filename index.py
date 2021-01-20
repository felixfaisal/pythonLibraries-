import os
import logging
import subprocess
#import logger

# subprocess is better alternative of OS commands


def C_obtainOutput(filepath):
    proc = subprocess.Popen(['gcc', filepath],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc = subprocess.Popen(['./a.out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return stdout


def Cpp_obtainOutput(filepath):
    proc = subprocess.Popen(['g++', filepath],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc = subprocess.Popen(['./a.out'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    # print(stdout)
    return stdout


def js_obtainOutput(filepath):
    proc = subprocess.Popen(['node', filepath],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    print(stdout)


print(Cpp_obtainOutput('HelloWorld.cpp').decode())

def check_outputC(filepath,test):
    output = C_obtainOutput(filepath).decode()
    if output==test:
        print("Test Completed Succesfully")
    else:
        print("Test Failed")
    
check_outputC('HelloWorld.c','Hello World')

##+LHDR###########################################################################################
##
##  File Name            :  M32ValCodeChecker.py
##  Author               :  Vaskar Paul
##  Creation Date        :  30/04/2015
##  Description          :  M32ValCodeChecker tool checks whether coding standard has been followed
##                          while library or test code development as mentioned in
##                          "http://confluence:8080/display/HPMDVAL/Coding+Standards"
##                          
###################################################################################################
## Copyright (c) Microchip Technology, Inc.
## This file is the confidential and proprietary property of Microchip Technology, Inc. and the
## possession or use of this file requires a written license from Microchip Technology, Inc.
##-LHDR############################################################################################

import sys

def search_func(lst, x):
    if not lst:    # shorter way to test if the list is empty
        return "failure"
    for e in lst:  # look how easy is to traverse the list!
        if e == x: # we no longer care about indexes
            return "success"
    else:
        return "failure" 

def TraverseFile(filename = '', str = '') :
    error = 0
    with open(filename) as openfile:    
        for num, line in enumerate( openfile, 1 ):
            for part in line.split():
                if str in part:
                    print num, ':' ,part
                    #print part
                    error = 1

    return error

def Rule38(filename = ''):
    """
    Macros and functions used within a library only, not user visible,
    are to be precede by 2 underscores. Any macro to be used by the
    user should have no preceding underscore.
    """
    str = "__"
    error = TraverseFile(filename, str)

    if error == 1:
        print "Rule38 violation: Private Library functions with double underscore accessed in TestLib or Func layer"

    return                    

def main():
    #f = open('C:\Users\i15929\TestSuites\Common\Libs\SDHC\DUT\Sdhc_LibInc.h', 'r')
    #print f.read()
    #f.read()
    
    #with open("C:\Users\i15929\TestSuites\Common\Libs\SDHC\DUT\Sdhc_LibInc.h") as openfile:
    #with open(filename) as openfile:    
    #    for line in openfile:
    #        for part in line.split():
    #            if "_" in part:
    #                print part

    filename = sys.argv[-1]
    Rule38(filename)
    
if __name__ == "__main__":
    main()

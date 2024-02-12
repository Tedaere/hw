#!/usr/bin/env python3


import argparse
import numpy as np
import matplotlib.pyplot as plt
#
parser = argparse.ArgumentParser()
parser.add_argument('input',  metavar='FILENAME', type=str)

def decoder(a):
    res = []
    for i in range(len(a) // 8):
        char = 0
        for j in range(8):
            char = (char << 1) | a[i*8+j]
        res.append(chr(char))
    return ''.join(res)

if __name__ == "__main__":
    args = parser.parse_args()
    f = open(args.input, 'r')
    
    ONE = [1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1]
    ZERO = [-1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1]
    
    i = 0
    j = 0
    a = []
    seq = []
    res_zero = 0
    res_one = 0
    
    ASCII = []
        
    for l in f:
        j += 1
        a.append(float(l))
            
        if (j == 11):
            j = 0
            seq += a
            a = []
            i += 1
            
        if (i == 5):
            conv_zero = np.correlate(seq, np.repeat(ZERO, 5), mode='full')
            conv_zero = conv_zero - conv_zero.mean()
            std_zero = np.std(conv_zero)
            level_zero = 2*std_zero
            
            conv_one = np.correlate(seq, np.repeat(ONE, 5), mode='full')
            conv_one = conv_one - conv_one.mean()
            std_one = np.std(conv_one)
            level_one = 2*std_one
            
            if (max(conv_zero) >= max(conv_one) 
            and max(conv_zero) >= level_zero 
            and min(conv_zero) >= -level_zero):
                ASCII.append(0)
            else:
                ASCII.append(1)
            
            res_zero = 0
            res_one = 0
            i = 0
            seq = []
    
    f.close
    
    f = open("wifi.json", 'w')
    f.write("{\"message\":\""+decoder(ASCII)+"\"}")
    f.close
            

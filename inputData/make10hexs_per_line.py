# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:37:18 2019

@author: SKY_SHY
"""


def make8(a_hex):
    while len(a_hex)<8:
        a_hex = '0' + a_hex
    return a_hex
      
        
def testFileHEX(path, oath_out_file):
    
    file = open(path, 'r').read().split()
    out_file = open(oath_out_file, 'a')
    s = 0
    R = len(file)//10
    for i in range(R):
        row = file[s:s+10]
        for item in row:
            out_file.write(make8(hex(int(item))[2:]))
        out_file.write('\n')
        s +=10

def main(inpPath, outPath):
	testFileHEX(inpPath, outPath)
	
if __name__ == '__main__':
	main(inpPath, outPath)


'''testFileHEX('A:/Pi_num__idea2_32Fullbits.txt', 'A:/Pi_id2.ascii')'''


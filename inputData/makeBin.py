# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:37:18 2020

@author: SKY_SHY
"""


import subprocess
import os
from diehard.settings import BASE_DIR

def main(inpPath, outPath):
	init_path = os.path.join(BASE_DIR, 'inputData')
	os.chdir(init_path)
	p = subprocess.Popen(['ASC2BIN.EXE'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text = True)
	p.communicate(input='\n\n\n' + inpPath + '\n' + outPath)
	

if "__name__" == "__main__":
	main(inpPath, outPath)
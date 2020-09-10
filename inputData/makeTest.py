# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 17:37:18 2020

@author: SKY_SHY
"""


import subprocess
import os
import shutil
from diehard.settings import BASE_DIR

def deleteFile():
	os.remove('bin')
	os.remove('hex.ascii')

def moveFile(ID):
	inp_path = os.path.join(BASE_DIR, 'inputData\\t.txt')
	out_path = os.path.join(BASE_DIR, 'uploads\\' + str(ID))
	shutil.move(inp_path, out_path)
	deleteFile()



def main(inpPath, outPath):
	init_path = os.path.join(BASE_DIR, 'inputData')
	os.chdir(init_path)
	p = subprocess.Popen(['DIEHARD.EXE'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text = True)
	p.communicate(input= inpPath + '\n' + outPath + '\n' + '111111111111111')
	
	'''arg = "/results/DIEHARD.exe && " + impPath + " && " + outPath + " && " + "111111111111111"
	args = [arg]
	p = subprocess.Popen(args, shell=True)'''


if "__name__" == "__main__":
	main(inpPath, outPath)
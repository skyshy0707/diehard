import os
from diehard.settings import BASE_DIR
import shutil

def main(ID, fileName):
	'''os.getcwd()'''
	path = os.path.join(BASE_DIR, 'uploads\\' + str(ID))
	os.makedirs(path)
	ipath = os.path.join(BASE_DIR, fileName)
	shutil.move(ipath, path)

if "__name__" == "__main__":
	main(ID, fileName)
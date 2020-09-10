# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:58:42 2020

@author: SKY_SHY
"""

'''output = "A:/pi4_2909.txt"'''

'''output = open(output, 'r')'''


'''d = output.readlines()'''


class Tests():

	def __init__(self,):

		self.Test_P = {}

		self.keys_p = {"p-value=", "byte stream", "           bits", "DNA for", "OQSO for", "OPSO for", "tst no", 
				  "A KSTEST for the 9 p-values", "p=", "p-values:", "p's:", "p-value for no. of wins:", 
				  "p-value for throws/game:"}
				  
		self.tests = ["BIRTHDAY_SPACINGS_TEST", "THE_OVERLAPPING_5_PERMUTATION_TEST", 
				 "BINARY_RANK_TEST_for_31x31_matrices", "BINARY_RANK_TEST_for_32x32_matrices", 
				 "BINARY_RANK_TEST_for_6x8_matrices", "THE_BITSTREAM_TEST", "OPSO", "OQSO", "DNA", 
				 "COUNT_THE_1s_TEST_on_a_stream_of_bytes","COUNT_THE_1s_TEST_for_specific_bytes", 
				 "PARKING_LOT_TEST", "THE_MINIMUM_DISTANCE_TEST", "THE_3DSPHERES_TEST", "SQEEZE_TEST", 
				 "OVERLAPPING_SUMS_TEST", "RUNS_TEST"]


		self.I = [9, (10, 11), 12, 13, 39, (40, 79), (80, 102), (103, 130), (131, 161), (162, 163), (164, 188),
			 189, 190, 211, 212, 213, (214, 217), (219, 220)]		  

		self.P = []

	def parse_TestsOutput(self, d):
		for line in d:
			for key in self.keys_p:
				if key in line:
					p = line.split()[-1]
					if p not in {"sample", "::"}:
						self.P.append(p)
					if p.startswith('p-value='):
						self.P[-1] = self.P[-1][8:]
				

	

	def makeP_values(self,): 
		for i in range(len(self.tests)):
			name, ind = self.tests[i], self.I[i]
			if type(ind) == int:
				self.Test_P[name] = self.P[ind]
			else:
				self.Test_P[name] = self.P[ind[0]:ind[1]+1]
				if name == 'THE_BITSTREAM_TEST':
					self.Test_P[name] = [self.Test_P[name][i] for i in range(len(self.Test_P[name])) if i%2 == 0]
		
        

        


	def makeDict(self, output):
		o = open(output, 'r')
		d = o.readlines()
		self.parse_TestsOutput(d)
		self.makeP_values()



'''ts = Tests()
ts.makeDict(output)
print(ts.Test_P)'''

def main(output):
    ts = Tests()
    ts.makeDict(output)
    return ts.Test_P	
		
if "__name__" == "__main__":
	main(output)
	
			
			
    
    
    
    
    
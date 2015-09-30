import sys
DEBUG = False
F_ABSOLUTE = 4294967296

data_in = {'F':0, 'D':0, 'B':0}
data_out = {'F':0, 'D':0, 'B':0}

def debug(string):
	if DEBUG:
		print(string)
class Pascal:
"""
Pascal class - basic implementation of pascal triangle.
Contains basic helper methods
"""
	def __init__ (self):
	"""
	Empty constructor
	"""
		pass	

	def __single_combi(self, n, k, prev):
	"""
	Helper for factor computation.
	Params: n - row, k - column, prev - preceeding factor
	Return: factor
	"""
		if k == 0:
			return 1
		else:
			return round(prev * ((n+1-k)/k))
	
	def get_row(self, r):
	"""
	Compute all factors in particular row.
	Params: r - row
	Return: row as list of factors
	"""
		a = []
		sc = 0
		for x in range(r+1):
			sc = self_single_combi(r, x, sc)
			a.append(sc)
		return a
	
	def get_factor(self, row, column, prev = 0):
	"""
	Compute particular factor. Uses __single_combi.
	Params: row, column, prev - preceeding factor
	Return: factor
	"""
		factor = 0
		if prev != 0:
			return self.__single_combi(row, column, prev)
		for i in range(column+1):
			factor = self.__single_combi(row, i, prev)
			prev = factor
			if i > row:
				break
		return factor
#end of Pascal class


"""
Egg drop computation functions
"""
#TODO: Encapsulate it in class
def get_Fmax(D, B, useBreak=False):
	F = 0
	prev = 0
	pascal = Pascal()
	#There is max D tries - loop has to be limited
	if B > D:
		B = D
	for i in range(B+1):
		prev = pascal.get_factor(D, i, prev)
		F += prev
		#useBreak is used only for pure Fmax computation, 
		#not for Dmin case
		if useBreak is True and F >= F_ABSOLUTE:
			return -1
	return F-1

def get_Dmin(F, B):
	f = 0
	row = data_out['B']
	while (f<F):
		f = get_Fmax(row, B)
		row +=1
	return row-1

def get_Bmin(F, D):
	f = 0
	factor = 1
	pascal = Pascal()
	for x in range(1, D+1):
		factor = pascal.get_factor(D, x, factor)
		f += factor
		if f >= F:
			return x

def set_data_in(F, D, B):
	data_in['F'] = int(F)
	data_in['D'] = int(D)
	data_in['B'] = int(B)

def compute():
	data_out['F'] = get_Fmax(data_in['D'], data_in['B'], useBreak=True)
	data_out['B'] = get_Bmin(data_in['F'], data_in['D'])
	data_out['D'] = get_Dmin(data_in['F'], data_in['B'])


"""
Main block
"""
if len(sys.argv) != 2:
	print("Usage: " + sys.argv[0] + " <input_file_name> ")
	sys.exit()
else:
	in_lines = []
	f = open(sys.argv[1], 'r')
	#TODO: make output file name generic, basing on input file name
	f2 = open("test.out", 'w')
	for n, line in enumerate(f.readlines()[1:]):
		a = line[:-1].split(" ");
		set_data_in(a[0], a[1], a[2])
		compute()
		f2.write("Case #" + str(n+1) + ": " + str(data_out['F']) + " " + 
				str(data_out['D']) + " " + str(data_out['B']) + '\n')
	f.close()
	f2.close()


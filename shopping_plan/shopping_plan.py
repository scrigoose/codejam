import sys
from math import sqrt

class Point:
	def __init__(self, x, y):
		(self._x, self._y) = (int(x), int(y))
	
	def get_coord(self):
		return str(self._x) + ", " + str(self._y) 

class Shop:
	def __init__(self, line):
		self._products = {}
		tmp = line.split(" ")
		self._position = Point(tmp[0], tmp[1])
		num_of_prod = len(tmp)
		for i in range(2, num_of_prod):
			tmp[i] = '"' + tmp[i] 
			tmp[i] = tmp[i].replace(':', '":')
		prods = "{" + ",".join(tmp[2:]) + "}"
		self._products = eval(prods)

	def show(self):
		print(self._position.get_coord(), "-- Products:", self._products)

class SingleCase:
	def __init__(self):
		self._gas_cost = 0
		self._shops = []
		self._products_to_buy = []

	def show(self):
		print("===")
		print("Products to buy:", self._products_to_buy)
		print("Gas cost:", self._gas_cost)
		print("Shops(" + str(len(self._shops)) + "):")
		for s in self._shops:
			s.show()
class Route:
	def __init__(self, start_point):
		self._currX = start_point._x
		self._currY = start_point._y
	
	def calc_dist(self, dest):
		return sqrt((dest._x - self._currX) ** 2 + (dest._y - self._currY) ** 2)
	

def parse_data_input(input_file_path):
	lineshift = 2
	cases = []
	in_file = open(input_file_path, 'r')
	num_of_cases = int(in_file.readline())
	in_data = in_file.readlines()
	in_file.close()
	index = 0
	for case in range (1, num_of_cases + 1):
		nums = [int(x) for x in in_data[index][:-1].split(" ")]	
		sc = SingleCase()
		sc._gas_cost = nums[2]
		sc._products_to_buy = in_data[index+1][:-1].split(" ")
		for i in range(nums[1]):
			shop = Shop(in_data[index+2+i][:-1])
			sc._shops.append(shop)
		cases.append(sc)	
		index += nums[1] + lineshift 
	return cases
		

cases = parse_data_input('test.in')
for sc in cases:
	sc.show()
	rt = Route(Point(0, 0))
	#print(sc._shops[0]._position)
	#print(sc._shops[0]._position.__class__)
	for shop in sc._shops:
		print(str(rt.calc_dist(shop._position)))




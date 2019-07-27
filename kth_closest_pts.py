import heapq

class PointWithD:
	def __init__(self, vertex, cord):
		self.point = cord
		self.dist = (cord[0]-vertex[0])**2 + (cord[1]-vertex[1])**2  

	def __cmp__(self, other):
		return -cmp(self.dist, other.dist)


def kth_closest(vertex, points, k):
	points_with_d = [PointWithD(vertex, point) for point in points]
	for ptd in points_with_d:
		print ptd.dist

	max_heap=points_with_d[:k]
	heapq.heapify(max_heap)
	#max_heap=[]
	#for pt in points_with_d[:k]:
	#	heapq.heappush(max_heap, pt)

	#while max_heap:
	#	pt = heapq.heappop(max_heap)
	#	print pt.point, pt.dist

	for pt in points_with_d[k:]:
		if pt.dist < max_heap[0].dist:
			print "replace", max_heap[0].point, "with",  pt.point
			heapq.heapreplace(max_heap, pt)

	print "results"	
	while max_heap:
		ptd = heapq.heappop(max_heap)
		print ptd.point


kth_closest((0,0), [(7,7), (1,-1), (8,8), (3,3),(10,10), (2,-2), (5,5)], 3)

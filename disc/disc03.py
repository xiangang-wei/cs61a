"""
This script is to validate the problems in disc03 of cs61a

There is a better solution: https://github.com/tejashah88/cs61a-self-study/blob/master/discussions/disc03/disc03.py
"""

# Constructor and Selectors of tree
def tree(label,branches=[]):
	for branch in branches:
		assert type(branch) == list, 'branch must be list'
	return [label] + branches

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

#################################
# Data abstraction barriers here
#################################

def is_leaf(t):
	return not branches(t)


# Question 3.1 solution
def tree_max(t):
	""" Return the max number of the tree

	>>> t = tree(5,[tree(10,[tree(30)]),tree(3)])
	>>> tree_max(t)
	30
	"""
	# my solution
	return max(all_label(t))

	# better solution
	# return max([label(t)] + [tree_max(x) for x in branches(t)])

def all_label(t):
	""" Return all the number of the tree

	>>> t = tree(5,[tree(10,[tree(30)]),tree(3)])
	>>> all_label(t)
	[5, 10, 30, 3]
	"""
	result = []
	def labels(t):
		if is_leaf(t): 
			result.append(label(t))
		else:
			result.append(label(t))
			for branch in branches(t):
				labels(branch)
	labels(t)
	return result


# Question 3.2 solution
def depth(t):
	""" Return the depth of tree
	
	>>> t = tree(5,[tree(10,[tree(30),tree(20)]),tree(3)])
	>>> depth(t)
	2
	>>> t = tree(5,[tree(10,[tree(30,[tree(40,[tree(60),tree(70)]),tree(50)]),tree(20)]),tree(3)])
	>>> depth(t)
	4
	"""
	# my solution
	if is_leaf(t):
		return 0
	else:
		return max([len(element)-1 for element in all_path(t)])

	# better solution
	# if is_leaf(t):
	# 	return 0
	# else:
	# 	return 1+ max([depth(x) for x in branches(t)])

def all_path(t):
	""" Return a list of lists which is consists of the path from root to leaf
	
	>>> t = tree(5,[tree(10,[tree(30),tree(20)]),tree(3)])
	>>> all_path(t)
	[[5, 10, 30], [5, 10, 20], [5, 3]]
	>>> t = tree(5,[tree(10,[tree(30,[tree(40,[tree(60),tree(70)]),tree(50)]),tree(20)]),tree(3)])
	>>> all_path(t)
	[[5, 10, 30, 40, 60], [5, 10, 30, 40, 70], [5, 10, 30, 50], [5, 10, 20], [5, 3]]
	"""
	res = []
	def paths(t,partitions=[]):
		if is_leaf(t):
			res.append(partitions + [label(t)] ) 
		else:
			for branch in branches(t):
				paths(branch,partitions + [label(t)])
		return res
	return paths(t)


# Question 3.3 solution
def square_tree(t):
	""" Return a tree which is the result of appling square funtion to every element of argument tree
	
	>>> t = tree(5)
	>>> square_tree(t)
	[25]
	>>> t = tree(5,[tree(10,[tree(30),tree(20)]),tree(3)])
	>>> square_tree(t)
	[25, [100, [900], [400]], [9]]
	"""
	if is_leaf(t):
		return tree(label(t)*label(t))
	else:
		root_label = label(t)*label(t)
		return tree(root_label,[square_tree(branch) for branch in branches(t)])

		
# Question 3.4 solution
def find_path(t,x):
	""" Returns a list containing the nodes along the path required to get from the root of the tree to a node containing x.

	>>> t = tree(5,[tree(10,[tree(30),tree(20)]),tree(3)])
	>>> find_path(t,3)
	[5, 3]
	>>> find_path(t,30)
	[5, 10, 30]
	>>> t = tree(2,[tree(7,[tree(6,[tree(5),tree(11)]),tree(3)]),tree(15)])
	>>> find_path(t, 5) 
	[2, 7, 6, 5]
	>>> find_path(t,10)
	"""
	# my solution
	target = [element for element in all_path(t) if x in element]
	if len(target) > 0:
		res = []
		for e in target[0]:
			res.append(e)
			if e == x:
				return res
	else:
		return None

	# better solution
	# if x == label(t):
	# 	return [label(t)]
	# else:
	# 	for path in [find_path(b,x) for b in branches(t)]:
	# 		if path:
	# 			return [label(t)] + path



# Question 3.5 solution
def prune(t,k):
	""" Return the first k level sub-tree of t
	
	>>> t = tree(2,[tree(7,[tree(6,[tree(5),tree(11)]),tree(3)]),tree(15)])
	>>> prune(t, 0)
	[2]
	>>> prune(t, 2)
	[2, [7, [6], [3]], [15]]
	>>> prune(t, 1)
	[2, [7], [15]]
	"""
	if k == 0:
		return tree(label(t))
	else:
		return tree(label(t),[prune(b,k-1) for b in branches(t)])


#################################
# Useful tools
#################################
def print_tree(t,indent=0):
	if is_leaf(t):
		print('  ' * indent + str(label(t)))
	else:
		print('  ' * indent + str(label(t)))
		for b in branches(t):
			print_tree(b,indent+1)





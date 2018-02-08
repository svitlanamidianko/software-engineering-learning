from log import FileLog
logFile = FileLog()

def giftGenerate(count = 1):
	import random
	glist = ['kettle', 'bell', 'chicken', 'donut', 'gingerman', \
			 'doll', 'figure', 'N\' Switch', 'toy car', \
			 'skateboard', 'LEGO set', \
			 'crayons', 'Rubik\'s cube', 'toy truck']

	ans = []
	for _ in range(count):
		ans.append(random.choice(glist))

	logFile.info('Generated ' + str(count) + ' gifts from giftGenerate().')
	return ans

def nameGenerate(count = 1):
	import random
	nlist = ['James', 'David', 'Christopher', 'George', 'Ronal', 'John', \
			 'Richard', 'Daniel', 'Kenneth', 'Anthon', 'Robert', 'Charles',\
			 'Paul', 'Steven', 'Kevi', 'Michael', 'Joseph', 'Mark', 'Edward', \
			 'Jaso', 'William', 'Thomas', 'Donald', 'Brian', 'Jeff', \
			 'Mary', 'Jennifer', 'Lisa', 'Sandra', 'Michell', 'Patricia',\
			 'Maria', 'Nancy', 'Donna', 'Laur', 'Linda', 'Susan', 'Karen',\
			 'Carol', 'Sara', 'Barbara', 'Margaret', 'Betty', 'Ruth',\
			 'Kimberl', 'Elizabeth', 'Dorothy', 'Helen', 'Sharon', 'Debora']

	ans = []
	for _ in range(count):
		ans.append(random.choice(nlist))

	logFile.info('Generated ' + str(count) + ' names from nameGenerate().')
	return ans

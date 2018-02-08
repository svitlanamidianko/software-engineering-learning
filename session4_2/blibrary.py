class ChristmasTree(object):
	from log import FileLog
	logFile = FileLog()

	def __init__(self, giftlist = []):
		self.giftlist = giftlist
		self.tree = None

		self.logFile.info('Christmas tree created.')

	def decorate(self):
		self.tree = list(self.giftlist)
		self.tree = sorted(self.tree, key = lambda st:len(st))

		self.logFile.info('Christmas tree decorated.')

	def show(self):
		if self.tree == None:
			self.logFile.error('Called ChristmasTree.show() before ChristmasTree.decorate().')
			raise Exception('Christmas tree has not been decorated')


		#Generate number of gifts in each row
		layers = []
		giftcount = len(self.tree)
		current_len = 0
		while giftcount > 0:
			current_len += 1
			layers.append(current_len)
			giftcount -= current_len
		pos = len(layers) - 1
		while giftcount < 0:
			layers[pos] -= 1
			giftcount += 1
			pos -= 1

		self.logFile.info('Christmas tree layers generated.')

		#Count number of spaces
		charcount = [0 for _ in range(len(layers))]
		maxcount = 0
		pos = 0
		for i in range(len(layers)):
			for _ in range(layers[i]):
				charcount[i] += len(self.tree[pos]) + 1
				pos += 1
			charcount[i] -= 1
			if charcount[i] > maxcount: maxcount = charcount[i]

		pos = 0
		for i in range(len(layers)):
			print(' ' * ((maxcount - charcount[i] + 1) // 2) + self.tree[pos], end = '')
			for _ in range(1, layers[i]):
				pos += 1
				print(' ' + self.tree[pos], end = '')
			print()
			pos += 1

		self.logFile.info('Successfully printed the Christmas tree.')

	def gift(self, children):
		import random
		random.shuffle(self.giftlist)

		giftcount = 0
		for child in children:
			if len(self.giftlist) == 0:
				print('Oops... The tree is empty!')
				self.logFile.warning('Gift request denied: Christmas tree is empty.')
				break
			print(child + ' gets ' + self.giftlist.pop() + '!')
			giftcount += 1

		self.logFile.info('Successfully gifted ' + str(giftcount) + ' present(s) to children.')
		self.decorate()

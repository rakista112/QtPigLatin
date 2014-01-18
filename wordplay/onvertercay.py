# Pig Latin yo!!!

class OnverterCay(object):
	# Pig Latinizer
	def __init__(self):
		self.vowels = ['a', 'e', 'i', 'o', 'u']
		
	def onvertCay(self, word):
		if not self.is_vowel(word[0]):
			return word[1:] + '-' + word[0] + 'ay'
		else:
			return word + 'way'
		
	def is_vowel(self, letter):
		return letter in self.vowels
        
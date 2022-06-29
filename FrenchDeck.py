from random import choice
import collections


'''
纸牌模拟小游戏
'''

Card = collections.namedtuple('Card',['rank','suit'])
class FrenchDeck():
	"""docstring for FrenchDeck"""
	ranks = [ str(i) for i in range(2,11)] + list('JQKA')
	suits = ['spades','diamonds','clubs','hearts']
	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
	def __len__(self):
		return len(self._cards)
	def __getitem__(self,position):
		return self._cards[position]
if __name__ == "__main__":
	deck = FrenchDeck()
	# print(len(deck))
	# print(deck[0],deck[-3])
	# print(choice(deck))
	for card in deck: # doctest:+ELLIPSIS
		print(card)
	suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
	def spades_heigh(card):
		rank_value = FrenchDeck.ranks.index(card.rank)
		return rank_value * len(suit_values) + suit_values[card.suit]
	for card in sorted(deck,key=spades_heigh):
		print(card)
import random

cards = ['card 1', 'card 2', 'card 3', 'card 4', 'card 5', 'card 6', 'card 7', 'card 8',]
cards_selected = []

card = 'card 2'
special_card = 'special card'


def random_select():
	card = random.choice(cards)
	print(card)



def add_to_selected():
	cards_selected.append(card)
	print(cards_selected)


def check_if_in_list():
	if card in cards_selected:
		print('card already selected')
#		return False
	else:
		print('its a new card')
#		return True



def compare_lists():
	compared = set(cards) & set(cards_selected)
	print(compared)


def list_length():
	lt_len = len(cards_selected)
	print(lt_len)


def check_turns():
	lt_len = len(cards_selected)
	
	if lt_len == 6:
		cards.append(special_card)




random_select()

add_to_selected()

check_if_in_list()

compare_lists()

list_length()

check_turns()

print(cards_selected)
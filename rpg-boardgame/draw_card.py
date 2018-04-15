import random

# dungeon_deck = 
# treasure_deck = 
# event_deck = 

# room_card = {"room_name" : "", "room_type" : "", "description" : "", "special_rules" : ""}

# treasure_card = {"item_name" : "", "description" : "", "special_rules" : "", "gold_value" : "", "item_duration" : ""}

# event_card = {}

cards = ['card 1', 'card 2', 'card 3', 'card 4', 'card 5', 'card 6', 'card 7', 'card 8',]
cards_selected = []


def draw_card():

	if 'special_card' in cards_selected:
		print("the special card has been selected. Please start a new game.")
		return

	if len(cards_selected) == 4:
		cards.append('special_card')
		print(cards)

	card = random.choice(cards)
	selected = check_if_in_list(cards_selected, card)

	if selected == True:
		cards_selected.append(card)

		print(card)
		print(cards_selected)
	else:
		print('pick another card')
		draw_card()



def check_if_in_list(cards_selected, card):
	if card in cards_selected:
		print('card already selected')
		return False
	else:
		print('its a new card')
		return True


draw_card()






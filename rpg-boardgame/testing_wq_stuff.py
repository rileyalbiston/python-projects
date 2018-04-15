card_1 = {"name":"bob", "stats":"fast"}

card_2 = {"name":"tom", "stats":"slow"}

deck_1 =[card_1, card_2]


print(deck_1[0])
print(deck_1[0]['name'])
print(deck_1[0]['stats'])


print(deck_1[1])
print(deck_1[1]['name'])
print(deck_1[1]['stats'])






import sys
import random


treasure_deck = "treasure_deck"
event_deck = "event_deck"




# room_card = {"room_name" : "", "room_type" : "", "description" : "", "special_rules" : ""}

# treasure_card = {"item_name" : "", "description" : "", "special_rules" : "", "gold_value" : "", "item_duration" : ""}

# event_card = {}



cards_selected = []

def draw_card(deck):

	if 'special_card' in cards_selected:
		print("the special card has been selected. Please start a new game.")
		return

	if len(cards_selected) == 3:
		deck.append('special_card')
		print(deck)

	card = random.choice(deck)
	selected = check_if_in_list(cards_selected, card)

	if selected == True:
		cards_selected.append(card)

		print(card)
		print(cards_selected)
	else:
		print('pick another card')
		draw_card(deck)



def check_if_in_list(cards_selected, card):
	if card in cards_selected:
		print('card already selected')
		return False
	else:
		print('its a new card')
		return True


def exit_program(exit):
        exit()


def draw_dungeon_card():

	room_card_1 = {"room_name" : "1", "room_type" : "1", "description" : "1", "special_rules" : "1"}
	room_card_2 = {"room_name" : "2", "room_type" : "2", "description" : "2", "special_rules" : "2"}
	room_card_3 = {"room_name" : "3", "room_type" : "3", "description" : "3", "special_rules" : "3"}
	room_card_4 = {"room_name" : "4", "room_type" : "4", "description" : "4", "special_rules" : "4"}
	room_card_5 = {"room_name" : "5", "room_type" : "5", "description" : "5", "special_rules" : "5"}

	dungeon_deck = [room_card_1, room_card_2, room_card_3, room_card_4, room_card_5]

	print("\nYou chose dungeon deck.")

	draw_card(dungeon_deck)


def  draw_treasure_card():
	print("\nYou chose treasure deck.")


def draw_event_card():
	print("\nYou chose the event deck.")




menu_options = {
                "dungeon deck"  : draw_dungeon_card,
                "treasure deck"  : draw_treasure_card,
                "event deck" : draw_event_card,
                "exit" : exit_program,
        }


# ===================================== menu ============================================== #


def main():
    while True:
        print("\n")
        print("//  ==============  menu  ==============  //")
        print("Please choose one of the following options:\n1) dungeon deck\n2) treasure deck\n3) event deck\n4) exit")

        
#        try: 
        user_input = input(str("Input:\n")).lower()

        menu_options[user_input]()


        # the key error exception is important. Always include.
#        except KeyError:
#                print("Invalid option. Please try again.")
#
#                
#        # other error exceptions may be optional/useful depending on the program
#        except NameError:
#                print("there was a name error.")
#        except KeyError:
#                print("there was a key error.")
#        except TypeError:
#                print("there was a type error.")
#        except ValueError:
#                print("there was a value error.")
#        except OSError as err:
#                print("OS error: {0}".format(err))
#        except:
#                print("Unexpected error:", sys.exc_info()[0])
#        raise


if __name__ == '__main__':
    main()
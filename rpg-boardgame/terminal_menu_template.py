import sys


def function_one():
        print("\nYou chose function one.")


def function_two():
        print("\nYou chose function two.")


def exit_program():
        exit()


menu_options = {
                "one"  : function_one,
                "two"  : function_two,
                "exit" : exit_program,
        }

while True:
        print("\n")
        print("//  ==============  menu  ==============  //")
        print("Please choose one of the following options:\n1) One\n2) Two\n3) exit")

        
        try: 
                user_input = input(str("Input:\n")).lower()

                menu_options[user_input]()

                # old skool way of doing things. if statements, so many if statements :o
#                if user_input == "one":
#                        function_one()
#                        print("you chose one")
#                elif user_input == "two":
#                        function_two()
#                        print("you chose two")
#                elif user_input == "" or user_input == " ":
#                        print("you didn't enter anything! Try again.")
#                elif user_input == "exit":
#                        exit_program()
#                        print("the program will exit now.")
#                else:
#                        print("unknow input. Please try again.")


        # the key error exception is important. Always include.
        except KeyError:
                print("Invalide option. Please try again.")

                
        # other error exceptions may be optional/useful depending on the program
        except NameError:
                print("there was a name error.")
        except KeyError:
                print("there was a key error.")
        except TypeError:
                print("there was a type error.")
        except ValueError:
                print("there was a value error.")
        except OSError as err:
                print("OS error: {0}".format(err))
        except:
                print("Unexpected error:", sys.exc_info()[0])
                raise




                
                        

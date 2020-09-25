import time
import random

# I tried to put these list on functions,
# but i didn't know what to pass as parameters.
creatures = random.choice(
    ["Spock", "Peter Pan", "Thanos", "Darth Vader"])

some_place = random.choice(
    ["Walmart", "Roman Forum", "Microsoft", "Theater"])


def print_pause(message):
    print(message)
    time.sleep(2)


def field():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that {creatures} is somewhere around here, "
                "and has been terrifying the nearby village")
    print_pause("In front of you there is a house.")
    print_pause(f"To your right is a {some_place}.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n\n")


def main(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause(f"Enter 2 to peer into the {some_place}")
    print_pause("What would you like to do?")
    # I thought about putting the input on a function,
    # but i decided that it would not improve a lot and
    # i didn't know if i could make a function with all the inputs
    choice = input("(Please enter 1 or 2)\n\n")
    if choice == "1":
        house(items)
    elif choice == "2":
        place(items)
    else:
        main(items)


def house(items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock wheen the door opens and "
                f"out steps {creatures}")
    print_pause(f"Eep! This is {creatures}'s house!")
    print_pause(f"{creatures} attacks you!")
    fight(items)


def place(items):
    print_pause(f"You peer cautiously into the {some_place}.")
    print_pause(f"It turns out to be only a vary small {some_place}.")
    print_pause("Your eyes catches a glint of metal behind a shelf.")
    print_pause("You have found the magical Sword of Ogoroth!")
    items.append("sword")
    print_pause("You discard your silly old dagger and take the sword "
                "with you.")
    print_pause("You walk back out to the field.\n\n")
    main(items)


def fight(items):
    if "sword" in items:
        choice = input("Would you like to (1) fight or (2) run "
                       "away?\n\n")
        if choice == "1":
            print_pause(f"As {creatures} moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause(f"But {creatures} takes one look at "
                        "your shiny new toy and runs away!")
            print_pause(f"You have rid the town of {creatures}. "
                        "You are victorious!")
            play_again()
        elif choice == "2":
            print_pause("You run back into the field. Luckily, "
                        "you don't seem to have been followed.")
            main(items)
    else:
        print_pause("You feel a little bit under-prepared for this, "
                    "what with only a tiny dagger.")
        choice = input("Would you like to (1) fight or (2) run "
                       "away?\n\n")
        if choice == "1":
            print_pause("You do your best...")
            print_pause(f"But your dagger is no match for {creatures}")
            print_pause("You have been defeated!")
            play_again()
        elif choice == "2":
            print_pause("You run back into the field. Luckily, "
                        "you don't seem to have been followed.\n\n")
            main(items)


def play_again():
    choice = input("Would you like to play again? (y/n)\n")
    if choice == "y":
        print_pause("Excelent! Restarting the game...")
        play_game()
    elif choice == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


def play_game():
    items = []
    field()
    main(items)


play_game()

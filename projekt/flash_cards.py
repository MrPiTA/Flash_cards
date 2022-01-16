import random
import sys

# Globalna zmienna do fiszek
flash_cards = {}


def read_flash_cards_from_text_file():
    """Wczytuje linia po linijce nazwę fiszki wraz z definicją z lokalnego pliku txt """
    global flash_cards

    with open("pliki/flash_cards.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            lines_arr = line.split("<=>")
            card_name = lines_arr[0]
            definition = lines_arr[1]
            flash_cards[card_name] = definition

    if len(flash_cards) < 4:
        print("You must have at least 4 4 flash cards in text file before starting FlashCards, exiting program now")
        sys.exit()


def update_flash_cards(card_name, new_definition, save_to_file=True, delete_flash_card=False):
    """Zawsze wywyływana przy dodawaniu, usuwaniu lub zmianie fiszek"""
    global flash_cards

    if delete_flash_card:
        del flash_cards[card_name]
    else:
        flash_cards[card_name] = new_definition

    if save_to_file:
        write_flash_cards_to_text_file()


def write_flash_cards_to_text_file():
    """Wpiszę linia za linią nazwę i definicję każdej fiszki do pliku txt ,żeby je zachować"""

    if len(flash_cards) < 4:
        print("Error: You must have at least four flash cards to save to a text file!")
        return

    with open("pliki/flash_cards.txt", "w", encoding="utf-8") as file:
        for card_name, definition in flash_cards.items():
            card_name = card_name.strip()
            definition = definition.strip()
            inscribe = f"{card_name}<=>{definition}\n"
            file.write(inscribe)


def add_flash_card():
    """Wywoływana z menu, aby stworzyć lub zupdatować fiszkę"""

    card_name = input("Enter card name: ")
    definition = input("Enter the definition: ")
    save_to_file = input("Save to file (y/n)?: ").lower()

    if save_to_file == "y" or save_to_file == "yes":
        save_to_file = True
    else:
        save_to_file = False

    update_flash_cards(card_name, definition, save_to_file)


def remove_flashcard():
    """Wywyływana z menu, aby usnuąć fiszkę"""
    global flash_cards
    card_name = input("Enter card name: ")
    save_to_file = input("Delete from file (y/n)?: ").lower()

    if save_to_file == "y" or save_to_file == "yes":
        save_to_file = True
    else:
        save_to_file = False

    if card_name not in flash_cards:
        print(f"Error: Card name '{card_name}' is not in flash cards")
    else:
        update_flash_cards(card_name, "", save_to_file=save_to_file, delete_flash_card=True)


def study_flash_cards():
    """Włącza tryb nauki z menu """
    global flash_cards

    flag = 1
    for card, definition in flash_cards.items():
        print("Card: " + card)
        print("Definition: " + definition)
        exit_study = input("\nPress ENTER to move to the next flash card, type Q to quit study mode\n").lower()
        if exit_study == "q":
            flag = 0
            break
        print("-------------------------------")
    print("\r")
    if flag:
        print("All flash cards are complete!")
    else:
        print("You have quit study mode!")
    print("-------------------------------")
    print("\r")


def get_valid_int_input():
    """Zwraca numer 1-4 lub -1 ,żeby opuścić program"""
    is_valid = False
    answer = -1
    while not is_valid:
        answer = input("Enter option 1-4 or Q to quit: ").lower()
        if answer.isnumeric():
            answer = int(answer)
            if 1 <= answer <= 4:
                is_valid = True
            else:
                print("Error: Please enter 1-4 or Q")
        else:
            if answer == "q":
                answer = -1
                is_valid = True
            else:
                print("Error: Please enter 1-4 or Q")

    return answer


def get_random_choices(answer, definitions):
    """Zwraca losowo potasowaną listę wyborów dla trybu quiz"""
    global flash_cards

    answers = [answer]

    while len(answers) < 4:
        random_definition = random.choice(definitions)
        if random_definition not in answers:
            answers.append(random_definition)

    random.shuffle(answers)

    return answers


def take_quiz():
    """Włącza tryb quiz z menu"""
    global flash_cards

    if len(flash_cards) < 4:
        print("Not enough flash cards to quiz with, add more cards")
        return

    card_names = list(flash_cards.keys())
    definitions = list(flash_cards.values())

    random.shuffle(card_names)
    random.shuffle(definitions)

    score = 0
    question_answered = 0

    for card_name in card_names:
        print("What is the definition for " + card_name)
        answer_choices = get_random_choices(flash_cards[card_name], definitions)

        for i in range(len(answer_choices)):
            print(str(i + 1) + ") " + answer_choices[i])


        answer = get_valid_int_input() - 1


        if answer == -2:
            print("Exiting Quiz")
            print("\r")
            break
        else:
            question_answered += 1

        print("\r")

        if answer_choices[answer] == flash_cards[card_name]:
            print("You chose the correct answer!")
            score += 1
            print("+1 Point")
        else:
            print("Sorry, the correct answer was:")
            print(card_name + " - " + flash_cards[card_name])
        print("-------------------------------")
        print("\r")

    print("Quiz is complete")
    print("Your total score was " + str(score) + "/" + str(question_answered))


def print_menu():
    """Wyświetla opcje menu"""
    menu = """
    1. Add/update a flash card
    2. Delete a flash card
    3. Save flash cards to text file
    4. Study Mode
    5. Quiz Mode
    6. Exit FlashCards
    """

    print(menu)


def get_valid_menu_input():
    """Zwraca cyfrę odpowiednio od 1 do 6"""
    is_valid = False
    answer = -1
    while not is_valid:
        answer = input("Enter option 1-6: ")
        if answer.isnumeric():
            answer = int(answer)
            if 1 <= answer <= 6:
                is_valid = True
            else:
                print("Error: Please enter number 1-6")
        else:
            print("Error: Please enter number 1-6")
    return answer


def recursive_tree(n, star=1, tabs=3):
    """rekurencyjna funkcja printująca choinkę podczas wyświetlenia menu, aby wykorzstać wszystko co było na zajęciach"""
    spaces = (n - star) // 2
    if spaces == 0:
        return print(("\t" * tabs) + n * " * ", end="\r")
    else:
        print(("\t" * tabs) + (" . " * spaces) + ( " * " * star) + (" . " * spaces))
        return recursive_tree(n, star+2, tabs)

def reversed_recursive_tree(n, spaces=0, tabs=3):
    """rekurencyjna funkcja printująca odwróconą choinkę podczas wyświetlenia menu"""
    stars = n - (2 * spaces)
    if stars <= 1:
        return print(("\t" * tabs) + (" . " * spaces) + " * " + (" . " * spaces))
    else:
        print(("\t" * tabs) + (" . " * spaces) + ( " * " * stars) + (" . " * spaces))
        return reversed_recursive_tree(n, spaces + 1, tabs)


def main():
    """Funkcja główna programu, pozwala na wybór opcji z menu"""
    global flash_cards

    read_flash_cards_from_text_file()

    run_loop = True

    recursive_tree(7,tabs=2)

    print("""
    ....Welcome to FlashCards....
    """, end="\r")

    reversed_recursive_tree(7,tabs=2)

    while run_loop:
        print_menu()
        option = get_valid_menu_input()
        if option == 1:
            add_flash_card()
        elif option == 2:
            remove_flashcard()
        elif option == 3:
            write_flash_cards_to_text_file()
        elif option == 4:
            study_flash_cards()
        elif option == 5:
            take_quiz()
        elif option == 6:
            run_loop = False

    print("Thanks for using FlashCards")




if __name__ == '__main__':
    main()

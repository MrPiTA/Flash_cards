import random
import sys
import time

# Globalna zmienna do fiszek
flash_cards = {}


def read_flash_cards_from_text_file():
    """Wczytuje linia po linijce nazwę fiszki wraz z definicją z lokalnego pliku txt """
    global flash_cards
    tmp = []
    card_name = []
    definition = []

    with open("pliki/flash_cards.txt", "r") as file:
        for line in file:
            line = line.strip()
            lines_arr = line.split("=")
            tmp.append(lines_arr)

    for arr in tmp:
        card_name.append(arr[0].strip())
        definition.append(arr[1].strip())
        flash_cards[arr[0]] = arr[1]

    if len(flash_cards) < 4:
        print("You must have at least 4 4 flash cards in text file before starting Quizlet, exiting program now")
        sys.exit()

    return flash_cards, card_name, definition


def update_flash_cards():
    """Będzie zawsze wywyływana przy dodawaniu, usuwaniu lub zmianie fiszek"""
    global flash_cards

    pass


def write_flash_cards_to_text_file():
    """Wpiszę linia za linią nazwę i definicję każdej fiszki do pliku txt ,żeby je zachować"""

    pass


def add_flash_card():
    """Będzie wywoływana z menu głównego aby stworzyć lub zupdatować fiszkę"""

    pass


def remove_flashcard():
    """Będzie wywyływana z menu, aby usnuąć fiszkę"""
    global flash_cards

    pass


def study_flash_cards():
    """Będzie włączać tryb nauki z menu """
    global flash_cards

    pass


def get_valid_int_input():
    """Będzie zwracać numer 1-4 lub -1 ,żeby opuścić program"""


def get_random_choices(answer, definitions):
    """Będzie zwracać losowo potasowaną listę wyborów dla trybu quiz """
    global flash_cards

    pass


def take_quiz():
    """Włącza tryb quiz z menu """
    global flash_cards

    pass


def print_menu():
    """Wyświetla opcje menu"""
    menu = """
    1. Add/update a flash card
    2. Delete a flash card
    3. Save flash cards to text file
    4. Study flash cards
    5. Be quizzed on flash cards
    6. Exit Quizlet
    """

    pass


def get_valid_menu_input():
    """Zwraca cyfrę odpowiednio od 1 do 6"""

    pass


def main():
    """Funkcja główna programu, pozwala na wybór opcji z menu"""
    global flash_cards
    print(read_flash_cards_from_text_file())


if __name__ == '__main__':
    main()

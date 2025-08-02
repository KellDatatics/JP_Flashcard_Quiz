import csv
import random


filename = 'vocab1.csv'

flashcards =[]

def load_flashcards_from_csv(level_choice):
    global flashcards
    flashcards = []

    try:
        with open("vocab1.csv", mode="r", encoding="utf-8")as file:
            reader= csv.DictReader(file)
            for row in reader:
                if row["Level"].strip().upper()== level_choice:
                    flashcards.append({
                        "kanji": row["Kanji"].strip(),
                        "kana": row["Kana"].strip(),
                        "romaji": row["Romaji"].strip().lower(),
                        "meaning": row["Meaning"].strip().lower()
                        
                    })

        if not flashcards:
            print(f' ⚠️ No flashcards found for {level_choice}')
        else:
            print(f"✅ Loaded {len(flashcards)} flashcards for {level_choice}")

    except FileNotFoundError:
        print(" ❌ Vocab1.csv not found.  Please make sure it is in the same folder. ")
    except Exception as e:
        print(f" ❌ Error reading CSV: {e}")



def quiz_front(vocab_list, quiz_length=10):
    score = 0

    random.shuffle(vocab_list)
    quiz_words = vocab_list[:quiz_length]

    for entry in quiz_words:
        front = f"{entry['kanji']} ({entry ['kana']})"
        answer = input(f" What is the romaji for: {front}? ").strip().lower()

        if answer == entry['romaji'].lower():
            print("✅ Correct!\n")
            score += 1

        else:
            print(f"❌ Incorrect!😥 Answer: {entry['romaji']} ({entry['meaning']})\n")

    print (f" 🏁 Final Score: {score} / {len(quiz_words)}")


def quiz_back(vocab_list, quiz_length=10):
    score = 0

    random.shuffle(vocab_list)
    quiz_words = vocab_list[:quiz_length]

    for entry in quiz_words:
        back = f" {entry['meaning']}"
        answer = input(f" What romaji matches this: {back}? ").strip().lower()

        if answer == entry['romaji'].lower():
            print("✅ Correct!\n")
            score +=1

        else:
            print(f"❌ Incorrect!😥 Answer: {entry['romaji']} ({entry['kanji']}) ({entry['kana']})\n")

    print (f" 🏁 Final Score: {score} / {len(quiz_words)}")


def select_level():
    global flashcards
    while True:
        print("\n 🌸 Select JLPT Level")
        print(" Select 1. N4 ")
        print(" Select 2. N5 ")

        level_input = input("Choose a level (1 or 2): ").strip()
        if level_input == "1":
            load_flashcards_from_csv("N4")
            break
        elif level_input == "2":
            load_flashcards_from_csv("N5")
            break
        else:
            print(" ⚠️ Invalid input.  Please enter 1 or 2 ")



def main_menu():
    while True:
        print("\n 📚 Japanese Flashcard Quiz")
        print("1. Guess the Romaji from the Kanji and Kana")
        print("2.  Guess the Romaji from the English Meaning")
        print("3.  Change JLPT level")
        print("4.  Exit")

        choice= input("Select an option from 1-4: ")

        if choice == "1":
            quiz_front(flashcards, quiz_length=10)
        elif choice == "2":
            quiz_back(flashcards, quiz_length=10)
        elif choice == "3":
            select_level()
        elif choice == "4":
            print(" 👋 Ja Mata じゃまた ")
            break
        
        else:
            print(" ⚠️ Invalid choice! Please select from options 1-4")

if __name__ == "__main__":
    select_level()
    main_menu()






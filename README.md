# 🈶 Japanese Vocab Quiz (JLPT N5/N4)

A command-line flashcard quiz tool to help you study Japanese vocabulary — designed for JLPT N5 and N4 levels. Choose from two quiz modes and track your score!

## ✨ Features

- Supports JLPT **N5** and **N4** vocab levels
- Two quiz modes:
  1. **Guess the Romaji** from Kanji + Kana
  2. **Guess the Romaji** from English meaning
- Randomized 10-question quizzes
- User-friendly text prompts
- Built-in menu navigation and level switching

## 📁 File Structure

jp_flashcards_project/
├── vocab1.csv
├── jp_flashcards.py
└── README.md


## 📋 CSV Format (`vocab1.csv`)

Make sure your CSV file uses the following headers:

Level,Kanji,Kana,Romaji,Meaning
N5,学生,がくせい,gakusei,student
N4,必要,ひつよう,hitsuyou,necessary


## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Place `vocab1.csv` in the same folder as `jp_flashcards.py`.
3. Open your terminal and run:

```bash
python jp_flashcards.py
Follow the prompts to select JLPT level and quiz type.

## 📸 Sample Outputs

**Main Menu**
![Main Menu](image/main_menu.png)

**Example Correct Answer**
![Correct Answer](https://github.com/KellDatatics/JP_Flashcard_Quiz/blob/main/images/example%20correct%20answer.png?raw=true)

**Example Incorrect Answer**
![Incorrect Answer](https://github.com/KellDatatics/JP_Flashcard_Quiz/blob/main/images/example%20incorrect%20answer.png?raw=true)

**Example Final Score**
![Final Score](https://github.com/KellDatatics/JP_Flashcard_Quiz/blob/main/images/example%20final%20score.png?raw=true)

🛠️ Built With
Python 3
csv and random modules
Simple text-based interface

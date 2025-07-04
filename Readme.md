# Task 1
# Calculator App 🔢
# CLI (Command Line Interface )
A simple Python-based calculator app that runs in the terminal.

## Features
- Addition
- Subtraction
- Multiplication
- Division
- Loops until user exits


# Task 2: CLI To-Do List Application (Python)

This is a simple **console-based To-Do List manager** built using Python.  
It allows users to **add**, **view**, and **remove** tasks — and it **saves them persistently** using a local text file (`tasks.txt`) stored inside the project folder.

---

# Objective

> Build a persistent, terminal-based task manager using Python lists and file I/O.

---

# 🔧 Tools Used

- **Python 3.x**
- **VS Code / Terminal**

---

# 🚀 Features

- 📝 View current tasks
- ➕ Add new tasks
- ❌ Remove tasks by number
- 💾 Persistent task saving via `tasks.txt`
- 📂 All data stored safely inside the `task2/` folder

---

# Task 3: Web Scraper for News Headlines

- Scrapes headlines from a news site using `requests` and `BeautifulSoup`.
- Stores the result in `headlines.txt`.

> Files: `news_scraper.py`, `headlines.txt`,'requirements.txt'

# ⚙️ Tools & Tech

- 🐍 Python 3
- 🌐 Requests (to fetch HTML)
- 🍲 BeautifulSoup (for parsing HTML)
- 📄 Plain `.txt` file (to save headlines)
## 🧠 How It Works

1. Sends a GET request to a news website.
2. Parses the HTML content using BeautifulSoup.
3. Extracts text from all `<h2>` or `<h3>` tags.
4. Saves the headlines to a local text file `headlines.txt`.
## Run it
```bash
## 📌 Objective:
Create a simple Flask API that shows a message when run.

## 🛠 Tools Used:
- Python
- Flask

## ▶️ How to Run:

1. Install Flask:
```bash
# Task 4: Flask API

## 📌 Objective:
Create a simple Flask API that shows a message when run.

## 🛠 Tools Used:
- Python
- Flask

## ▶️ How to Run:

1. Install Flask:
```bash
pip install flask
# 📊 Tyagi Associate – Task 5

## 🎯 Goal:
Analyze mock trading data (2000 rows) using Python & Pandas.

## 🧰 Tools:
Python, Pandas, Matplotlib

## 📁 Dataset:
`Tyagi_Associate_Paper_Trading_Data_2000.csv`

## 🔍 Steps:
- Load & explore CSV
- Calculate total Profit/Loss
- Group by Stock Symbol
- Plot trading value & profit/loss

## 🧠 Result:
Quick insights into stock-wise trade performance.gi
python calculator.py
python Tod.py
python News_scrapper.py# Task 4: Flask API
# Flask Portfolio Website

This is a simple portfolio website built using Python Flask.  
It includes:

- Home page
- Contact page
- Backend with Flask
- HTML templates in `templates/` folder

Run it locally:
```bash
python app.py

# Task 7 - Image Resizer Tool

## 📌 Objective:
Resize all images in a folder and save them in a different folder.

## 🛠 Tools Used:
- Python
- Pillow (PIL)

## ▶️ How to Run:
1. Put images in `input_images/` folder
2. Run command: `python resizer.py`
3. Resized images will be saved in `output_images/`

TASK *8
# Real Conversation Voice Chatbot 🎙️💬

This is a Python-based voice chatbot that feels like you're talking to a real friend.  
It responds in natural Hinglish, handles real-life phrases like:

- "Kya kar rahe ho?"
- "Tum mujhe Google par le chalo"
- "Bore ho gaya hoon"
- "Haryanvi song chalao"

and much more!

---

## 🔧 Features

- 🎤 Voice Input (Mic se baat)
- 🔊 Voice Output (Natural replies)
- 😄 Random friendly responses
- 🌐 Opens Google, YouTube, Haryanvi songs on command

---

## 🚀 How to Run

### Step 1: Install requirements
```bash
pip install speechrecognition pyttsx3 pyaudio
# 🎰 Console-Based Casino System

## 🧾 Project Overview

This is a **Console-based Casino Management System** developed in Python as a final project for the Programming Techniques course. It includes player management, a collection of mini-games, reporting modules, and utilities.

This project showcases:
- Advanced programming concepts (recursion, backtracking)
- Classical data structures (stacks, queues)
- Data persistence (JSON)
- Search and sorting algorithms

---

## ✅ Features

- 👤 Player management with JSON persistence
- 🕹️ Mini-games:
  - Slot Machine (Brute force)
  - Simplified Blackjack (Recursion with stack)
  - Guessing Game (Recursion with queue)
  - Betting Strategy Solver (Backtracking)
- 📊 Player activity tracking using custom stacks
- ⏳ Queue system for popular tables
- 🔍 Utilities for search and sorting
- 📈 Report generation (top players, history, ranking, etc.)

---

## 📁 Project Structure

```bash
casino/
│
├── data/
│   └── players.json              # Persistent player data file
│
├── games/
│   ├── blackjack.py              # Blackjack game using recursion with stack
│   ├── guessing_game.py          # Guessing game using recursion with queue
│   ├── slot_machine.py           # Slot machine using brute force
│   └── strategy_solver.py        # Betting strategy solver using backtracking
│
├── players/
│   ├── player.py                 # Player class with stack-based history
│   ├── player_manager.py         # Player CRUD and validation
│   └── waiting_queue.py          # Queue management for popular tables
│
├── reports/
│   └── report_generator.py       # Report generation module
│
├── utils/
│   ├── custom_stack.py           # Custom stack implementation
│   ├── file_handler.py           # JSON read/write
│   ├── search_algorithms.py      # Linear and binary search algorithms
│   └── sorting_algorithms.py     # Bubble, selection, insertion, and merge sort
│
├── main.py                       # Main entry point
└── README.md                     # Project documentation
```

---

## 🚀 Getting Started

### Requirements
- Python 3.8 or higher

### Run the program

```bash
python main.py
```

---

## 📊 Included Reports

- Top N players with the highest balance
- Full history of a specific player
- Player ranking by games played
- Players with the most losses
- Most popular games

---

## 💡 Concepts Used

- Object-Oriented Programming (OOP)
- JSON file handling
- Stacks and Queues
- Recursion and Backtracking
- Search and Sorting Algorithms

---

## 🧑‍💻 Authors

- Víctor Manuel Valencia Álvarez
- Juan José Hernández Velasquez

---

## 📜 License

This project was developed for educational purposes.
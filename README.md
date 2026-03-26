# Personalized Diet Recommendation System
## Constraint Satisfaction & Heuristic Search Based Diet Planner

## Project Overview
This project is a Personalized Diet Recommendation System that generates optimal meal plans based on user biometrics such as age, weight, height, and diet preference (Veg / Non-Veg). The system uses Constraint Satisfaction logic and a Heuristic Search Algorithm to select the best meal from a structured food database.

Unlike traditional calorie calculators, this system considers age-based metabolic differences and searches for the most suitable meal option instead of giving fixed diet charts.

---

## Features
- Personalized diet recommendation
- Age-based metabolic tier classification (Youth, Adult, Elder)
- Constraint Satisfaction based decision making
- Heuristic Search meal selection
- Veg / Non-Veg diet selection
- Metric / Imperial unit support
- TDEE (Total Daily Energy Expenditure) calculation
- Macro nutrients display (Protein, Carbs, Fat)
- GUI built using Tkinter
- Animated interface

---

## Age Tier Classification

| Age Range | Tier  | Metabolic Multiplier |
|-----------|-------|----------------------|
| 14–24     | Youth | 1.5 |
| 25–55     | Adult | 1.35 |
| 56+       | Elder | 1.2 |

---

## TDEE Formula
TDEE = ((10 × weight) + (6.25 × height) − (5 × age) + 5) × metabolic multiplier


---

## Technologies Used
- Python
- Tkinter (GUI)
- Heuristic Search Algorithm
- Constraint Satisfaction Logic
- Nutrition Food Database

---

## Project Structure
project/
│
├── project work.py
├── README.md


---

## How to Run the Project
1. Install Python 3
2. Download the project files
3. Open terminal in the project folder
4. Run the program:


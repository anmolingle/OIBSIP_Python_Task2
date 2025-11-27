# 📉 Advanced BMI Tracker (Tkinter & SQLite)

This is a desktop application developed in Python using the Tkinter library for the GUI and SQLite for persistent data storage. It allows users to calculate their Body Mass Index (BMI), save their history, and visualize the trend over time using Matplotlib.

## ✨ Features

* **GUI Interface:** Easy-to-use graphical interface for entering weight and height.
* **BMI Calculation:** Calculates BMI using the standard formula: $BMI = \frac{Weight}{(Height)^2}$.
* **Data Persistence:** Saves the date and calculated BMI to a local SQLite database (`bmi_data.db`).
* **Trend Visualization:** Generates a line graph showing BMI history over entry number using Matplotlib.
* **Threshold Lines:** The graph includes visual markers for the Overweight ($\text{BMI} = 25$) and Underweight ($\text{BMI} = 18.5$) thresholds.

## 🛠️ Prerequisites

Before running the application, ensure you have Python 3 installed. You will also need the following libraries, which can be installed using `pip`.

## 🚀 Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/anmolingle/OIBSIP_Python_Task2.git
    cd OIBSIP_Python_Task2
    ```

2.  **Install Dependencies:**
    Install all required Python packages using the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application:**
    Execute the main Python script:
    ```bash
    python BMI_Calculator.py
    ```

## 📂 Project Structure

The repository should contain the following files:

````

OIBSIP_Python_Task2/
├── BMI_Calculator.py  \# The main application script
├── README.md          \# Project information (This file)
└── requirements.txt   \# List of dependencies

```

**(Note: The SQLite database file, `bmi_data.db`, will be created automatically when the application is run for the first time.)**
```

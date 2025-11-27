# 📈 Advanced BMI Tracker (Tkinter & SQLite)

A simple, desktop-based health tracking application built using Python's **Tkinter** for the graphical user interface, **SQLite** for local data persistence, and **Matplotlib** for visualization. It calculates your Body Mass Index (BMI) and tracks your history over time.

## ✨ Features

* **BMI Calculation:** Calculates BMI instantly using the standard formula: $BMI = \frac{\text{Weight (kg)}}{\text{Height (m)}^2}$.
* **Data Saving:** Automatically saves the date and the calculated BMI value to a local database.
* **Historical Tracking:** Stores all calculated entries in an SQLite database (`bmi_data.db`).
* **Visualization:** Generates an interactive line graph showing your BMI trend over all recorded entries.
* **Threshold Lines:** The graph includes horizontal reference lines for **Underweight** (18.5) and **Overweight** (25.0) categories.

## 🚀 Installation & Setup

### 1. Prerequisites

You must have Python 3.x installed on your system.

### 2. Clone the Repository

If you haven't yet, clone your repository and navigate into the project directory:

```bash
git clone <repository_url>
cd <repository_name>
````

### 3\. Install Dependencies

Install the required libraries using pip. **Note:** Tkinter and SQLite are usually built-in with standard Python installations, but Matplotlib is required:

```bash
pip install -r requirements.txt
```

### 4\. Database Initialization

No manual setup is required. The application will automatically create the `bmi_data.db` file in the project directory when you run it for the first time.

## ⚙️ How to Run

Execute the main Python script from your terminal:

```bash
python BMI_Calculator.py
```

## 🛠️ Project Structure

```
/Advanced-BMI-Tracker
├── BMI_Calculator.py  # Main application logic and Tkinter UI
├── requirements.txt   # List of required Python packages (Matplotlib)
└── README.md          # Project documentation (this file)
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\! Feel free to open an issue or submit a pull request.

```
```

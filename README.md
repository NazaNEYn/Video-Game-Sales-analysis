# Video Game Sales Trends Analyzer

This is a Python-based command-line tool that analyzes a dataset of video game sales to provide users with sales figures, search capabilities, and general insights into the video game market. It uses the **Pandas** library for efficient data handling and analysis.

---

## Key Features

* **Robust Game Search:** Users can search for any game or series (e.g., "Mario," "Call of Duty") and get a list of matching titles across different platforms. The search is **case-insensitive** and finds **partial matches** using `str.contains()`.
* **Total Sales Calculation:** For any game or series searched, the tool calculates and reports the **total global sales** (in millions).
* **Interactive Sorting:** Results can be sorted by release year or total global sales upon request.
* **Top 10 Global Sales List:** Users can quickly view the top 10 best-selling games across the entire dataset.
* **Efficient Data Handling:** Uses Pandas for fast data loading and cleaning, including converting the `Year` column to a proper numerical type (`Int64`).

---

## Prerequisites

This project requires Python and the Pandas library.

1.  **Python 3**
2.  **Pandas:** Install via pip:
    ```bash
    pip install pandas
    ```

---

## Dataset

The script is designed to work with a file named `vgsales.csv`. This file must contain the following required columns for the tool to function correctly:

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `Name` | String | The official title of the game. |
| `Platform` | String | The console/system the game was released on. |
| `Year` | Numerical (Can be mixed) | The year of release (must be cleaned to a number). |
| `Genre` | String | The game's primary genre. |
| `Publisher` | String | The company that published the game. |
| `Global_Sales` | Numerical | The total sales worldwide (in millions). |

---

## How to Run the Tool

1.  Save the provided Python code as `main.py`.
2.  Ensure the `vgsales.csv` file is in the same directory as the script.
3.  Run the script from your terminal:

    ```bash
    python main.py
    ```

4.  The script will immediately enter the interactive search loop, prompting you for a game name.

---

## How to Use the Interactive Search

The script runs in a loop, repeatedly asking for a game name.

1.  **Enter Game Name:** Type any part of a game or series name (e.g., `zelda` or `final fantasy`).
2.  **Review Results:** The script displays all matching titles.
3.  **Sort Option:** You are prompted to sort the displayed results by **Year (`Y`)** or **Global Sales (`GS`)**.
4.  **Sales Summary:** You are asked if you want to see the total sales for *all* matching games.
5.  **Exit:** If you say 'N' to the total sales prompt, the script will exit the search loop and terminate.

---

## Core Logic Highlights

The robust search and sales calculations are handled by the following key Pandas operations:

* **Case-Insensitive Partial Match:**
    ```python
    game_row = df[df["Name"].str.lower().str.contains(game_info_input)]
    ```
* **Total Sales Aggregation:**
    ```python
    total_sales = game_row["Global_Sales"].sum()
    ```
* **Top 10 Global Ranking:**
    ```python
    df.sort_values(by="Global_Sales", ascending=False).head(10)
    ```

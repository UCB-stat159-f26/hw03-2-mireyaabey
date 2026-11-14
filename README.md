# HW03 — Tennis Career Analysis

**Author:** Mireya Abeywardane
**Course:** STAT 159 — UC Berkeley, Fall 2026  
**Project Start Date:** November 5, 2026

## Overview

This project uses publicly available match data from Tennis Abstract to visualize and evaluate professional tennis player career matches for both genders. 

The assignment is comprised of two main functions. The purpose of the first function is to extract and process a player's match data in order to determine match dates, results, opponents, and ages. The second function is used to create a scatter plot with the player's age on the x-axis, the age difference between the player and their opponent on the y-axis, and blue and purple points depicting wins and losses, respectively. Each dot on the plot represents a win or a loss: the blue dots are match wins and the purple dots are match losses.

Although the Tennis Abstract stores match data differently for male and female tennis players, the package works with both male and female tennis players. The visualizations were implemented using Python, Pandas, and Matplotlib, following the style of the New York Times visualization used in homework 2.

## Software and Dependencies

This project was developed using UC Berkeley DataHub (2026) with the following software and Python libraries:

- Python: 3.14.7
- Pandas: 3.0.6
- NumPy: 2.4.6
- Matplotlib: 3.11.2
- Requests: Version not verified
- Pytest: Version not verified
- JupyterLab

The dependencies required to reproduce this project are listed in pyproject.toml.

## Repository Structure

```text
hw03/
├── tennis_career/
│   ├── __init__.py
│   ├── data.py
│   ├── cleaning.py
│   ├── career_matches.py
│   └── plotting.py
│
├── tests/
│   ├── __init__.py
│   ├── test_cleaning.py
│   ├── test_data.py
│   ├── test_plotting.py
│   └── test_career_matches.py
│
├── figures/
│   ├── serena_plot.png
│   └── nadal_plot.png
│
├── pyproject.toml
├── README.md
├── instructions.md
└── .gitignore
```

`tennis_career/` — Python package containing the functions used to retrieve, clean, process, and visualize tennis match data.

`tests/` — Tests that were used to check each function created in the tennis career package.

`figures/` — Example visualizations of Serena Williams's and Rafael Nadal's career matches (format: PNG).

`pyproject.toml` — Package configuration and Python dependencies.

`README.md` — Project overview, installation instructions, usage examples, and reflections.

`.gitignore` — Directories and files absent from version control.

## Installation

Install the package directly from Github using the following command:

```bash
pip install git+https://github.com/UCB-stat159-f26/hw03-2-mireyaabey.git
```

Otherwise, you can install the package locally by cloning or downloading the Git repository:

```bash
git clone https://github.com/UCB-stat159-f26/hw03-2-mireyaabey.git
cd hw03-2-mireyaabey
pip install -e .
```

## Usage

The package is comprised of two main functions: load_career_data() and plot_tennis_career_matches().

The load_career_data() function fetches and processes the player's match data from the Tennis Abstract. The data is then organized into a Pandas dataframe. The relevant information is extracted, including match dates, opponents, and results. It also calculates the player's age, their opponent's age, and the age difference between them at each match automatically. The function is designed to work with both male and female tennis players.

The plot_tennis_career_matches() function creates a scatter plot using the processed data where the wins and losses are separated by color. 

## Example 1: Serena Williams

```python
from tennis_career import load_career_data, plot_tennis_career_matches

serena = load_career_data("Serena Williams")
fig = plot_tennis_career_matches(serena)
fig.savefig("serena_plot.png")
```

## Example 2: Rafael Nadal

```python
from tennis_career import load_career_data, plot_tennis_career_matches

nadal = load_career_data("Rafael Nadal")
fig = plot_tennis_career_matches(nadal)
fig.savefig("nadal_plot.png")
```
Different players can be used within the same function without altering the underlying code.

## Testing

The functionality of the package was tested using automated tests implemented using Pytest. The tests span across data cleaning, plotting, name formatting for players, invalid player name inputs, and career match data processing. The tests are able to run without accessing the Tennis Abstract because network requests were simulated during testing. 

In order to test the package, enter the repository directory in the terminal and run:
```bash
python -m pytest -v
```

All 10 tests passed in the development of the assignment. 

## Data Source

Tennis Abstract: https://www.tennisabstract.com/

The original career match data comes from Tennis Abstract's publicly available JavaScript files. The files include: various player statistics, dates, opponents, wins, losses, and other subsequent match information. 

The package retrieves the data, converts the relevant information into a Pandas DataFrame, and calculates the ages needed to reproduce the visualization.

## Reproduce

To reproduce the visualizations:

1. Download or clone this repository.

2. Access the project using a Python environment or JupyterLab.

3. Install the package and required dependencies using pip install -e ..

4. Import load_career_data() and plot_tennis_career_matches().

5. Enter the name of a player to retrieve their career match data.

6. Use the plotting function to generate the scatter plot.

7. Save the resulting figure as a PNG file if desired.

The example visualizations are stored in the figures/ directory.

## Reflections

This assignment taught me the value of creating a reusable package rather than randomized scripts that are difficult to follow. I found that my system for constructing functions and making changes was much more organized. This also made it easier to make more consistent commits because I was no longer bound to a lengthy script. I also realized the importance of testing when creating many different functions at a time. It was common for my tests to point me to problems within my functions, which made troubleshooting errors a much faster process. The tests were a great way to track my progress as well. They made great checkpoints to refer back to when I made changes to certain functions. 

A challenge I encountered on this assignment was understanding the differences in genders within the Tennis Abstract. I initially found difficulty finding Serena William's birth date because I was searching for it in the wrong file and did not account for differences in how the variable was written. I was able to manually look through the JavaScript files to determine what I was doing wrong and modified my code accordingly. Overall, this assignment taught me how to solve problems and to approach coding in a more organized way. 



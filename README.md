
# README: Web Scraping

## Summary

This code takes in a website provided and performs click events to scrape all the cast information. The gathered information is organized and sorted into respective CSV tables, including Person, Character, and Plays. Prior information from Person-writer&director - Sheet1.csv is also formatted and added to the CSV tables.

## Full Description

This code takes in the IMDB website provided and performs click events to reveal hidden information on the website. The revealed information includes the titles of the episodes the cast member worked on. The collected data includes cast member's name (first and last), character's name (first and last), job title, and the episode titles the cast member worked on. The episode titles are compared to Episode - Sheet1.csv to obtain season and episode numbers. The information is then organized and sorted into Person, Character, and Plays CSV files.

### CSV Files:

- **Person CSV:** personid, season number, episode number, first name, last name, and job title.
- **Character CSV:** character Id, first name, and last name.
- **Plays CSV:** plays Id, cast member first name, cast member last name, character first name, character last name, and job title.

Additionally, previously gathered information from Person-writer&director - Sheet1.csv is formatted, and the formatted information is added to the CSV Person.

## Used

- **Language:** Python
- **Website:** [IMDb - Parks and Recreation](https://www.imdb.com/title/tt1266020/fullcredits)

## Installation

Install the required libraries:

```bash
pip install BeautifulSoup
pip install selenium
```

## Needed Files

- **Person-writer&director - Sheet1.csv**
- **Episode - Sheet1.csv**

## How to Use

When you run the code, it will give you three prompts, all related to file paths.

1. The first one will tell you to “Enter the file path where you want the csv.” All that needs to be typed is the path to where you want the CSV files to go. For example: `/User/path/destination`.

2. The next one will tell you to “Enter Person-writer&director - Sheet1.csv file path:'' when you download Person-writer&director, get its file path, and enter it for this prompt. For example: `/User/path/path/Person-writer&director - Sheet1.csv`.

3. Finally, this one will tell you to “Enter Downloads/Episode - Sheet1.csv file path:” when you download Downloads/Episode, get its file path, and enter it for this prompt. For example: `/User/path/path/Downloads/Episode - Sheet1.csv`.

### Dependencies

- **BeautifulSoup:** Library for pulling data out of HTML and XML files.
- **Selenium:** Open-source framework for automating web browsers.

### Troubleshooting:

- The window that appears may cause issues. Clicking anything inside the window while it’s running will cause an error. It is recommended to keep your cursor away from the window while it is running.
- The file paths may cause issues. In the first prompt, the example `/User/path/destination` is given. Like the prompts say, it is suggested to follow the example formats. In the first prompt, if there is a `/` after destination (like `/User/path/destination/`), then there will be errors.

## Acknowledgments

- **Selenium:** Developed by Jason Huggins.
- **BeautifulSoup:** Developed by Leonard Richardson

## Final Notes

If expanded upon and refined more, this code could be used for not just scraping IMDB data but also other sites. This expansion could improve quality since there would be more data to compare. Ultimately, this scraping if expanded upon could help movie fans have quick and easy access to all the information related to their favorite shows.

---

# README: Data Preparation for Database

## Viewers Data

The code in this section combines information from two CSV files (`parks_and_rec_imdb.csv` and `parks_and_rec_episodes.csv`) related to the "Parks and Recreation" TV show. It specifically focuses on IMDb ratings, total votes, and US viewers data.

### Code Explanation:

1. **Data Source:** The CSV files can be accessed on Kaggle:
   - IMDb Data: [Parks and Recreation IMDb Data](https://www.kaggle.com/datasets/USERNAME/parks-and-recreation-imdb-data)
   - Episode Data: [Parks and Recreation Episodes Data](https://www.kaggle.com/datasets/USERNAME/parks-and-recreation-episodes-data)

2. **Usage:**
   - Replace the file paths (`imdb_csv_path` and `episode_data_csv_path`) with the actual paths to your downloaded CSV files.
   - Run the code to generate the `Viewers_data.csv` file.

## Episode Data

This section extracts specific attributes from the `parks_and_rec_imdb.csv` file to create a new CSV file containing essential episode information.

### Code Explanation:

1. **Data Source:** The IMDb CSV file can be accessed on Kaggle: [Parks and Recreation IMDb Data](https://www.kaggle.com/datasets/USERNAME/parks-and-recreation-imdb-data)

2. **Usage:**
   - Replace the file path (`csv_file_path`) with the actual path to your downloaded IMDb CSV file.
   - Run the code to generate the `episode_data.csv` file.

## Transcripts Data

This repository contains CSV files with transcripts data extracted from web archives. The data is ready for use and does not require any preprocessing steps.

### Files
- **transcripts folder:** Include CSV files containing the transcripts data.

### Usage

1. **Download the Data:**
   - You can download the CSV file from [Parks and Recreation Scripts](https://www.kaggle.com/datasets/heheheluke/parks-and-recreation-scripts).

2. **Data Fields:**
   - The CSV file includes the following fields: Character and dialogue.

3. **Data Exploration:**
   - You can explore the data directly using tools like pandas in Python, Excel, or any other data analysis tool.

## Person Data

This code processes a CSV file (`merged_output_file.csv`) containing information about people involved in the "Parks and Recreation" show, specifically focusing on names and job titles.

### Code Explanation:

1. **Data Source:** The merged CSV file can be created using IMDb and episode data.

2. **Usage:**
   - Replace the file path (`csv_file_path`) with the actual path to your merged CSV file.
   - Run the code to generate the `Person.csv` file.

---

# README: Extraction

## Introduction

This Python script is designed to scrape information about the cast and crew of a TV show from IMDb, specifically focusing on the TV show with the IMDb ID 'tt1266020'. The script extracts data such as person names, character names, season and episode information, and job titles.

### Dependencies

Before running the script, make sure you have the necessary dependencies installed. You can install them using the following commands:

```bash
pip install beautifulsoup4
pip install requests
pip install selenium
```

Additionally, you need to download the appropriate WebDriver for Selenium. In this script, it uses the Chrome WebDriver. Download it from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/) and ensure the

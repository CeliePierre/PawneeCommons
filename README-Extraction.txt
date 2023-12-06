README-Extraction


Introduction


This Python script is designed to scrape information about the cast and crew of a TV show from IMDb, specifically focusing on the TV show with the IMDb ID 'tt1266020'. The script extracts data such as person names, character names, season and episode information, and job titles.


Dependencies


Before running the script, make sure you have the necessary dependencies installed. You can install them using the following commands:
'''bash
pip install beautifulsoup4
pip install requests
pip install selenium
'''
Additionally, you need to download the appropriate WebDriver for Selenium. In this script, it uses the Chrome WebDriver. Download it from [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/) and ensure the executable is in your system's PATH.


Usage


1. Open the script ('imdb_scraper.py') in a text editor.


2. Update the file paths for the destination CSV file ('destination_csv_path'), episode CSV file ('file_path_epsode'), and other CSV files ('file_path_Person', 'file_path_Character', 'file_path_Plays') according to your system paths.


3. Run the script:


    '''bash
    python imdb_scraper.py
    '''


4. The script will launch a Chrome browser, navigate to the IMDb page of the TV show ('tt1266020'), and extract relevant information about the cast and crew.


5. The scraped data will be stored in the specified CSV files.




Structure


The script consists of the following main functions:


- 'splitup(text, var)': A utility function to split first and last names from text.


- 'get_episode_info(title, file_path_epsode)': Function to retrieve season and episode information based on the episode title.


- 'main()': The main function that orchestrates the entire scraping process.


CSV Output


The script generates four CSV files:


1. 'Person.csv': Contains information about individuals involved in the TV show, including person ID, season number, episode number, first name, last name, and job title.


2. 'Character.csv': Contains information about characters in the TV show, including character ID, first name, and last name.


3. 'Play.csv': Represents relationships between characters and actors, including character ID, actor's first name, actor's last name, character's first name, character's last name, and job title.


4. 'destination_csv_path' (customizable): Appends information from the original CSV file with additional data collected during scraping.


Notes


- The script uses BeautifulSoup for parsing HTML and Selenium for dynamic interactions with the IMDb website.


- Ensure that you comply with IMDb's terms of service and robots.txt when using this script for scraping.


- Customize the file paths and IMDb ID as needed for different TV shows.


- Adjust the sleep times based on the performance of your system and internet speed.
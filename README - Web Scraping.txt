Web Scraping 

Summary 

This code takes in a website provided and performs click events. To scrape all the cast information. This information is then organized and sorted into their respective CSV tables. Previously gathered information from Person-writer&director - Sheet1.csv is also formatted and added to the CSV tables. 

Full Description 

This code takes in the IMDB website provided and performs click events. These click events open up hidden information on the website. The information that should be revealed is the titles of the episodes the cast member worked on. With the new information revealed it can be scraped and parsed. The information that should be collected is the cast member's name first and last, the character's name first and last, the job title, and the episode titles the cast member worked on. The episode title is then compared to Episode - Sheet1.csv to get the season number and episode number. This information is then organized and sorted into their respective CSV files Person, Character, and Plays. 

What is the CSV files: 

- Person CSV: personid, season number, episode number, first name, last name, and job title. 

- Character CSV: character Id, first name, and last name 

- Plays CSV: plays Id, cast member first name, cast member last name, character first name, character last name, and job title. 

Since Plays is a relationship between the entities' Person and Character it connects their information. The previously gathered information from Person-writer&director - Sheet1.csv is also formatted. The formatting is the separating first name and last name. After formatting the information is then added to the CSV Person. 


Used 
● Language: python 
● Website: https://www.imdb.com/title/tt1266020/fullcredits 


Installation 
Install the required libraries: 
```bash 
pip install BeautifulSoup 
pip install selenium


Needed Files 
● Person-writer&director - Sheet1.csv 
● Episode - Sheet1.csv 


How to Use 

When you run the code it will give you three prompts all of them relating to file paths. - The first one will tell you to “Enter the file path where you want the csv:”. All that needs to be typed is the path to where you want the CSV files to go. For example: /User/path/destination 

- The next one will tell you to “Enter Person-writer&director - Sheet1.csv file path:'' when you download Person-writer&director get its file path and enter it for this prompt. For example: /User/path/path/Person-writer&director - Sheet1.csv 

- Finally, this one will tell you to “Enter Downloads/Episode - Sheet1.csv file path:” when you download Downloads/Episode get its file path and enter it for this prompt. For example: /User/path/path/Downloads/Episode - Sheet1.csv 


Dependencies 

● BeautifulSoup: Library for pulling data out of HTML and XML files 
	○ Selenium was used for pulling data out of HTM files. 
● selenium: Open-source framework for automating web browsers 
	○ Selenium was used for simulating click events. more information on selenium click can be viewed here. 


Troubleshooting: 

The window that appears may cause issues. There is a window that will appear to perform click events. Clicking anything inside the window while it’s running will cause an error. It is recommended to keep your cursor away from the window while it is running. 

The file paths may cause issues. In the first prompt, the example /User/path/destination is given. Like the prompts say It is suggested to follow the example formats. In the first prompt If there is a / after destination (like /User/path/destination/) then there will be errors. 


Acknowledgments 

● Selenium - Developed by Jason Huggins. 
● BeautifulSoup - Developed by Leonard Richardson


Final Notes 

This scraping if expanded upon and refined more this code could be used for not just scraping IMDB data but also other sites. This expansion could improve quality since there would be more data to compare. Ultimately this scraping if expanded upon could help movie fans have quick and easy access to all the information related to their favorite shows.

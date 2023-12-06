from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


#splits up first and last name
def splitup(text,var):
  #spliting first and lastname
  char_text = str(text).replace("\n",",")
  split_string = char_text.split(',')
  char = split_string[var].strip()
  split_first= char.split()
  First_name = split_first[0]
  Last_name = split_first[-1]
  if (First_name == Last_name):
            Last_name = ""
  return First_name, Last_name

def get_episode_info(title, file_path_epsode):
   with open(file_path_epsode, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
         if row['title'] == title:
            # Match found, print or return the desired information
            season = row['season']
            episode_num_in_season = row['episode_num']
            return season,episode_num_in_season
      else:
         return "",""
         
def main():
  #file paths
  list = []
  destination_csv_path = '/Users/s_7_24/Downloads/Person-writer&director - Sheet1.csv'
  file_path_epsode = '/Users/s_7_24/Downloads/Episode - Sheet1.csv'
  file_path_Person = '/Users/s_7_24/Python/Cos 457/Person.csv'
  file_path_Character = '/Users/s_7_24/Python/Cos 457/Character.csv'
  file_path_Plays = '/Users/s_7_24/Python/Cos 457/Play.csv'

  
  #accessing/parsing website
  url = 'https://www.imdb.com/title/tt1266020/fullcredits'
  soup = BeautifulSoup(requests.get(url).content, 'html.parser')

  #opening website
  driver = webdriver.Chrome()  
  driver.get('https://www.imdb.com/title/tt1266020/fullcredits')
  time.sleep(10)

  #counting all instances in of Cast 
  count_all = soup.find_all('tr',class_=["even","odd"])

  #Simulating a click event
  #942
  half = (len(count_all)/2)
  num = 2
  # int(half)
  for i in range(0,int(half)):
   if num == 1442:
      num = 1443
   if num  == 1717:
      link_selector = '//*[@id="fullcredits_content"]/table[3]/tbody/tr[1717]/td[4]/a'
   else:
    link_selector = '//*[@id="fullcredits_content"]/table[3]/tbody/tr['+ str(num) +']/td[4]/a[2]'
   #10000
   link_element = WebDriverWait(driver, 10000).until(
   EC.element_to_be_clickable((By.XPATH,link_selector))
   )
   if link_element:
   #time.sleep(0.3)
    link_element.click()
    num += 2
  
  #Parseing new information
  time.sleep(15)
  html_content = driver.page_source
  soupex = BeautifulSoup(html_content, 'html.parser')
  div = soupex.find_all("div")

  #Person colum lables in csv
  with open(file_path_Person, 'w', newline='', encoding='utf-8') as csvfile:
       csvfile.write("PersonID" + "\t"+"Season Number"+ "\t"+"Episode number"+"\t"+"First name" + "\t" +
                      "Last name" + "\t"+"Job title" + "\n")
  #Character colum lables in csv
  with open(file_path_Character, 'w', newline='', encoding='utf-8') as csvfile:
       csvfile.write("CharacterID" + "\t"+"First name" + "\t" +
                      "Last name" + "\n")
   
  #Plays (relationship) colum lables in csv
  with open(file_path_Plays, 'w', newline='', encoding='utf-8') as csvfile:
       csvfile.write("CharacterID" + "\t"+"Actor First Name" + "\t" +
                      "Actor Last name" + "\t" +"Character First name" + 
                      "\t" +"Character Last name" + "\t" +"Job Title " +"\n")

  #setup
  IDnum = 0
  count_all = soupex.find_all('tr',class_=["even","odd"])
  for row in count_all:
   #Actor name
   next_row = row.find_all('td', {'colspan': '4'})
   if not next_row:
    actor_nm = row.find('td',class_=False) 
    if actor_nm:
      act = actor_nm.find('a').text.strip()
      act_first_name, act_last_name = splitup(act,0)

   #Character name
   character_name = row.find('td', class_='character')
   if character_name:
           #ID number
           IDnum += 1
           char = character_name.find('a').text.strip()
           char_first_name, char_last_name = splitup(char,0)
           with open(file_path_Character, 'a', newline='', encoding='utf-8') as csvfilechar:
            csvfilechar.write("" + str(IDnum) + "\t" + char_first_name + "\t" +
                      char_last_name + "\n")
   #Epsode Titles
   if next_row:
      for somthing in next_row:
         td_elements = somthing.find_all('div', class_="filmo-episodes")
         if td_elements:
            Title_contents = [td.get_text(strip=True) for td in td_elements]
         else:
            Title_contents = []
      for T_content in Title_contents:
         Title = (((str(T_content).replace("-","",1)).replace("(",",")).split(','))[0].strip()
         #match titles to get season num and epsiode num
         season,ep_num = get_episode_info(Title, file_path_epsode)
         with open(file_path_Person, 'a', newline='', encoding='utf-8') as csvfile:
          csvfile.write("" +str(IDnum) + "\t"+ season + "\t" +
                      ep_num + "\t"+ act_first_name + "\t"+ act_last_name +"\t"+ "Cast" +"\n")
      #Plays(relationship)
      with open(file_path_Plays, 'a', newline='', encoding='utf-8') as csvfile:
       csvfile.write(str(IDnum) + "\t"+ act_first_name + "\t" +
                      act_last_name + "\t" + char_first_name + 
                      "\t" + char_last_name + "\t" + "Cast" +"\n")
 
  #combining information from prevously collected cvs with new information
  with open(destination_csv_path, 'r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for drow in csv_reader:
         IDnum += 1
         dseason = drow['season']
         episode_num_in_season = drow['episode_num_in_season']
         job_title = drow['job title ']
         person_name = drow['person name and family']
         if "&" in person_name:
            split_pname = (person_name.replace(" & ", ",")).split(",")
            for split_n in split_pname:
               first, last = splitup(split_n,0)
               with open(file_path_Person, 'a', newline='', encoding='utf-8') as csvfile:
                  csvfile.write("" +str(IDnum) + "\t"+ dseason + "\t" +
                     episode_num_in_season + "\t"+ first + "\t"+ last +"\t"+ job_title +"\n")
         else: 
            split_pname = person_name
            first, last = splitup(split_n,0)
            with open(file_path_Person, 'a', newline='', encoding='utf-8') as csvfile:
               csvfile.write("" +str(IDnum) + "\t"+ dseason + "\t" +
                      episode_num_in_season + "\t"+ first + "\t"+ last +"\t"+ job_title +"\n")

   

if __name__ == "__main__":
 main()
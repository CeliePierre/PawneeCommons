"""
Célie Pierre
COS 457 Database Systems
Database Systems Project Part 2
November 20, 2023

File: import_data_to_sql.py
"""

import csv
import os

import mysql.connector
import json
from datetime import datetime

"""
The methods read_[name] take in a file_path and a dictionary of tuples
It then reads in the .csv file associates with that table, extracts the data,
adds the data to the dictionary, then returns the dictionary
"""


def read_character(file_path, dic_tuples_charactr):
    # Table: charactr: cID, cFirstName, cLastName
    # File: CharacterID, First name, Last name
    print("Reading: " + os.path.basename(file_path))
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            cID = row[0]
            firstName = row[1]
            lastName = row[2]
            if not lastName:
                lastName = None
            if len(cID) < 4:
                cID = '{:04d}'.format(int(cID))
            dic_tuples_charactr[cID] = (cID, firstName, lastName)
    print("Successfully read: " + os.path.basename(file_path))
    return dic_tuples_charactr


def read_person(file_path, dic_tuples_person, dic_tuples_works):
    # Table 1: person: pID, firstName, lastName
    # Table 2: works: pID, eID, job
    # File: PersonID, Season #, Episode #, First name, Last name, Job title
    print("Reading: " + os.path.basename(file_path))
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csv_reader)
        wID = 1
        for row in csv_reader:
            # Get People table info
            pID = row[0]
            firstName = row[3]
            lastName = row[4]
            if not lastName:
                lastName = None
            if len(pID) < 4:
                pID = '{:04d}'.format(int(pID))
            # Get Works table info
            season = row[1]
            episode = row[2]
            if not season:
                season = None
                episode = None
                eID = None
            else:
                if len(episode) < 2:
                    episode = '{:02d}'.format(int(episode))
                eID = "s" + season + "e" + episode
            job = row[5]
            if pID not in dic_tuples_person:
                dic_tuples_person[pID] = (pID, firstName, lastName)
            if wID:
                dic_tuples_works[wID] = (pID, eID, job, wID)
                wID += 1
    print("Successfully read: " + os.path.basename(file_path))
    return dic_tuples_person, dic_tuples_works


def read_plays(file_path, dic_tuples_plays):
    # Table 1: plays: cID, cFirstName, cLastName, pID, pFirstName, pLastName
    # File: CharacterID, Actor First Name, Actor Last name, Character First name, Character Last name, Job Title
    print("Reading: " + os.path.basename(file_path))
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            # Get Character info
            cID = row[0]
            cFirstName = row[3]
            cLastName = row[4]
            if not cLastName:
                cLastName = None
            if len(cID) < 4:
                cID = '{:04d}'.format(int(cID))
            # Get Person info
            pID = None
            pFirstName = row[1]
            pLastName = row[2]
            if not pLastName:
                pLastName = None
            dic_tuples_plays[cID] = (cID, cFirstName, cLastName, None, pFirstName, pLastName)
    print("Successfully read: " + os.path.basename(file_path))
    print("Successfully read: " + os.path.basename(file_path))
    return dic_tuples_plays


def read_episode(file_path, dic_tuples_episode):
    # Table 1: episode: eID, season, epNum, title, airDate, descript
    # File: season, episode_num, title, original_air_date, desc, us_viewers
    print("Reading: " + os.path.basename(file_path))
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            season = row[0]
            episode = row[1]
            if not season:
                season = None
                episode = None
                eID = None
            else:
                if len(episode) < 2:
                    episode = '{:02d}'.format(int(episode))
                eID = "s" + season + "e" + episode
            title = row[2]
            airDate = row[3]
            airDate = datetime.strptime(airDate, '%m/%d/%Y')
            descript = row[4]
            dic_tuples_episode[eID] = (eID, season, episode, title, airDate, descript)
    print("Successfully read: " + os.path.basename(file_path))
    return dic_tuples_episode


def read_viewers(file_path, dic_tuples_viewers, dic_tuples_views):
    # Table 1: viewers: vID, rating, votes, viewers
    # Table 2: views: vID, eID
    # File: season, episode_num, imdb_rating, total_votes, us_viewers
    print("Reading: " + os.path.basename(file_path))
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csv_reader)
        for row in csv_reader:
            season = row[0]
            episode = row[1]
            if not season:
                season = None
                episode = None
                eID = None
            else:
                if len(episode) < 2:
                    episode = '{:02d}'.format(int(episode))
                eID = "s" + season + "e" + episode
            vID = eID
            rating = row[2]
            votes = row[3]
            viewers = row[4]
            if vID:
                dic_tuples_viewers[vID] = (vID, rating, votes, viewers)
                dic_tuples_views[vID] = (vID, eID)
    print("Successfully read: " + os.path.basename(file_path))
    return dic_tuples_viewers, dic_tuples_views


def read_transcripts(t_directory, dic_tuples_transcripts, dic_tuples_says, dic_tuples_scripts):
    # Table 1: transcripts: lID, lineNum, dialogue
    # Table 2: says: lID, eID, cID, cName
    # Table 3: scripts: eID, lID
    # File: character, line
    os.chdir(t_directory)
    print("Reading: transcripts...")
    for csv_file in os.listdir(t_directory):
        with open(csv_file, newline='', encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            #print(file_path)
            next(csv_reader)
            lineCtr = 1
            if csv_file != "desktop.ini":
                for row in csv_reader:
                    cName = row[0]
                    if not cName:
                        season = 'Unknown'
                    dialogue = row[1]
                    eID = os.path.basename(csv_file)
                    eID = eID.replace(".csv", "")
                    # Line ID Format: s01e01-001 (season 01, episode 01, line 001)
                    lineNum = '{:03d}'.format(int(lineCtr))
                    lID = eID + "-" + lineNum
                    dic_tuples_transcripts[lID] = (lID, lineNum, dialogue)
                    dic_tuples_says[lID] = (lID, eID, None, cName)
                    dic_tuples_scripts[eID] = (eID, lID)
                    lineCtr += 1
    print("Successfully read: transcripts")
    return dic_tuples_transcripts, dic_tuples_says, dic_tuples_scripts


def insert_table(directory, config_file, charactr_info, person_info, episode_info,
                 transcripts_info, viewers_info, plays_info, works_info, views_info,
                 scripts_info, says_info):
    """
    This method takes in the directory, SQL configuration file, and info for each table.
    It then passes the info into their associated methods to get data from their associates CSV files.
    It then inserts that data into SQL.
    """
    with open(config_file, "r") as f:
        config = json.load(f)
    connection_config = config["mysql"]
    data_base = mysql.connector.connect(**connection_config)

    # preparing a cursor object
    cursor_object = data_base.cursor()
    dic_tuples_charactr = {}
    dic_tuples_person = {}
    dic_tuples_episode = {}
    dic_tuples_transcripts = {}
    dic_tuples_plays = {}
    dic_tuples_works = {}
    dic_tuples_viewers = {}
    dic_tuples_views = {}
    dic_tuples_scripts = {}
    dic_tuples_says = {}

    for csv_file in os.listdir(directory):
        # Charactr table
        if csv_file == charactr_info[0]:
            dic_tuples_charactr = read_character(directory + csv_file, dic_tuples_charactr)
            for cID in dic_tuples_charactr:
                cursor_object.execute("INSERT INTO pawneecommons."+charactr_info[1]+" (cID, cFirstName, cLastName)"
                                      "values (%s, %s, %s)", (dic_tuples_charactr[cID]))
            data_base.commit()
            print("Successfully imported: " + csv_file)

        # Episode table
        if csv_file == episode_info[0]:
            dic_tuples_episode = read_episode(directory + csv_file, dic_tuples_episode)
            for eID in dic_tuples_episode:
                cursor_object.execute("INSERT INTO pawneecommons."+episode_info[1]+" (eID, season, episode, title, airDate, descript)"
                                      "values (%s, %s, %s, %s, %s, %s)", (dic_tuples_episode[eID]))
            data_base.commit()
            print("Successfully imported: " + csv_file)

        # Person and Works tables
        if csv_file == person_info[0]:
            dic_tuples_person_works = read_person(directory + csv_file, dic_tuples_person, dic_tuples_works)
            dic_tuples_person = dic_tuples_person_works[0]
            dic_tuples_works = dic_tuples_person_works[1]
            for pID in dic_tuples_person:
                cursor_object.execute("INSERT INTO pawneecommons."+person_info[1]+" (pID, pFirstName, pLastName)"
                                      "values (%s, %s, %s)", (dic_tuples_person[pID]))
            data_base.commit()
            print("Successfully imported: " + csv_file + " (1 of 2)")
            for wID in dic_tuples_works:
                works_values = dic_tuples_works[wID]
                cursor_object.execute("INSERT INTO pawneecommons."+works_info[1]+" (pID, eID, job)"
                                      "values (%s, %s, %s)", (works_values[:-1]))
            data_base.commit()
            print("Successfully imported: " + csv_file + " (2 of 2)")

        # Plays table
        if csv_file == plays_info[0]:
            dic_tuples_plays = read_plays(directory + csv_file, dic_tuples_plays)
            for cID in dic_tuples_plays:
                cursor_object.execute("INSERT INTO pawneecommons."+plays_info[1]+" (cID, cFirstName, cLastName, pID, pFirstName, pLastName)"
                                      "values (%s, %s, %s, %s, %s, %s)", (dic_tuples_plays[cID]))
            data_base.commit()
            print("Successfully imported: " + csv_file)

        # Viewers and Views tables
        if csv_file == viewers_info[0]:
            dic_tuples_viewers_views = read_viewers(directory + csv_file, dic_tuples_viewers, dic_tuples_views)
            dic_tuples_viewers = dic_tuples_viewers_views[0]
            dic_tuples_views = dic_tuples_viewers_views[1]
            for vID in dic_tuples_viewers:
                cursor_object.execute("INSERT INTO pawneecommons."+viewers_info[1]+" (vID, rating, votes, viewers)"
                                      "values (%s, %s, %s, %s)", (dic_tuples_viewers[vID]))
            data_base.commit()
            print("Successfully imported: " + csv_file + " (1 of 2)")
            for vID in dic_tuples_views:
                cursor_object.execute("INSERT INTO pawneecommons."+views_info[1]+" (vID, eID)"
                                      "values (%s, %s)", (dic_tuples_views[vID]))
            data_base.commit()
            print("Successfully imported: " + csv_file + " (2 of 2)")

    # Transcripts and Says tables
    # Table 1: transcripts: lID, lineNum, dialogue
    # Table 2: says: cID, cName, lID, eID
    dic_tuples_transcripts_says = read_transcripts(transcripts_info[0], dic_tuples_transcripts, dic_tuples_says, dic_tuples_scripts)
    dic_tuples_transcripts = dic_tuples_transcripts_says[0]
    dic_tuples_says = dic_tuples_transcripts_says[1]
    dic_tuples_scripts = dic_tuples_transcripts_says[2]
    for lID in dic_tuples_transcripts:
        cursor_object.execute("INSERT INTO pawneecommons."+transcripts_info[1]+" (lID, lineNum, dialogue)"
                              "values (%s, %s, %s)", (dic_tuples_transcripts[lID]))
    data_base.commit()
    print("Successfully imported: " + "transcripts" + " (1 of 3)")
    for lID in dic_tuples_says:
        cursor_object.execute("INSERT INTO pawneecommons."+says_info[1]+" (lID, eID, cID, cName)"
                              "values (%s, %s, %s, %s)", (dic_tuples_says[lID]))
    data_base.commit()
    print("Successfully imported: " + "transcripts" + " (2 of 3)")
    for eID in dic_tuples_scripts:
        cursor_object.execute("INSERT INTO pawneecommons."+scripts_info[1]+" (eID, lID)"
                              "values (%s, %s)", (dic_tuples_scripts[eID]))
    data_base.commit()
    print("Successfully imported: " + "transcripts" + " (2 of 3)")
    cursor_object.close()


# begin main

print("Starting imports...")
find_directory = os.path.dirname(os.path.abspath(__file__))
path_to_data_dir = os.path.join(find_directory, "data\\")
os.chdir(path_to_data_dir)

# Tables
charactr_table = "charactr"
person_table = "person"
episode_table = "episode"
transcripts_table = "transcripts"
viewers_table = "viewers"
plays_table = "plays"
works_table = "works"
views_table = "views"
scripts_table = "scripts"
says_table = "says"

# .csv files
charactr_file = "charactr_data.csv"
person_file = "person_data.csv"
episode_file = "episode_data.csv"
transcripts_file = os.path.join(find_directory, "data\\transcripts\\")
viewers_file = "viewers_data.csv"
works_file = person_file
views_file = viewers_file
scripts_file = transcripts_file
plays_file = "plays_data.csv"
says_file = "says_data.csv"

# Tables + csv files
charactr_info = [charactr_file, charactr_table]
person_info = [person_file, person_table]
episode_info = [episode_file, episode_table]
transcripts_info = [transcripts_file, transcripts_table]
viewers_info = [viewers_file, viewers_table]
plays_info = [plays_file, plays_table]
works_info = [works_file, works_table]
views_info = [views_file, views_table]
scripts_info = [transcripts_file, scripts_table]
says_info = [says_file, says_table]

insert_table(path_to_data_dir, "connectorConfig.json", charactr_info,
             person_info, episode_info, transcripts_info,
             viewers_info, plays_info, works_info, views_info,
             scripts_info, says_info)
print("Imports complete.")

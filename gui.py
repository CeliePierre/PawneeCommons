"""
Célie Pierre
COS 457 Database Systems
Database Systems Project Part 3
December 4, 2023

File: gui.py
"""

import mysql.connector
import PySimpleGUI as sg
import json
import trigger
import os
import sentencesearcher


# Connect to MySQL Database
def get_database_connection():
    config_file = "config.json"
    with open(config_file, "r") as f:
        config = json.load(f)
    connection_config = config["mysql"]
    conn = mysql.connector.connect(**connection_config)
    return conn


# Takes in user input and passes into MySQL procedure
def get_procedure(conn, proc_name, proc_param):
    cursor = conn.cursor(dictionary=True)
    cursor.callproc(proc_name, proc_param)
    results = []
    for result in cursor.stored_results():
        rows = result.fetchall()
        for row in rows:
            results.append(row)
    cursor.close()
    return results


def get_procedure2(conn, proc_name):
    cursor = conn.cursor(dictionary=True)
    cursor.callproc(proc_name)
    results = []
    for result in cursor.stored_results():
        rows = result.fetchall()
        for row in rows:
            results.append(row)
    cursor.close()
    return results


def get_table(conn, table_name):
    cursor = conn.cursor(dictionary=True)
    select_command = f"SELECT * FROM {table_name};"
    cursor.execute(select_command)
    result = cursor.fetchall()
    cursor.close()
    return result


def get_query(conn, custom_query):
    cursor = conn.cursor(dictionary=True)
    select_command = f"{custom_query};"
    cursor.execute(select_command)
    result = cursor.fetchall()
    cursor.close()
    return result


def make_browse_layout(conn, table_name):
    headings = []
    data = []
    mysql_table = get_table(conn, table_name)
    if mysql_table:
        headings = list(mysql_table[0].keys())
        data = [list(row.values()) for row in mysql_table]
    if table_name == 'episode':
        columns_to_display = [1, 2, 3]
        display_headings = [list(mysql_table[0].keys())[col] for col in columns_to_display]
        display_data = [[row[col] for col in columns_to_display] for row in data]
        table = [
            [sg.Text(f'Browsing {table_name}. Click on an episode for more information.')],
            [sg.Table(values=display_data, headings=display_headings, max_col_width=25,
                      auto_size_columns=True, display_row_numbers=False,
                      justification='left', num_rows=10, enable_events=True,
                      row_height=25, key=f'-{table_name.upper()} TABLE-')]
        ]
    elif table_name == 'transcripts':
        mysql_query = get_query(conn, 'select S.cName, T.dialogue '
                                      'from transcripts as T join says as S on T.lID=S.lID')
        display_headings = list(mysql_query[0].keys())
        display_data = [list(row.values()) for row in mysql_query]
        col_widths = [20, 100]
        seasons_nums = [0, 1, 2, 3, 4, 5, 6, 7]
        episode_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        table = [
            [sg.Text(f'Browsing {table_name}. Click on a line for more information.\n'
                     f'To see transcripts from a specific season or episode, please make a selection below.')],
            [sg.Text('Select a season number:'), sg.DropDown(seasons_nums, key='t_season_in', enable_events=True),
            sg.Text('Select an episode number:'), sg.DropDown(episode_nums, key='t_episode_in', enable_events=True),
             sg.Text(' (0 = None)'),
            sg.Button('Browse Transcripts')],
            [sg.Table(values=display_data, headings=display_headings, max_col_width=25,
                      auto_size_columns=False, display_row_numbers=False,
                      justification='left', num_rows=10, enable_events=True,
                      col_widths=col_widths, key=f'-{table_name.upper()} TABLE-')]
        ]
    else:
        table = [
            [sg.Text(f'Browsing {table_name}')],
            [sg.Table(values=data, headings=headings, max_col_width=25,
                      auto_size_columns=True, display_row_numbers=False,
                      justification='left', num_rows=10, enable_events=True,
                      row_height=25, key=f'-{table_name.upper()} TABLE-')]
        ]
    return table, data


def make_facts_layout(conn, procedure_name):
    headings = []
    data = []
    mysql_table = get_procedure2(conn, procedure_name)
    if mysql_table:
        headings = list(mysql_table[0].keys())
        data = [list(row.values()) for row in mysql_table]
    about = ''
    if procedure_name == 'q_best_seasons':
        about = 'Best seasons ranked based on rating then total views.'
    elif procedure_name == 'q_best_episodes':
        about = 'Best episodes ranked based on rating then viewers.'
    elif procedure_name == 'q_main_cast':
        about = 'Main cast (appear in more than 30 episodes).'
    elif procedure_name == 'q_guest_stars':
        about = 'Recurring guest stars (appear in 2-29 episodes).'
    elif procedure_name == 'q_most_lines':
        about = 'Character with the most lines, ranked.'
    elif procedure_name == 'q_popular_characters':
        about = 'Most popular characters (based on number of episodes they appear in).'
    elif procedure_name == 'q_actor_creator':
        about = 'People who have appeared in the show and also have either written or directed.'
    table = [
        [sg.Text(f'{about}')],
        [sg.Table(values=data, headings=headings, max_col_width=25,
                  auto_size_columns=True, display_row_numbers=False,
                  justification='left', num_rows=10, enable_events=False,
                  row_height=25, key='-FACTS TABLE-')]
    ]
    return table


def make_search_layout(conn, proc_name, proc_param):
    headings = []
    data = []
    mysql_table = get_procedure(conn, proc_name, proc_param)
    if mysql_table:
        headings = list(mysql_table[0].keys())
        data = [list(row.values()) for row in mysql_table]
    table = [
        [sg.Text(f'Searching {proc_name}')],
        [sg.Table(values=data, headings=headings, max_col_width=25,
                  auto_size_columns=True,
                  display_row_numbers=False,
                  justification='left',
                  num_rows=10,
                  key='-SEARCH TABLE-',
                  row_height=25)]
    ]
    return table


def make_window(theme):
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']]]
    right_click_menu_def = [[], ['Edit Me', 'Versions', 'Nothing', 'More Nothing', 'Exit']]

    home_layout = [[sg.Text('Welcome to Pawnee Commons!\n'
                            'Database for TV Show Fans and Creators\n\n'
                            'by Célie Pierre, Sarah Lawrence, and Reihaneh Maarefdoust\n'
                            'for COS 457 Database Systems\n'
                            'University of Southern Maine, fall 2023')],
                   ]

    conn = get_database_connection()

    # Browse layouts with data
    episodes_layout, episodes_data = make_browse_layout(conn, 'episode')
    transcripts_layout, transcripts_data = make_browse_layout(conn, 'transcripts')
    characters_layout, characters_data = make_browse_layout(conn, 'charactr')
    person_layout, person_data = make_browse_layout(conn, 'person')

    browse_layout = [
        [sg.TabGroup([[
            sg.Tab('Browse Episodes', episodes_layout, metadata=episodes_data, key='-EPISODE TAB-'),
            sg.Tab('Browse Transcripts', transcripts_layout, metadata=transcripts_data, key='-TRANSCRIPTS TAB-'),
            sg.Tab('Browse Characters', characters_layout, metadata=characters_data, key='-CHARACTR TAB-'),
            sg.Tab('Browse Cast & Crew', person_layout, metadata=person_data, key='-PERSON TAB-')]],
            key='-BROWSE TAB-', expand_x=True, expand_y=True),
        ],
        [sg.Text('', size=(100, 10), key='-BROWSE TEXT-')],
    ]

    # Fun facts section
    procedure_name = 'q_actor_creator'
    mysql_procedure = get_procedure2(conn, procedure_name)
    if mysql_procedure:
        table_headings = list(mysql_procedure[0].keys())
        table_data = [list(row.values()) for row in mysql_procedure]
    facts_layout = [
        [sg.TabGroup([[
            sg.Tab('Best Seasons', make_facts_layout(conn, 'q_best_seasons')),
            sg.Tab('Best Episodes', make_facts_layout(conn, 'q_best_episodes')),
            sg.Tab('Main Cast', make_facts_layout(conn, 'q_main_cast')),
            sg.Tab('Guest Stars', make_facts_layout(conn, 'q_guest_stars')),
            sg.Tab('Most Lines', make_facts_layout(conn, 'q_most_lines')),
            sg.Tab('Popular Characters', make_facts_layout(conn, 'q_popular_characters')),
            sg.Tab('Actors and Creators', make_facts_layout(conn, 'q_actor_creator'))]],
            key='-FACTS TAB-', expand_x=True, expand_y=True),
        ],
        [sg.Text('', size=(100, 10), key='-FACTS TEXT-')]
    ]

    # Search section
    def make_search_layout(procedure_name):
        # For table data
        data = []
        headings = []
        # Create search fields
        search_field = []
        if procedure_name is None or procedure_name == 'basic_character':
            # Get table data
            data = get_procedure(conn, 'basic_character', [1, '', ''])
            if data: headings = list(data[0].keys())
            # User input: cID, cFirstName, cLastName
            get_cIDs = get_query(conn, 'select cID from charactr')
            cIDs = [0] + [list(row.values()) for row in get_cIDs]
            search_field = [
                [sg.Text('Select a character ID number OR search by character name.\n')],
                [sg.Text('Select a character ID:'), sg.DropDown(cIDs, key='cID_in', enable_events=True), sg.Text(' (0 = None)')],
                [sg.Text('OR')],
                [sg.Text('Enter a character\'s first name:'), sg.InputText(key='cFirstName_in')],
                [sg.Text('Enter a character\'s last name:'), sg.InputText(key='cLastName_in')],
                [sg.Text('')],
                [sg.Button('Character Search')],
            ]
        elif procedure_name == 'basic_person':
            # Get table data
            data = get_procedure(conn, 'basic_person', [1, '', '', ''])
            if data: headings = list(data[0].keys())
            # User input: pID_in, firstName_in, lastName_in, job_in
            get_pIDs = get_query(conn, 'select pID from person')
            pIDs = [0] + [list(row.values()) for row in get_pIDs]
            jobs = ['', 'Cast', 'Writer', 'Director']
            search_field = [
                [sg.Text('Select a person ID number OR search by person name OR select a job title.\n')],
                [sg.Text('Select a person ID:'), sg.DropDown(pIDs, key='pID_in', enable_events=True), sg.Text(' (0 = None)')],
                [sg.Text('OR')],
                [sg.Text('Enter a person\'s first name:'), sg.InputText(key='pFirstName_in')],
                [sg.Text('Enter a person\'s last name:'), sg.InputText(key='pLastName_in')],
                [sg.Text('OR')],
                [sg.Text('Select a job title:'), sg.DropDown(jobs, key='job_in', enable_events=True)],
                [sg.Text('')],
                [sg.Button('Cast & Crew Search')],
            ]
        elif procedure_name == 'basic_episode':
            # Get table data
            data = get_procedure(conn, 'basic_episode', ['', 1, 1, '', '2000-01-01'])
            if data: headings = list(data[0].keys())
            # User input: title_in, season_in, episode_in, eID_in, airDate_in
            seasons_nums = [0, 1, 2, 3, 4, 5, 6, 7]
            episode_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                            14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
            get_eIDs = get_query(conn, 'select eID from episode')
            eIDs = [0] + [list(row.values()) for row in get_eIDs]
            search_field = [
                [sg.Text('Enter either an episode title OR select a season and/or episode number '
                         'OR enter an episode ID OR enter air date.\n')],
                [sg.Text('Enter an episode title:'), sg.InputText(key='title_in')],
                [sg.Text('OR')],
                [sg.Text('Select a season number:'), sg.DropDown(seasons_nums, key='season_in', enable_events=True), sg.Text(' (0 = None)')],
                [sg.Text('Select an episode number:'), sg.DropDown(episode_nums, key='episode_in', enable_events=True), sg.Text(' (0 = None)')],
                [sg.Text('OR')],
                [sg.Text('Enter an episode ID:'), sg.InputText(key='eID_in')],
                [sg.Text('OR')],
                [sg.Text('Enter an episode air date (format YYYY-MM-DD):'), sg.InputText(key='airDate_in')],
                [sg.Text('')],
                [sg.Button('Episode Search')],
            ]
        elif procedure_name == 'basic_transcript':
            # Get table data
            data = get_procedure(conn, 'basic_transcript', ['pilot', '', '', 1])
            if data: headings = list(data[0].keys())
            # User input: title_in, firstName_in, lastName_in, dialogue_in
            search_field = [
                [sg.Text('Enter either an episode title OR a character\'s name AND minimum dialogue length')],
                [sg.Text('Enter an episode title:'), sg.InputText(key='t_title_in')],
                [sg.Text('OR')],
                [sg.Text('Enter a character\'s first name:'), sg.InputText(key='t_cFirstName_in')],
                [sg.Text('Enter a character\'s last name:'), sg.InputText(key='t_cLastName_in')],
                [sg.Text('AND')],
                [sg.Text('Enter minimum number of characters (letters, numbers):'), sg.InputText(key='dialogue_in')],
                [sg.Text('')],
                [sg.Button('Transcript Search')],
            ]
        elif procedure_name == 'basic_viewers':
            # Get table data
            data = get_procedure(conn, 'basic_viewers', [1, 0, 0])
            if data: headings = list(data[0].keys())
            # User input: rating_in, votes_in, viewers_in
            ratings = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            search_field = [
                [sg.Text('Select a rating and/or number or votes and/or number of viewers\n')],
                [sg.Text('Select a minimum rating:'), sg.DropDown(ratings, key='rating_in', enable_events=True), sg.Text('(0 = None)')],
                [sg.Text('AND/OR')],
                [sg.Text('Enter minimum number of votes:'), sg.InputText(key='votes_in')],
                [sg.Text('AND/OR')],
                [sg.Text('Enter minimum number of viewers:'), sg.InputText(key='viewers_in')],
                [sg.Text('')],
                [sg.Button('Viewer Stats Search')],
            ]
        # Create tables
        table_name = '-' + procedure_name + '_table-'
        basic_layout = [
            [sg.Table(values=data, headings=headings, max_col_width=25,
                      auto_size_columns=True, display_row_numbers=False, justification='left',
                      num_rows=10, key=table_name, row_height=25, visible=False,
                      enable_events=True)],
        ]
        layout = search_field + basic_layout
        return layout

    data = []
    headings = []
    sentence_layout = [
        [sg.Text('Search the transcripts for dialogue.\n')],
        [sg.Text('Enter search: '), sg.InputText(key='sentence_in')],
        [sg.Text('')],
        [sg.Button('Advanced Transcript Search')],
        [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'),
         sg.Text('', size=(50, 1), key='-PROGRESS TEXT-')],
        [sg.Text('')],
        [sg.Multiline('', size=(100, 20), autoscroll=True, enable_events=True, key='-SENTENCE TEXT-')]
    ]

    search_layout = [
        [sg.TabGroup([[
            sg.Tab('Search Characters', make_search_layout('basic_character')),
            sg.Tab('Search Episodes', make_search_layout('basic_episode')),
            sg.Tab('Search Cast & Crew', make_search_layout('basic_person')),
            sg.Tab('Search Transcripts (basic)', make_search_layout('basic_transcript')),
            sg.Tab('Search Transcripts (advanced)', sentence_layout),
            sg.Tab('Search Viewers', make_search_layout('basic_viewers'))]],
            key='-SEARCH TAB-', expand_x=True, expand_y=True),
        ],
        [sg.Text('', size=(100, 10), key='-SEARCH TEXT-')]
    ]

    data = []
    headings = []
    update_layout = [
        [sg.Text(f'Insert (with trigger and rollback)\n\n'
                 f'Add a character:')],
        [sg.Text('Enter a new character\'s first name:'), sg.InputText(key='trig_cFirstName_in')],
        [sg.Text('Enter a new character\'s last name:'), sg.InputText(key='trig_cLastName_in')],
        [sg.Text('')],
        [sg.Button('Add Character')],
        [sg.Text('')],
        [sg.Text('', size=(100, 10), key='-UPDATE TEXT-')]

    ]

    layout = [[sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)],
              [sg.Text('Pawnee Commons', size=(38, 1), justification='center', font=("Helvetica", 16),
                       relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
    layout += [[sg.TabGroup([[
        sg.Tab('Home', home_layout),
        sg.Tab('Browse', browse_layout),
        sg.Tab('Search', search_layout),
        sg.Tab('Fun Facts', facts_layout),
        sg.Tab('Insert', update_layout)
    ]],
        key='-TAB GROUP-', expand_x=True, expand_y=True),
    ]]

    layout[-1].append(sg.Sizegrip())
    window = sg.Window('Pawnee Commons: Database for TV Show Fans and Creators', layout, right_click_menu=right_click_menu_def,
                       right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0, 0),
                       use_custom_titlebar=True, finalize=True, keep_on_top=True)
    window.set_min_size(window.size)
    return window


def main():
    window = make_window(sg.theme())
    conn = get_database_connection()

    # This is an Event Loop
    browse_layout = make_browse_layout(conn, 'episode')
    facts_layout = make_facts_layout(conn, 'q_best_seasons')
    while True:
        event, values = window.read(timeout=100)
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ', values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break

        def hide_all_tables():
            all_tables = ['-basic_character_table-', '-basic_episode_table-', '-basic_person_table-',
                          '-basic_transcript_table-', '-basic_viewers_table-', '-TRANSCRIPTS TABLE-']
            for table in all_tables:
                window[table].update(visible=False)

        if event == 'Character Search':
            basic_character_in = []
            cFirstName = values['cFirstName_in']
            cLastName = values['cLastName_in']
            if values['cID_in'] and int(values['cID_in'][0]) != 0:
                cID = int(values['cID_in'][0])
                basic_character_in = [cID, '', '']
            elif cFirstName or cLastName:
                if not cFirstName:
                    cFirstName = ''
                elif not cLastName:
                    cLastName = ''
                basic_character_in = [0, cFirstName, cLastName]
            else:
                sg.popup(f'Please enter valid input.\n'
                         f'Either select a character ID\n'
                         f'OR enter a character name.')
            mysql_table = get_procedure(conn, 'basic_character', basic_character_in)
            if mysql_table:
                data = [list(row.values()) for row in mysql_table]
                hide_all_tables()
                window['-basic_character_table-'].update(visible=True, values=data)
            else:
                window['-SEARCH TEXT-'].update(f'No results found. Please try again.')
        if event == '-basic_character_table-':
            selected_row_index = values[event][0]
            selected_row_values = data[selected_row_index]
            window['-SEARCH TEXT-'].update(f'You clicked on: {selected_row_values} from basic_character')

        elif event == 'Episode Search':
            basic_episode_in = []
            if values['title_in']:
                basic_episode_in = [values['title_in'], 0, 0, '', '2000-01-01']
            elif ((values['season_in'] or values['episode_in']) and
                  (values['season_in'] != 0 or values['episode_in'] != 0)):
                season = values['season_in']
                episode = values['episode_in']
                if season == 0 or season is None:
                    season = 0
                if episode == 0 or episode is None:
                    episode = 0
                basic_episode_in = ['', season, episode, '', '2000-01-01']
            elif values['eID_in']:
                basic_episode_in = ['', 0, 0, values['eID_in'], '2000-01-01']
            elif values['airDate_in']:
                basic_episode_in = ['', 0, 0, '', values['airDate_in']]
            mysql_table = get_procedure(conn, 'basic_episode', basic_episode_in)
            if mysql_table:
                data = [list(row.values()) for row in mysql_table]
            else:
                window['-SEARCH TEXT-'].update(f'No results found. Please try again.')
            hide_all_tables()
            window['-basic_episode_table-'].update(visible=True, values=data)
        if event == '-basic_episode_table-':
            selected_row_index = values[event][0]
            selected_row_values = data[selected_row_index]
            window['-SEARCH TEXT-'].update(f'You clicked on: {selected_row_values} from basic_episode')

        elif event == 'Cast & Crew Search':
            basic_person_in = []
            if values['pID_in'] and values['pID_in'] != 0:
                pID = int(values['pID_in'][0])
                basic_person_in = [pID, '', '', '']
            elif values['pFirstName_in'] or values['pLastName_in']:
                basic_person_in = [0, values['pFirstName_in'], values['pLastName_in'], '']
            elif values['job_in']:
                job = values['job_in']
                if job == 'Writer':
                    job = 'written_by'
                elif job == 'Director':
                    job = 'directed_by'
                basic_person_in = [0, '', '', job]
            mysql_table = get_procedure(conn, 'basic_person', basic_person_in)
            if mysql_table:
                data = [list(row.values()) for row in mysql_table]
            else:
                window['-SEARCH TEXT-'].update(f'No results found. Please try again.')
            hide_all_tables()
            window['-basic_person_table-'].update(visible=True, values=data)
        if event == '-basic_person_table-':
            selected_row_index = values[event][0]
            selected_row_values = data[selected_row_index]
            window['-SEARCH TEXT-'].update(f'You clicked on: {selected_row_values} from basic_person')

        elif event == 'Transcript Search':
            dialogue = 1
            if values['dialogue_in']:
                dialogue = values['dialogue_in']
            if values['t_title_in']:
                basic_transcript_in = [values['t_title_in'], '', '', dialogue]
            elif values['t_cFirstName_in'] or values['t_cLastName_in']:
                basic_transcript_in = ['', values['t_cFirstName_in'], values['t_cLastName_in'], dialogue]
            else:
                basic_transcript_in = ['', '', '', dialogue]
            mysql_table = get_procedure(conn, 'basic_transcript', basic_transcript_in)
            if mysql_table:
                data = [list(row.values()) for row in mysql_table]
            else:
                window['-SEARCH TEXT-'].update(f'No results found. Please try again.')
                data = []
            hide_all_tables()
            window['-basic_transcript_table-'].update(visible=True, values=data)
        if event == '-basic_transcript_table-':
            selected_row_index = values[event][0]
            selected_row_values = data[selected_row_index]
            window['-SEARCH TEXT-'].update(f'You clicked on: {selected_row_values} from basic_transcript')

        elif event == 'Viewer Stats Search':
            rating = 0
            votes = 0
            viewers = 0
            if values['rating_in']:
                rating = values['rating_in']
            if values['votes_in']:
                votes = values['votes_in']
            if values['viewers_in']:
                viewers = values['viewers_in']
            basic_viewers_in = [rating, votes, viewers]
            mysql_table = get_procedure(conn, 'basic_viewers', basic_viewers_in)
            if mysql_table:
                data = [list(row.values()) for row in mysql_table]
            else:
                window['-SEARCH TEXT-'].update(f'No results found. Please try again.')
                data = []
            hide_all_tables()
            window['-basic_viewers_table-'].update(visible=True, values=data)
        if event == '-basic_viewers_table-':
            selected_row_index = values[event][0]
            selected_row_values = data[selected_row_index]
            window['-SEARCH TEXT-'].update(f'You clicked on: {selected_row_values} from basic_viewers')

        if event == 'Browse Transcripts':
            season = 0
            episode = 0
            if ((values['t_season_in'] or values['t_episode_in']) and
                  (values['t_season_in'] != 0 or values['t_episode_in'] != 0)):
                season = values['t_season_in']
                episode = values['t_episode_in']
            if int(episode) < 10:
                episode = '0' + str(episode)
            eID = 's' + str(season) + 'e' + str(episode) + '%'
            print(eID)
            custom_query = 'select S.cName, T.dialogue from transcripts as T join says as S on T.lID=S.lID where T.lID like \'' + eID + '\''
            mysql_table = get_query(conn, custom_query)
            if mysql_table:
                data = [list(row.values()) for row in mysql_table]
            else:
                window['-SEARCH TEXT-'].update(f'No results found. Please try again.')
            hide_all_tables()
            window['-TRANSCRIPTS TABLE-'].update(visible=True, values=data)

        if event.endswith('TABLE-'):
            table_name = event[1:-7]
            selected_row_index = values[f'-{table_name} TABLE-'][0]
            selected_row_values = window[f'-{table_name} TAB-'].metadata
            if table_name == 'EPISODE':
                window['-BROWSE TEXT-'].update(
                    f'Episode ID: {selected_row_values[selected_row_index][0]}\n'
                    f'Original air date: {selected_row_values[selected_row_index][4]}\n'
                    f'Episode Description: {selected_row_values[selected_row_index][5]}')
            elif table_name == 'TRANSCRIPTS':
                window['-BROWSE TEXT-'].update(
                    f'Line ID: {selected_row_values[selected_row_index][0]}\n'
                    f'Full dialogue: {selected_row_values[selected_row_index][2]}')
            else:
                window['-BROWSE TEXT-'].update(
                    f'You clicked on: {selected_row_values[selected_row_index]} from {table_name} TABLE')

        if event == 'Add Character':
            newFirstName = values['trig_cFirstName_in']
            newLastName = values['trig_cLastName_in']
            find_directory = os.path.dirname(os.path.abspath(__file__))
            path_to_data_dir = os.path.join(find_directory, "config.json")
            test_passed = trigger.trigger_test(path_to_data_dir, newFirstName, newLastName)
            if test_passed:
                new_location = trigger.checks(path_to_data_dir, newFirstName, newLastName)
                window['-UPDATE TEXT-'].update(f'Insert successful. New character added.\n\n'
                                               f'New character\'s first name: {newFirstName}\n'
                                               f'New character\'s last name: {newLastName}\n'
                                               f'New character\'s ID number: {new_location[0][0]}')
            else:
                exist_char = [0, newFirstName, newLastName]
                exist_char_info = get_procedure(conn, 'basic_character', exist_char)
                existFirstName = exist_char_info[0].get('cFirstName')
                existLastName = exist_char_info[0].get('cLastName')
                existcID = exist_char_info[0].get('cID')
                window['-UPDATE TEXT-'].update(f'Character already exists. Please try again.\n\n'
                                               f'Existing character\'s first name: {existFirstName}\n'
                                               f'Existing character\'s last name: {existLastName}\n'
                                               f'Existing character\'s ID number: {existcID}\n')

        if event == 'Advanced Transcript Search':
            window['-PROGRESS TEXT-'].update('Searching... please wait...')
            progress_bar = window['-PROGRESS BAR-']
            for i in range(25):
                progress_bar.update(current_count=i + 1)
            search_query = sentencesearcher.SentenceSearcher(values['sentence_in'])
            for i in range(25, 75):
                progress_bar.update(current_count=i + 1)
            search_query.start_search()
            sentence_results = search_query.get_query_results()
            for i in range(75, 100):
                progress_bar.update(current_count=i + 1)
            window['-SENTENCE TEXT-'].update(sentence_results)
            window['-PROGRESS TEXT-'].update('')
            print("Done")

    window.close()
    exit(0)


if __name__ == '__main__':
    sg.theme('SystemDefault')
    main()

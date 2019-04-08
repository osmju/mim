# -*- coding: utf-8 -*-

import os
import sys
import random
import sqlite3 as sqlt

from flask import Flask, session, request, render_template, url_for, redirect, g
from flask_babel import Babel
from flask_babel import gettext, ngettext, lazy_gettext, refresh
from werkzeug.utils import secure_filename


import forms
import strings
import utility as util

#----------------------------------------------------------#
# FLASK CONFIGURATION
#----------------------------------------------------------#
app = Flask(__name__)

DATABASE_FILE_AUTO = 'exp_data_auto.db'
DATABASE_FILE_CREAMY = 'exp_data_creamy.db'
DATABASE_FILE_EMOTIONS = 'exp_data_emotions.db'
UPLOAD_FOLDER = 'static/uploaded'
MAX_COUNTER = 8
NUM_AUDIO_FILES = 154
AUDIO_FOLDER = 'static/audio_db/'

app.debug = True
app.secret_key = '_oHMYGosH@ndOhMYFuckIngpiZz@_'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

babel = Babel(app)
current_language = 'en'

LANGUAGES = {
    'en': 'English',
    'fr': 'Français',
    'nl': 'Nederlands', 
    'es': 'Espanol'
}

# LAUNCH Configuration
# "CONFIG_AUTO"     = Automatic selection of contrasting sounds
# "CONFIG_CREAMY"   = Fixed selection of a creamy and rough sounds
# "CONFIG_EMOTIONS" = Fixed selection of emotions sounds
launch_config = "CONFIG_AUTO"

#----------------------------------------------------------#
# END CONFIGURATION
#----------------------------------------------------------#

#----------------------------------------------------------#
# UTILITY FUNCTIONS
#----------------------------------------------------------#
def get_next_sound():    
    return random.randint(0, NUM_AUDIO_FILES)

#----------------------------------------------------------#
@babel.localeselector
def get_locale():
    #print request.accept_languages.best_match(LANGUAGES.keys())
    #return request.accept_languages.best_match(LANGUAGES.keys())
    print "GET LOCALE WITH LANGUAGE = {0}".format(current_language)

    return current_language

#----------------------------------------------------------#
def insert_xp_results(results_tuple):
    db_file = ""

    if launch_config == "CONFIG_AUTO":
        db_file = DATABASE_FILE_AUTO
    elif launch_config == "CONFIG_CREAMY":
        db_file = DATABASE_FILE_CREAMY
    elif launch_config == "CONFIG_EMOTIONS":
        db_file = DATABASE_FILE_EMOTIONS

    with sqlt.connect(db_file) as db_connection:
        cur = db_connection.cursor()

        cur.execute('''INSERT INTO XP_RESULTS(name, email, age, city, gender, flavor1, flavor2, sound1, sound2,
            snd1_q1, snd1_q2, snd1_q3, snd1_q4, snd1_q5, snd1_q6, snd1_q7, snd1_q8,
            snd2_q1, snd2_q2, snd2_q3, snd2_q4, snd2_q5, snd2_q6, snd2_q7, snd2_q8,
            cmp_q1, cmp_q2, cmp_q3, cmp_q4, cmp_q5, cmp_q6)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', results_tuple)
        
        db_connection.commit()
    
#----------------------------------------------------------#
def write_to_database(cli_display=True):
    # participant's informations 
    name = session['exp_name']
    email = session['exp_email']
    age = session['exp_age']
    city = session['exp_city']
    gender = session['exp_gender']

    # sounds informations
    flavor1 = session['flavour1']
    flavor2 = session['flavour2']
    sound1 = session['sound1']
    sound2 = session['sound2']

    # questions 1
    snd1_q1 = session['snd1_q1']
    snd1_q2 = session['snd1_q2']
    snd1_q3 = session['snd1_q3']
    snd1_q4 = session['snd1_q4']
    snd1_q5 = session['snd1_q5']
    snd1_q6 = session['snd1_q6']
    snd1_q7 = session['snd1_q7']
    snd1_q8 = session['snd1_q8']

    # questions 2
    snd2_q1 = session['snd2_q1']
    snd2_q2 = session['snd2_q2']
    snd2_q3 = session['snd2_q3']
    snd2_q4 = session['snd2_q4']
    snd2_q5 = session['snd2_q5']
    snd2_q6 = session['snd2_q6']
    snd2_q7 = session['snd2_q7']
    snd2_q8 = session['snd2_q8']

    # comparative questions
    cmp_q1 = session['cmp_q1']
    cmp_q2 = session['cmp_q2']
    cmp_q3 = session['cmp_q3']
    cmp_q4 = session['cmp_q4']
    cmp_q5 = session['cmp_q5']
    cmp_q6 = session['cmp_q6']

    if cli_display:
        print "=================================================="
        print " PARTICIPANT'S INFORMATION"
        print "=================================================="
        print name
        print email
        print age
        print gender
        print "=================================================="
        print " SOUNDS INFORMATIONS "
        print "=================================================="
        print flavor1
        print flavor2
        print sound1
        print sound2
        print "=================================================="
        print " SOUND 1 QUESTIONS"
        print "=================================================="
        print snd1_q1
        print snd1_q2
        print snd1_q3
        print snd1_q4
        print snd1_q5
        print snd1_q6
        print snd1_q7
        print snd1_q8
        print "=================================================="
        print " SOUND 2 QUESTIONS"
        print "=================================================="
        print snd2_q1
        print snd2_q2
        print snd2_q3
        print snd2_q4
        print snd2_q5
        print snd2_q6
        print snd2_q7
        print snd2_q8
        print "=================================================="
        print " COMPARATIVE QUESTIONS"
        print "=================================================="
        print cmp_q1
        print cmp_q2
        print cmp_q3
        print cmp_q4
        print cmp_q5
        print cmp_q6
    
    # write user data
    print "Writing participant's informations to database."   

    results_tuple = (name, email, age, city, gender, flavor1, flavor2, sound1, sound2,
        snd1_q1, snd1_q2, snd1_q3, snd1_q4, snd1_q5, snd1_q6, snd1_q7, snd1_q8,
        snd2_q1, snd2_q2, snd2_q3, snd2_q4, snd2_q5, snd2_q6, snd2_q7, snd2_q8,
        cmp_q1, cmp_q2, cmp_q3, cmp_q4, cmp_q5, cmp_q6)    
    
    insert_xp_results(results_tuple)

#----------------------------------------------------------#
# ROUTES
#----------------------------------------------------------#
@app.route('/change_language/<lang>')
def change_language(lang):
    print "CHANGE LANGUAGE !"
    print lang

    global current_language
    current_language = lang
    refresh()

    return render_template('dummy.html')

#----------------------------------------------------------#
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm() 
    name = None
    email = None    
    age = None
    city = None
    gender = None
    consent = None     

    if login_form.validate_on_submit():
        #experiment_id = get_new_experiment_id()
        name = login_form.name.data
        email = login_form.email.data
        age = login_form.age.data
        city = login_form.city.data
        gender = login_form.gender.data
        consent = login_form.consent.data             
        
        if consent == "disagree":
            print "User disagrees with consent. ABORT."
            return render_template('login.html', form=login_form, lang=current_language)
            # TODO :: Redirect to ABORT page
        
        session['exp_name'] = name
        session['exp_email'] = email
        session['exp_age'] = age
        session['exp_city'] = city
        session['exp_gender'] = gender         

        # Here we have 3 options:
        # + Option 1 :: Automatically find contrasting flavors
        # + Option 2 :: Fixed Creamy / Rough sounds
        # + Option 3 :: Fixed Emotion 1 / Emotion 2
        
        if launch_config == "CONFIG_AUTO":
            # select 2 contrasting sounds from 2 contrasting flavours
            contrasting_flavours = util.get_contrasting_flavours(AUDIO_FOLDER)
            session['flavour1'] = contrasting_flavours[0]
            session['flavour2'] = contrasting_flavours[1]
            session['sound1'] = util.get_random_sound(AUDIO_FOLDER, session['flavour1'])
            session['sound2'] = util.get_random_sound(AUDIO_FOLDER, session['flavour2'])
            
        elif launch_config == "CONFIG_CREAMY":  
            selected_flavor = random.randint(0,1)
            
            if selected_flavor == 0: # creamy
                session['flavour1'] = 'creamy'
                session['flavour2'] = 'rough'
                session['sound1'] = 'fixed_sounds/WD_creamy_soundtrack.mp3'
                session['sound2'] = 'fixed_sounds/TK_rough_soundtrack.mp3'
            else:
                session['flavour2'] = 'creamy'
                session['flavour1'] = 'rough'
                session['sound2'] = 'fixed_sounds/WD_creamy_soundtrack.mp3'
                session['sound1'] = 'fixed_sounds/TK_rough_soundtrack.mp3'
        
        elif launch_config == "CONFIG_EMOTIONS":
            selected_flavor = random.randint(0,1)

            if selected_flavor == 0: # emotions04
                session['flavour1'] = 'emotions04'
                session['flavour2'] = 'emotions01'
                session['sound1'] = 'fixed_sounds/WD_music_emotions_04.mp3'
                session['sound2'] = 'fixed_sounds/TK_music_emotions_01.mp3'        
            else:
                session['flavour2'] = 'emotions04'
                session['flavour1'] = 'emotions01'
                session['sound2'] = 'fixed_sounds/WD_music_emotions_04.mp3'
                session['sound1'] = 'fixed_sounds/TK_music_emotions_01.mp3'        

        print session['flavour1']
        print session['flavour2']
        print session['sound1']
        print session['sound2']
        
        return redirect(url_for('experiment_instructions'))

        global current_language

    return render_template('login.html', form=login_form, lang=current_language)

#----------------------------------------------------------#
@app.route('/experiment_instructions', methods=['GET', 'POST'])
def experiment_instructions():
    if request.method == 'POST':
        # user clicked on next: redirect to next page.
        return redirect(url_for('experiment_song1'))        
    
    instructions_text = strings.experiment_instructions
    
    return render_template('instructions.html', instruct=instructions_text)

#----------------------------------------------------------#
@app.route('/experiment_song1', methods=['GET', 'POST'])
def experiment_song1():
    if request.method == 'POST':
        # user clicked on next: redirect to next page
        return redirect(url_for('questions_sound1'))        
    
    instructions_text = strings.instructions_sound1

    return render_template('listen_sound.html', sound=session['sound1'], instruct=instructions_text)

#----------------------------------------------------------#
@app.route('/experiment_song2', methods=['GET', 'POST'])
def experiment_song2():
    if request.method == 'POST':
        # user clicked on next: redirect to next page
        return redirect(url_for('questions_sound2'))        
    
    # TODO :: Select text from correct language file.
    instructions_text = strings.instructions_sound2

    return render_template('listen_sound.html', sound=session['sound2'], instruct=instructions_text)

#----------------------------------------------------------#
@app.route('/questions_sound1', methods=['GET', 'POST'])
def questions_sound1():
    # create form and send it to the template
    questions_form = forms.SoundQuestionsForm()  
    
    # if NOT validate_on_submit() print error message to guide user

    if request.method == 'POST' and questions_form.validate_on_submit():       
        session['snd1_q1'] = int(questions_form.question1.data)
        session['snd1_q2'] = int(questions_form.question2.data)
        session['snd1_q3'] = int(questions_form.question3.data)
        session['snd1_q4'] = int(questions_form.question4.data)
        session['snd1_q5'] = int(questions_form.question5.data)
        session['snd1_q6'] = int(questions_form.question6.data)
        session['snd1_q7'] = int(questions_form.question7.data)
        session['snd1_q8'] = int(questions_form.question8.data)       
       
        return redirect(url_for('experiment_song2')) 
    
    return render_template('sound_questions.html', form=questions_form)

#----------------------------------------------------------#
@app.route('/questions_sound2', methods=['GET', 'POST'])
def questions_sound2():
    # create form and send it to the template
    questions_form = forms.SoundQuestionsForm()

    if request.method == 'POST' and questions_form.validate_on_submit():
        session['snd2_q1'] = int(questions_form.question1.data)
        session['snd2_q2'] = int(questions_form.question2.data)
        session['snd2_q3'] = int(questions_form.question3.data)
        session['snd2_q4'] = int(questions_form.question4.data)
        session['snd2_q5'] = int(questions_form.question5.data)
        session['snd2_q6'] = int(questions_form.question6.data)
        session['snd2_q7'] = int(questions_form.question7.data)
        session['snd2_q8'] = int(questions_form.question8.data)

        return redirect(url_for('comparative_questions'))

    return render_template('sound_questions.html', form=questions_form)

#----------------------------------------------------------#
@app.route('/comparative_questions', methods=['GET', 'POST'])
def comparative_questions():
    # create form and send it to the template
    comparative_form = forms.ComparisonQuestions()
    
    if request.method == 'POST' and comparative_form.validate_on_submit():
        session['cmp_q1'] = comparative_form.question1.data
        session['cmp_q2'] = comparative_form.question2.data
        session['cmp_q3'] = float(comparative_form.question3.data)
        session['cmp_q4'] = comparative_form.question4.data
        session['cmp_q5'] = comparative_form.question5.data
        session['cmp_q6'] = float(comparative_form.question6.data)        
        
        return redirect(url_for('final_page'))

    return render_template('comparative_questions.html', form=comparative_form)

#----------------------------------------------------------#
@app.route('/final_page', methods=['GET', 'POST'])
def final_page():
    if request.method == 'POST':
        # TODO : Write data to database
        write_to_database(cli_display=True)
        return redirect(url_for('login'))

    text = strings.thanks
    
    return render_template('thanks.html', text=text)

#----------------------------------------------------------#
if __name__ == '__main__':
    if len(sys.argv) < 2:
        launch_config = "CONFIG_AUTO"
    else:    
        launch_config = sys.argv[1]    

    print "Launching with launch configuration = {0}".format(launch_config)    

    app.run(host='127.0.0.1', port=5000, threaded=True)

#----------------------------------------------------------#


import sqlite3 as sqlt
import sys

# open connection to new database
conn = sqlt.connect('exp_data_auto.db')

with conn:    
    cur = conn.cursor()   
    
    # create table XP_RESULTS
    cur.execute('''CREATE TABLE XP_RESULTS
                   (xp_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT,
                    age INTEGER NOT NULL,
                    city TEXT NOT NULL,
                    gender TEXT NOT NULL,
                    flavor1 STRING NOT NULL,
                    flavor2 STRING NOT NULL,
                    sound1 STRING NOT NULL,
                    sound2 STRING NOT NULL,
                    snd1_q1 INTEGER NOT NULL,
                    snd1_q2 INTEGER NOT NULL,
                    snd1_q3 INTEGER NOT NULL,
                    snd1_q4 INTEGER NOT NULL,
                    snd1_q5 INTEGER NOT NULL,
                    snd1_q6 INTEGER NOT NULL,
                    snd1_q7 INTEGER NOT NULL,
                    snd1_q8 INTEGER NOT NULL,
                    snd2_q1 INTEGER NOT NULL,
                    snd2_q2 INTEGER NOT NULL,
                    snd2_q3 INTEGER NOT NULL,
                    snd2_q4 INTEGER NOT NULL,
                    snd2_q5 INTEGER NOT NULL,
                    snd2_q6 INTEGER NOT NULL,
                    snd2_q7 INTEGER NOT NULL,
                    snd2_q8 INTEGER NOT NULL,
                    cmp_q1 TEXT NOT NULL,
                    cmp_q2 TEXT NOT NULL,
                    cmp_q3 REAL NOT NULL,
                    cmp_q4 TEXT NOT NULL,
                    cmp_q5 TEXT NOT NULL,
                    cmp_q6 REAL NOT NULL)''')
    
    # commit changes to the database
    conn.commit()

# close connection to database
conn.close()

    


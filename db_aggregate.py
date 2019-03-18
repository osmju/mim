import sqlite3 as sqlt
import sys
import unicodecsv as csv

DB_FILES = ['exp_data.db', 'exp_data2.db', 'exp_data3.db']


#=========================================================================#
def gather_data_from_db(db_file):
    conn = sqlt.connect(db_file)
    cur = conn.cursor()

    cur.execute("SELECT * FROM XP_RESULTS")

    rows = cur.fetchall()

    conn.close()

    return rows

#=========================================================================#

# Main code
merged_rows = []

print "Reading input data."

for db_file in DB_FILES:
    print "Reading file :: {0}".format(db_file)
    
    rows = gather_data_from_db(db_file)
    
    for item in rows:
        merged_rows.append(list(item)) # convert SQL tuples to lists

total_num_records = len(merged_rows)

print
print "Total number of records :: {0}".format(total_num_records)
print

for i in range(total_num_records):
    merged_rows[i][0] = i # Modify ID to have continuous ids

    print "=== Record {0} ===".format(i)
    print merged_rows[i]
    print

# Write list of merged results in CSV file
print "Writing merged data in output.csv file."

with open("output.csv", "wb") as csv_file:
    writer = csv.writer(csv_file)

    # columns headers
    writer.writerow([
        'ID', 'Name', 'Email', 'Age', 'City', 'Gender',
        'Flavor 1', 'Flavor 2', 'Sound 1', 'Sound 2',
        'snd1-q1', 'snd1-q2', 'snd1-q3', 'snd1-q4', 'snd1-q5', 'snd1-q6', 'snd1-q7', 'snd1-q8',
        'snd2-q1', 'snd2-q2', 'snd2-q3', 'snd2-q4', 'snd2-q5', 'snd2-q6', 'snd2-q7', 'snd2-q8',
        'cmp-q1', 'cmp-q2', 'cmp-q3', 'cmp-q4', 'cmp-q5', 'cmp-q6'])

    writer.writerows(merged_rows)

print "Done."







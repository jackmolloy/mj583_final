from subprocess import call
import os
import glob
import json

# # Open the file with read only permit
# f = open('tick_nc.txt')
# # use readline() to read the first line
# line = f.readline()
# while line:
#     os.system("python3 yahoo_finance.py " + line)
#     line = f.readline()
# f.close()


glob_data = []


for file in glob.glob('*-summary.json'):
    with open(file) as json_file:
        data = json.load(json_file)
        glob_data.append(data)
        

with open('all_companies.json', 'w') as f:
    json.dump(glob_data, f, indent=4)

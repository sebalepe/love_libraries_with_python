import os

with open('requirements.txt', 'r') as file:
	data = [line.strip('\n') for line in file]



for line in data:
	txt = f'''
cd .. 
git clone {line}
'''
	os.system(txt)
import os

with open('requirements.txt', 'r') as file:
	data = [line.strip('\n') for line in file]


for line in data:
	os.system(f"git clone {line}")
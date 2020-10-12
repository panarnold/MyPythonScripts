#! python
# reg_finder: it opens every .txt file in the current directory, ask user for the regex and is able
# to find its occurrencies in this files and print it on the screen
# X 2020 Arnold Cytrowski



import re, os
regex = input('Type here regex which u want to find:\n')
current_regex = re.compile(regex)

file_list = os.listdir('.')

occurencies = []

for file in file_list:
    if file.endswith('.txt'):
        file_content = open(file)
        count = 0
        while True:
            count += 1
            line = file_content.readline()
            if not line:
                break
            if current_regex.search(line):
                occurencies.append('{}: line {}: {}'.format(file, count, line.strip()))
print(f'there are occurencies of "{regex}":')
for occurency in occurencies:
    print(occurency)



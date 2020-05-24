#chat
'''
with open('input.txt', 'r', encoding='utf-8') as f:
	text = []
	for line in f:
		t = line.strip().split(',')
		if line == 'ALLEN':
			name.append(line)
			continue
			if line == 'TOM':
				name.append(line)
				continue
		else:
			text.append([name, line])
'''

def read_file(filename):
	lines = []
	person = None
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	new = []
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()
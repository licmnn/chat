lines = []
with open('input.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
	print(lines)

new = []
for line in lines:
	if line == 'Allen':
		person = 'Allen'
		continue
	elif line == 'Tom':
		person = 'Tom'
		continue
	new.append(person + ': ' + line)
print(new)
	
#	def write_file(filename, lines):
with open('output.txt', 'w') as f:
	for n in new:
		f.write(n + '\n')

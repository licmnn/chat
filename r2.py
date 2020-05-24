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
			text.append([name, line])       split(' ')
'''
#读取文件
def read_file(filename):
	lines = []
	person = None
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines
#名称转换
def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count  = 0
	viki_sticker_count  = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen 说了', allen_word_count, '个字', '传了', allen_sticker_count, '貼圖', allen_image_count, '个图片')
	print('viki 说了', viki_word_count, '个字', '传了', viki_sticker_count, '貼圖', viki_image_count, '个图片')

	
#写入文档	
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')
#程序执行
def main():
	lines = read_file('Viki.txt')
	lines = convert(lines)
	#write_file('out_Viki.txt', lines)

main()
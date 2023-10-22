# 打开TXT文件并读取内容
with open('Movielens/test.txt', 'r') as txt_file:
    lines = txt_file.readlines()

# 处理每一行，将整数减1
new_lines = []
for line in lines:
    parts = line.strip().split()
    new_parts = []
    for part in parts:
        try:
            num = int(part)
            new_num = num - 1
            new_parts.append(str(new_num))
        except ValueError:
            new_parts.append(part)
    new_line = ' '.join(new_parts)
    new_lines.append(new_line)

# 创建一个新的TXT文件并将处理后的内容写入其中
with open('Movielens/test.txt', 'w') as new_txt_file:
    for new_line in new_lines:
        new_txt_file.write(new_line + '\n')

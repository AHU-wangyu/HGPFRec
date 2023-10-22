# 打开DAT文件并读取内容
with open('Movielens/user_movie.dat', 'r') as dat_file:
    lines = dat_file.readlines()

# 提取前两列数据
data = [line.strip().split()[:2] for line in lines]

# 创建一个TXT文件并将数据写入其中
with open('Movielens/um.txt', 'w') as txt_file:
    for row in data:
        txt_file.write('\t'.join(row) + '\n')


import time

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0:
        	print(len(data)) 
        # 求餘數



# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)

# ave_len = sum_len / len(data)
# print(ave_len)

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('There are', len(new), 'messages that length is more than 100' )

# ring = []
# for d in data:
# 	if 'ring' in d:
# 		ring.append(d)
# print(ring[0])

# #ring = [d for d in data if 'ring' in d] #24~#27的快寫法

# counts = 0
# for review in ring[:3]:
# 	counts += 1
# 	print('This is', counts, 'messages that contain ring')
# 	print(review)

# 文字記數
start_time = time.time()

wc = {} # word_count
for d in data:
    words = d.split() # split dafault用空格分割 且default遇到連續空格會全跳過不會切成空字串
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time ,'秒')
print(len(wc))

while True:
	word = input('請問你想查什麼字：')
	if word == 'q':
		print('感謝使用此查詢功能')
		break
	elif word in wc:
		print(word, '出現次數',wc[word])
	else:
		print('這個字沒出現過')

		
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		#if count % 1000 == 0:
		#	print(len(data)) 
		# % 求餘數

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

ave_len = sum_len / len(data)
print(ave_len)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'messages that length is more than 100' )

ring = []
for d in data:
	if 'ring' in d:
		ring.append(d)
print(ring[0])

#ring = [d for d in data if 'ring' in d] #24~#27的快寫法

counts = 0
for review in ring[:3]:
	counts += 1
	print('This is', counts, 'messages that contain ring')
	print(review)
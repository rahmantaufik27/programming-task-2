g = []
g2 = []
vc = []
ed = []
graf = {}

while True:
	try:
		g.append(input().split())
	except EOFError:
		break

for x in range(1,len(g)):
	if not int(g[x][0]) in graf:
		graf[int(g[x][0])]=[]
	graf[int(g[x][0])].append(int(g[x][1]))	
	if not int(g[x][1]) in graf:
		graf[int(g[x][1])]=[]
	graf[int(g[x][1])].append(int(g[x][0]))	

# print(g2)
print(graf)
# print("graf : ")
maks = len(graf[1])
# for cari len terbesar
for i in range(1,len(graf)):
	# print(graf[i])
	if(maks < len(graf[i])):
		maks = len(graf[i])
		vc.append(i)
	maks = 1
	# for edges terkait dan hapus edgenya
	# for j in graf[i]:
	# 	print(graf[j])
	# 	graf[j].remove(i)

	# for u in range(0, maks):
		# graf[i].remove(u)
		# print(u)		
				# if(j == i):
	# graf[i].clear()	

# print(graf)

print("vertex cover : ")
for y in range(0, len(vc)):
	print(vc[y])

# print("delete edge : ")
for k in range(1,len(graf)):
	# print(graf[k])
	# for j in range(0, len(graf[k])):
	# 	print(graf[k][j])
	# 	print(vc[j])
	# 	if(graf[k][j] == vc[j]):
	# 		 print(graf[k][j])
	# 		 graf[k].remove([k][j])
	for j in graf[k]:
		graf[j].remove(k)
		# print(j)
		# for y in range(0, len(vc)):
		# 	# print(vc[y])		
		# 	if(j == vc[y]):
		# 		graf[k].remove(j)
		# 		print(j)

	graf[k].clear()

print(graf)





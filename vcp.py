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

print(graf)
maks = len(graf[1])
for i in range(1,len(graf)):
	print(graf[i])
	if(maks < len(graf[i])):
		maks = len(graf[i])
		vc.append(i)

		for j in graf[i]:
			# print(graf[j])
			graf[j].remove(i)

		maks = 1
# print(graf)
		graf[i].clear()	

print(graf)
for y in range(0, len(vc)):
	print(vc[y])
with open('star rating.txt', 'r', encoding='utf-8')as f:
    star_list = f.read().split('\n')
for i in range(5):
    star_list[int(i)] = star_list[i].split('#')
star_dict = {}
for i in range(5):
    star_dict[str(i[0])] = star_list[i[1]]
print(star_list)
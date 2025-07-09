city_list = ['서울', '대전', '대구', '서울', '부산', '광주', '부산']

print("*"*26)
city_set = set(city_list)
city_list = list(city_set)
city_list.sort()
print(city_list)
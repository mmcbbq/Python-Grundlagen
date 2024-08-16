# import requests
# from bs4 import BeautifulSoup as bs
# anagram = []
# for i in range(1,96):
# 	url = f'https://www.d-rhyme.de/anagramm-lexikon/seite-{i}/'
# 	req = requests.get(url)
# 	html_bs = bs(req.text, features="html.parser")
# 	html_tr_list = html_bs.find('table').find_all('td')
# 	for ele in html_tr_list:
# 		if len(ele.findChildren()) > 0:
# 			for ele_text in ele.findChildren():
# 				anagram.append(ele_text.text)
# 		else:
# 			anagram.append(ele.text)
# with open(r'C:\BBQ\Python\anagram.txt','w') as fp:
# 	for x in anagram:
# 		fp.write(x+'\n')
# print(anagram)


# words = ["lesen", "seeln", "hören", "renhö", "stein", "tines", "rat", "tar", "lieb", "blei", "gärtner", "rantger", "kragen", "garnek", "leben", "nebel", "lager", "regal"]
#
# anagram = []
# for index, word in enumerate(words):
#     sorted_word_list = sorted(word)
#     sorted_word = ''
#     for letter in sorted_word_list:
#         sorted_word += letter
#     for test_word_index in range(index + 1 , len(words)):
#         test_sorted_word_list = sorted(words[test_word_index])
#         test_sorted_word = ''
#         for letter in test_sorted_word_list:
#             test_sorted_word += letter
#         if test_sorted_word == sorted_word:
#             anagram.append([word,words[test_word_index]])
#
# print(anagram)
# # students_grades = {
# #     "Anna": [85, 78, 92],
# #     "Ben": [88, 90, 85],
# #     "Clara": [95, 91, 89],
# #     "David": [76, 85, 80],
# #     "Eva": [90, 88, 92],
# #     "Felix": [82, 77, 79],
# #     "Greta": [91, 93, 90],
# #     "Hanna": [84, 86, 88],
# #     "Isaac": [89, 87, 90],
# #     "Julia": [92, 94, 91],
# #     "Kevin": [78, 74, 80],
# #     "Lena": [85, 89, 87],
# #     "Max": [88, 92, 90],
# #     "Nina": [83, 79, 81],
# #     "Oscar": [80, 82, 85],
# #     "Paula": [91, 88, 90],
# #     "Quentin": [77, 73, 79],
# #     "Rita": [90, 85, 88],
# #     "Simon": [86, 89, 87],
# #     "Tina": [93, 91, 94]
# # }
# # for name ,liste in students_grades.items():
# #     summe = 0
# #     anzahl = 0
# #     for punkte in liste:
# #         summe += punkte
# #         anzahl += 1
# #     print(f'{name} hat eine Durchschnittsnote von {summe / anzahl}')
# #
# #
# list_a = ['a', 'b']
# list_b = ['b', 'a']
# print(list_a == list_b)

# 키와 값으로 이루어진 각 리스트를 조합해 하나의 딕셔너리를 만드세요
'''
[실행 결과]
{'name'}: '기사', 'hp':200, 'mp': 30, 'level': 5
'''


key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

i = 0
# key_list 반복
# len() 이용해서 반복문 만들기
while i <= len(key_list):
    character["key"] =  key_list[i]
    character["key"] = value_list[i]
    i += 1
    
print(character)

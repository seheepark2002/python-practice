# 딕셔너리 선언
dictionary = {
  "name": "박세희",
  "age": "25",
  "height": "172cm",
  "hobby": ["watching movie", "reading a book", "cooking"],
  "hometown": "Seoul"
}

# 출력하기
print("name: ", dictionary["name"])
print("age: ", dictionary["age"])
print("hobby: ", dictionary["hobby"])
print("hometown: ", dictionary["hometown"])

# 값 변경하기
dictionary["hometown"] = "Gumi"
print("hometown: ", dictionary["hometown"])
print("favorite hobby: ", dictionary["hobby"][0])


# dictionary 요소 제거하기 #del 키워드
dictionary = {
  "name": "박세희",
  "age": "25살",
  "hobby": "요리",
}

# 요소 삭제 전 출력
print("요소 삭제 이전: ", dictionary)

# 요소 삭제하기
del dictionary["hobby"]

# 요소 삭제 후 출력
print("요소 삭제 이후: ", dictionary)
# 키의 값을 추출해보자 #get() 함수
dictionary = {
  "name": "sehee",
  "age": "25",
  "hobby": "Cooking"
}

# 키 값에 접근하기
value = dictionary.get("name")

# 출력
print("name: ", value)
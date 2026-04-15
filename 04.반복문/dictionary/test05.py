# 키가 존재하는지 확인하고 값에 접근하기  #in 키워드
dictionary = {
  "name": "sehee",
  "age": "25",
  "hobby": "Cooking"
}

# 사용자로부터 입력 받기 "접근하고자 하는 키: "
key = input("접근하고자 하는 키: ")

# 입력받은 키가 존재한다면 출력, 그렇지 않으면 "존재하지 않는 키에 접근하고 있습니다." 출력
if key in dictionary:
  print(dictionary[key])
else:
  print("존재하지 않는 키에 접근하고 있습니다.")

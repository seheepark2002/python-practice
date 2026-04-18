# 반복문으로 피라미드 만들기(2)

output = ""

# 총 15행 반복하기
for i in range(0, 14):

    # 앞에 공백 행마다 반복 출력 
    for j in range(14, i, -1):
        output += " "
    # 별 반복해서 더하기 
    for k in range(0, (i * 2) + 1):
        output += "*"
    output += "\n"

print(output)

# break키워드 / comtinue 키워드
# 변수 선언하기
i = 0

# 무한 반복하기
while True:
    # 몇 번째 반복인지 출력하기
    print(f"{i}번째 반복문입니다")
    i += 1
    # 반복 종료
    input_text = input("종료하시겠습니까?(y/n): ")
    if input_text in ["y", "Y"]:
        print("반복을 종료합니다")
        break
    
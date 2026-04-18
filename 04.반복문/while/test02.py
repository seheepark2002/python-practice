# 상태를 기반으로 반복하기
# 변수를 선언합니다
from turtle import listen


list_test = [1,2,1,2]
value = 2

# list_test 내부에 value가 있다면 반복
while value in list_test:
    list_test.remove(value)
    
# 출력
print(list_test)
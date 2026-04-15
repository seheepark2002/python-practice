# 수식에 나누기 연산자를 사용한 경우
n = 10
# a = range(0, n / 2)
# 타입에러가 뜸.  range함수의 매개변수로는 반드시 정수를 입력해야 함

# a = range(0, int(n / 2)) 이것보다
a = range(0, int(n // 2)) #이걸 더 많이 사용함

print(list(a))
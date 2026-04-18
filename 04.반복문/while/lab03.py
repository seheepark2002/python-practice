# 1부터 100까지의 숫자가 있을 때, 1 * 99, 2 * 98, 3 * 97, ... , 99 * 1 와 같이 계산한다고 했을 때, 최대가 되는 경우는 어떤 숫자를 곱했을 때인지 찾아라
max_value = 0
a = 0 
b = 0

for i in range(1, 100 + 1):
    j = 100 - i
    
    # 최댓값 구하기
    # i * j  결과 sum으로 두고 max_value보다 크면 대입하기
    sum = i * j
    if sum > max_value:
        a = i
        b = j
        max_value = sum
        
print(f"최대가 되는 경우: {a} * {b} = {max_value}")
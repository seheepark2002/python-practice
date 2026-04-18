# 시간을 기반으로 반복하기
import time

# 변수 선언
num = 0

# 5초 동안 반복
target_tick = time.time() + 5
while time.time() < target_tick:
    num += 1

# 출력
print(f"5초 동안 {num}번 반복했습니다")
import sys

# 1 부터 n 까지의 수들 중에서 모든 소수를 찾는 방법: 에라토스테네스의 체
# n 의 루트를 구하는 방법: [1] n**(1/2) [2] Math.sqrt(n)
# n 이 소수인지 판단하는 방법: 2 부터 루트n 까지의 소수들로 나누어 떨어지지 않으면 소수
#
# 본 문제에서는 1000000 이하의 자연수 중에서 소수를 찾기 때문에 "에라토스테네스의 체" 방식을 사용한다.
def solution(m: int, n: int) -> None:
    # "에라토스테네스의 체" 구성
    sieve: list = [num+1 for num in range(n)]

    # 1 은 소수가 아니니 제외
    sieve[0] = 0

    # "에라토스테네스의 체" 에서 소수가 아닌 놈들 제외
    for num in sieve:
        if num == 0:
            continue

        position: int = num-1

        for inner_num in sieve[num:]:
            position += 1

            if inner_num == 0:
                continue

            if inner_num%num == 0:
                sieve[position] = 0

    # 출력
    if m == n:
        print([m-1])
    else:
        for num in sieve[m-1:n-1]:
            if num == 0:
                continue
            print(num)

# Input 오류는 고려하지 않는다.
if __name__ == '__main__':
    input_data = sys.stdin.readline().rstrip().split(' ')
    solution(int(input_data[0]), int(input_data[1]))

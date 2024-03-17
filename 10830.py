import sys
N, B = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

def matrix_multiply(A, B):
    # 곱셈 결과를 저장할 2차원 리스트 생성
    result = [[0] * N for _ in range(N)]
    # 행렬 곱셈 연산 수행
    for row in range(N):
        for col in range(N):
            s = sum(A[row][i] * B[i][col] for i in range(N))
            result[row][col] = s % 1000
    # 결과 반환
    return result

def divide(n, arr):
    if n == 1:
        return arr
    if n % 2 == 0: # B 짝수
        half = divide(n // 2, arr)
        return matrix_multiply(half, half)
    else: # B 홀수
        return matrix_multiply(arr,  divide(n - 1, arr))

for row in divide(B, arr):
    print(*[r % 1000 for r in row])
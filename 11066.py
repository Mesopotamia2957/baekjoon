# import heapq
# T = int(input())
# for _ in range(T):
#     # 0. 초기화
#     answer = 0
#     K = int(input())
#     File = list(map(int, input().split()))
#
#
#
#     # 크기가 작은 파일 끼리 병합 반복
#     while len(File) > 1:
#         # 최소 힙 구성
#         heapq.heapify(File)
#         a = heapq.heappop(File)
#         b = heapq.heappop(File)
#         merged_scale = a + b
#         answer += merged_scale
#         heapq.heappush(File, merged_scale)
#
#     # 정답 출력
#     print(answer)


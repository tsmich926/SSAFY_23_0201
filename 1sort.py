# def bubble_sort(array):
#     """ Best: O(n^2) Average: O(n^2) Worst: O(n^2) | O(n) """
#     for i in range(len(array)):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array

# 55 7 78 12 42
# for i : N-1 >> 1
#     for j : 0 >> i-1
#         if arr[j] > arr[j+1]
#             arr[j] <> arr[j+1]

N =  int(input())
arr = list(map(int,input().split()))
for i in range(N-1, 0 , -1): #각 구간의 끝
    for j in range(i): #비교할 왼쪽 원소
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(*arr)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    MaxV = arr[0]  #첫원소를 최대로 가정
    for i in range(1,N): #나머지 원소와 비교
        if maxV  < arr[i]:
            maxV = arr[i]
    print(f'#{tc} {maxV}')
nums= [55,7,78,12,42]
#작은 수에서 큰 수로 정렬
N = 5
i= 4 로 78을 보낸다
i= 4:
    [55,7,78,12,42] 0-1:[7,55,78,12,42]
    [7,55,78,12,42] 1-2 [7,55,78,12,42]
[7,55,78,12,42] 2-3 : [7,55,12,78,42]
[7,55,12,78,42] 3-4: [7,55,12,42,78]

i=3:
    [7,55,12,42,78] 0-1:[7,55,12,42,78]
    [7,55,12,42,78] 1-2 :[7,12,55,42,78]
    [7,12,55,42,78] 2-3: [7,12,42,55,78]

i = 2:

i=1:

i=0:

i=i
for i in range(N-1,0,-1):
    for j in rage(0,1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(nums)

#왼쪽부터 채우려면?
#자율실습> 0번째부터 채운다면 작은수에서 큰수로 버블 정렬
for i in range(0,N-1,1):
    for j in range(0,1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]

#i번째 위치의 데이터 최댓값?




arr = [1, 2 ,3, 4, 5]

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1): #i번째 인덱스에서의 최댓값을 결정하기
        for j in range(i): # 두수끼리 비교해서 최댓값을 결정해나감
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sort(arr)

for i in range(3,0,-1):
    print(i)
#temp 변수
a = 10
b = 5

# t = a
# a = b
# b = t
(a,b) = (b,a)

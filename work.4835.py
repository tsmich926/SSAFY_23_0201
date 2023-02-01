# 3개의 합이면 인덱스0,1,2의 합이므로 
# 이웃한 M개의 합을 구하려면
N=10
M=3
ai = [1 ,2 ,3, 4, 5, 6, 7, 8, 9 ,10]
for i in range(0,(N+1)//2,1): 
    for k in range(i,(i+M)-1,1):
        print(ai[i])
        
N=4
M=2
1 ,2 ,3, 4 짝수는  N//M 홀수는 N+M//2
1,2,3,4,5
N=8
M=3
1,2,3,4,5,6!,7,8
1,2,3,4,5,6,7!,8,9

끝 인덱스에서 M-1만큼 떨어진값(M에는 끝값인 자기자신도 포함)이 마지막 인덱스가 된다

for mm in range(N-M+1): 0 1 2
    for i in range(mm):
        for i in range(i,(i+M)-1,1):
            v[i]

N = 5
M = 3
[1,2,3,4,5]
123
234
345
----------
TC = int(input())
for t in range(1, TC+1):
    N,M = list(map(int,input().split()))
    v = list(map(int,input().split()))

    for i in range(N-M+1):
        for j in range(M):
            sumV += V[i+j]

# N =5
# M =3
# v =[1,2,3,4]
# for i in range(N-M+1):
#     for k in range(i,i+M-1,1):
#         v[k]

# N =5
# M =3
# v =[1,2,3,4]
# for i in range(N-M+1):
#     for k in range(i,i+M-1,1):
#         sumV += v[k]
""""""""""""""""""""
TC = int(input())
for t in range(1, TC+1):
    N,M = list(map(int,input().split()))
    v = list(map(int,input().split()))

    lst = [0] * (N-M+1)
    for i in range(N-M+1):
        sumV = 0
        for j in range(M):
            sumV += v[i+j]
            lst[i] = sumV
    # print(lst)
    min_V = lst[0]
    max_V = lst[0]
    for k in lst:
        if min_V > k:
            min_V = k
        if max_V < k :
            max_V = k
    sub_V = max_V-min_V
    print(f'#{t} {sub_V}')
        
"""""""""""""""""""""""""""""" 

#!sw Exper Academy 4828 minmax
# T = int(input())
# for i in range(1,T+1):
#     N = int(input())
#     ai = list(map(int,input().split()))
#     print(N, ai)
#     pmax = ai[0]
#     pmin = ai[0]
#     for i in range(N-1):
#         if pmax < ai[i+1]:
#             curmax = ai[i+1]
#             curmin = ai[i]
#         else:
#             pmax = ai[i]
#             pmin = ai[i+1]
    # print(type(min), type(max))
        # if ai[i] > ai[i+1]:
        #     min = ai[i+1]
        # else:
        #     min = ai[i]
    # print(max,min)
    # sub = max - min 
    # print(sub)
""""""""""""""""""""""""
T = int(input())
for K in range(1,T+1):
    N = int(input())
    ai = list(map(int,input().split()))
    # print(N, ai)
    pmax = ai[0]
    pmin = ai[0]
    for i in range(N-1):
        if pmax < ai[i+1]:
            pmax = ai[i+1]
        if pmin > ai[i+1]:
            pmin = ai[i+1] 
    sub = pmax - pmin
    print(f'#{K} {sub}')  #출력 맞춰줘야 함

    """"""""""""""""""""""""""
    import sys
    sys.stdin = open("파일이름.txt","r")

    TC = int(input())
    for r in range(1, TC+1):
        N = int(input())
        ai = list(map(int,input().split()))
    curMaxV = 0
    curminV = 1000000
    for num in ai:
        if curMaxV < num :
            curMaxV = num
        if curminV > num :
            curminV = num
    print(curminV)
    print(curMaxV)
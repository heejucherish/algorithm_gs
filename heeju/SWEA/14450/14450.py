'''
3
35 267 3
40 27 247
1 199999 3
2 3 4
97 1230 4
96 10 11 12
'''
import sys
sys.stdin = open('./sample_input.txt')
T = int(input())


def len_math(n):
    lenght= 0
    first_num = 0 
    while n >0:
        if n <10:
            first_num = n
            break 
        
        n //= 10 
        lenght +=1
        
    return (lenght, first_num)

for tc in range(1, T+1):
    L, R, Q = list(map(int, input().split()))
    Q_list = list(map(int, input().split()))
    l_list = str(L)
    r_list = str(R)
    key = []
    l_lenght,l_first = len_math(L)
    print(l_lenght+1,l_first)
    r_lenght, r_first = len_math(R)
    print(r_lenght+1,r_first)

    for i in range(Q):
        A = len(str(Q_list[i]))
        # if l_lenght <= 
        
        # print(A)
        # if int(l_list[:A]) <= int(str(Q_list[i])[:A]) <= int(r_list[:A]):
        #     res = 'O'
        #     key.append(res)
        # else:
        #     res = 'X'
        #     key.append(res)
    print(f'#{tc}', ''.join(key))
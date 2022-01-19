def homework():
    num = input()
    num = int(num)
    answer = {}
    for n in  range(1 , num+1):
        answer[n] = n * n
    print(answer)
homework()

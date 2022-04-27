# i번 부터 j번째까지 숫자를 자르고 정렬했을 때
# k번째 있는 수를 구하고자 한다

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        newarray = array[commands[i][0]-1:commands[i][1]]
        newarray.sort()
        answer.append(newarray[commands[i][2]-1])
    return answer

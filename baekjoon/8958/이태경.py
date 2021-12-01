# 백준_1차원 배열_OX퀴즈
# https://www.acmicpc.net/problem/8958

import sys
input = sys.stdin.readline

n = int(input())            # test case 개수

for _ in range(n):                 # n 만큼 반복
    ox_list = list(input()) # 입력 받은 OX를 리스트에 저장
    score = 0               # 점수 초기화
    sum_score = 0           # 총 점수 초기화

    for ox in ox_list:      # ox_list 만큼 반복하고 각각을 ox에 저장
        if ox == 'O':       # ox가 'O'이라면
            score += 1      # 'O'가 나올 때 마다 1점씩 추가
            sum_score += score  # score를 최종 점수에 합산
        else:
            score = 0       # 'O'가 아니라면 0점 처리
    print(sum_score)

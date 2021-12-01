# 백준_1차원 배열_평균은 넘겠지
# https://www.acmicpc.net/problem/4344

import sys
input = sys.stdin.readline

c = int(input())    # 테스트 케이스 개수

for _ in range(c):  # c만큼 반복
    n = list(map(int, input().split()))  # 학생 수 및 점수들을 리스트에 담기
    avg = sum(n[1:]) / n[0]   # index[0] == 학생 수, index[1:] == 점수들
    cnt = 0
    for score in n[1:]:  # 점수 각각을 score에 선언
        if score > avg:     # 점수가 평균보다 높다면
            cnt += 1        # 평균 이상인 학생 수 카운트
    rate = cnt / n[0] * 100 # 평균 이상 학생 수 / 학생수 * 100 == 평균 이상인 학생의 비율

    print(f'{rate:.3f}%')   # f-string 문법으로 rate 변수를 받고
                            # ':'구분자를 써서 '.3f' 소수점(float) 3자리 까지 출력

# 백준_1차원 배열_평균
# https://www.acmicpc.net/problem/1546

import sys
input = sys.stdin.readline                 # 하운님 팁

n = int(input())                           # 시험 본 과목의 총 개수
m = list(map(int, input().split()))        # 세준이의 현재 성적들을 리스트에 담음
maxScore = max(m)                          # 리스트에 담긴 성적 중에서 최고 점수

newList = []                               # 빈 리스트 생성
for score in m:
    newList.append(score / maxScore * 100) # 새로운 점수 생성 후에 빈 리스트에 담기

newAvg = sum(newList)/n                    # 리스트에 담긴 점수들을 n으로 나누기
print(newAvg)

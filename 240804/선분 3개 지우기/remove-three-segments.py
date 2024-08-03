n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
cnt = 0

# 가능한 모든 3개의 선분 조합을 순회
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 3개의 선분을 제거하고 남은 선분 리스트 생성
            remaining_segments = [
                segments[m] for m in range(n)
                if m != i and m != j and m != k
            ]
            
            # 남은 선분들이 겹치지 않는지 확인
            non_overlapping = True
            for a in range(len(remaining_segments)):
                for b in range(a + 1, len(remaining_segments)):
                    seg1 = remaining_segments[a]
                    seg2 = remaining_segments[b]
                    if not (seg1[1] <= seg2[0] or seg2[1] <= seg1[0]):
                        non_overlapping = False
                        break
                if not non_overlapping:
                    break
            
            # 겹치지 않는다면 경우의 수 증가
            if non_overlapping:
                cnt += 1

# 결과 출력
print(cnt-1)
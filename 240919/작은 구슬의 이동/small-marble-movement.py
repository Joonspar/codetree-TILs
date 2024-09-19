# 뒤집기 ? (격자)
# 상하좌우 중 한 방향으로 이동중 
# 끝에 도착하면 방향이 바뀌면서 되돌아감...1초에 한 칸씩 움직인다 했음.
# 방향을 90도가 아니라 180도 바꿔야함
# 0 , 1 , 2 , 3의 각자 합이 맞는 것을 pair로 정의함.
# 0과 3 , 1과 2를 짝으로 정한다. 
# dir = 3 - dir...
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
n,t = map(int,input().split())
sections = [
    [0 for _ in range(n)]
    for _ in range(n)
]
dxs , dys = [0,1,-1,1] , [1,0,0,-1]
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n
r,c,d = input().split()
d = mapper[d]
r , c = int(r) , int(c)
for _ in range(t):
    nr = r + dxs[d]
    nc = c + dys[d]

    if in_range(nr,nc):
        r , c = nr , nc
    else:
        d = 3 - d
print(c,r)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = {'up':[0,1,'left','right'],
                     'down':[0,-1,'right','left'],
                     'left':[-1,0,'down','up'],
                     'right':[1,0,'up','down']}
        x,y = 0,0
        dir = 'up'
        ans = 0
        obstacles = set(map(tuple, obstacles))
        for cmd in commands:
            if cmd > 0:
                for _ in range(cmd):
                    if (x + direction[dir][0],y + direction[dir][1]) not in obstacles:
                        x += direction[dir][0]
                        y += direction[dir][1]
                        ans = max(ans,x**2 + y**2)#求解最大 eucd, for in range 后面+=的次数为 range 中的数值
                    else:
                        break
            if cmd<0:
                if cmd == -1:
                    dir = direction[dir][3]
                if cmd == -2:
                    dir = direction[dir][2]
        return ans
import sys
import heapq

n = input()
day = 0
barn = []
total_size = 0

for _ in range(n):
    instruction = map(int, sys.stdin.readline().strip().split())
    if instruction[0] == 1:
        heapq.heappush(barn, (instruction[2]+day, instruction[1]))
        total_size += instruction[1]
    elif instruction[0] == 2:
        need = instruction[1]
        if need <= total_size:
            while need > 0:
                if need >= barn[0][1]:
                    deduct = heapq.heappop(barn)[1]
                    need -= deduct
                    total_size -= deduct
                else:
                    barn[0] = (barn[0][0], barn[0][1] - need)
                    total_size -= need
                    need = 0
            
            print("yes")
        else:
            print("no")
    elif instruction[0] == 3:
        day += 1
        while barn and barn[0][0] <= day:
            total_size -= heapq.heappop(barn)[1]
    else:
        if barn:
            print(barn[0][0] - day)
        else:
            print(0)

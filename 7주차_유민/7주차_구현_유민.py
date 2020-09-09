def add_modi(position, ladder, case, modi, H):
    if len(case) == 3:
        return

    h = position*H

    while True:
        if ladder[h] != 0:
            h += ladder[h]
        elif ladder[h] == 0:
            if h-H > 0 and ladder[h-H] == 0:
                case.append(h-H)
                modi.append(list(case))
                case.pop()

            if (h+H) // H < N and ladder[h+H] == 0:
                case.append(h)
                modi.append(list(case))
                case.pop()
        h += 1
        if h % H == 0:
            break
    return

def ladder_slip(position, ladder, case, H):
    h = position*H
    while True:
        if ladder[h] != 0:
            h += ladder[h]
        h += 1
        if h % H == 0:
            break
    return (h-1) // H

N, M, H = map(int, input().split(' '))
ladder = []
[ladder.append(0) for j in range(N*H)]
for k in range(M):
    i, j = map(int, input().split(' '))
    ladder[i-1 + (j-1)*H] = H
    ladder[i-1 + j*H] = -H
modi_position = []
position_cnt = 0
for position in range(N):
    if position != ladder_slip(position, list(ladder), [], H):
        break
    position_cnt += 1
if position_cnt == N:
    print(0)
else:
    add_modi(position, ladder, [], modi_position, H)
    success = 4
    position_cnt = 0
    while modi_position != []:
        case = modi_position.pop(0)
        position_cnt = 0
        temp_ladder = list(ladder)
        if len(case) >= success:
            continue
        for loc in case:
            temp_ladder[loc] = H
            temp_ladder[loc + H] = -H
        for position in range(N):
            if position != ladder_slip(position, temp_ladder, case, H):
                break
            position_cnt += 1
        if position_cnt != N:
            add_modi(position, temp_ladder, case, modi_position, H)
        else:
            success = len(case)
            print(success)
            break
    if success == 4:
        print(-1)
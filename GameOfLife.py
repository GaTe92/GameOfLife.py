#by Gabriel Teuchert

import random as rd

width = 5
height = 5
dead_state = []


def DState(dh, dw):  # initialize input
    dstate = []
    zero = [0] * dw
    for _ in range(dh):
        dstate.append(zero)
    dstate = [sublist[:] for sublist in dstate]  # no sublists in list
    return dstate


def RState(rh, rw):  # randomize input matrix
    rstate = DState(rh, rw)
    for i in range(rh):
        for ii in range(rw):
            random_number = rd.random()
            if random_number >= 0.5:
                rstate[i][ii] = 0
            else:
                rstate[i][ii] = 1
    return rstate


def Render(state, sh, sw):                                          # output creator
    plot = ["-------\n"]
    for i in range(sh):
        plot.append("|")
        for ii in range(sw):
            if state[i][ii] == 0:                                   # 0 or dead state equals space
                plot.append(".")
            else:
                plot.append("#")                                    # 1 or live state equals hashtag
        plot.append("|\n")
    plot.append("-------")
    print(''.join(plot))


def RulesOfLive(cstate, sum):                              # cellstate True = live ; cellstate False = dead
    if sum <= 1 and cstate is True:                        # underpopulation
        cstate = False
        return cstate
    if sum <= 3 and cstate is True:                        # just right
        cstate = True
        return cstate
    if sum > 3 and cstate is True:                         # overpopulation
        cstate = False
        return cstate
    if sum == 3 and cstate is False:                       # reproduction
        cstate = True
        return cstate
    elif cstate is True:                                   # none of the conditions above remain current state
        cstate = True
        return cstate
    elif cstate is False:                                  # remain current state
        cstate = False
        return cstate


def NextBordState(state, nh, nw):
    nstate = DState(nh, nw)
    for i in range(nh):                                                 # list indices start with 0
        for ii in range(nw):
            kernel = []
            for x in range(i - 1, i + 2):
                if x < 0 or x >= nh:
                    for _ in range(3):                                    # because first or last row, no upper elements
                        kernel.append(-1)
                else:
                    for y in range(ii - 1, ii + 2):
                        if y < 0 or y >= nw:
                            kernel.append(-1)
                        else:
                            kernel.append(state[x][y])
            cstate = kernel.pop(4)                                           # cell state
            if cstate == 1:
                cstate = True
            else:
                cstate = False
            kernel = list(filter(lambda num: num != -1, kernel))             # delete all -1
            cellstate = RulesOfLive(cstate, sum(kernel))
            if cellstate is True:
                nstate[i][ii] = 1
            else:
                nstate[i][ii] = 0
    return nstate


random_state = RState(height, width)                            # create an instance
Render(random_state, height, width)                             # create plot
next_state = NextBordState(random_state, height, width)         # evolution
Render(next_state, height, width) 
for _ in range(3):
    next_state = NextBordState(next_state, height, width)
    Render(next_state, height, width)                           # rendering again

import pandas as pd
import numpy as np

def append_name(Day_Schedule, time, day, name):
    if Day_Schedule.at[time,day] == 'x':
        Day_Schedule.at[time,day] = name
    else:
        new_value = Day_Schedule.at[time,day] + ',' +name
        Day_Schedule.at[time,day]=new_value

def pre_backtrack(Dict,Name):

    Day=['월','화','수','목','금','토','일']
    Part=['manager','hall','kitchen']
    Time=['open','mid','close']
    Day_Schedule = pd.DataFrame({'월' :['x','x','x'],'화' :['x','x','x'],'수' :['x','x','x'],
                             '목' :['x','x','x'],'금' :['x','x','x'],'토' :['x','x','x'],
                             '일' :['x','x','x']}, index=['open','mid','close'])
    for i in Name:
    #print('Name : ', i)
        for j in Part:
            if j in Dict[i]: # Manager -> hall -> kitchen 순으로 검사
                #print("Part : ", j)
                #print("Day : ", end=' ')
                for k in Day:
                    if k in Dict[i][j]:
                        #print(k,end=', ')
                        for e in Time:
                            if e in Dict[i][j][k]:
                                #print(e, end=' ')
                               # Day_Schedule[j][k]=i # 이런식으로 input 해주면 될듯.
                                append_name(Day_Schedule, e, k, i)
    return Day_Schedule
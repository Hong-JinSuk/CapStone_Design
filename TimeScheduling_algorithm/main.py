from 알바생_옵션입력 import employ_info
from 시간표_수요조사 import pre_backtrack
from 시간표_사전배치 import pre_place
import pandas as pd
import numpy as np

if __name__=="__main__":

    Dict, Name_list = employ_info() # 직원 정보 집합, 직원 이름 리스트
    # Info = name -> part -> time 순으로 되어있다.
    # Name_list = name : 주 몇일 으로 되어있다.

    isvisited = [[False]*3]*7 # open,mid,close * 7(월~일)
    
    hall_Schedule = pre_backtrack(Dict,Name_list)

    isvisited, hall_Schedule = pre_place(hall_Schedule, isvisited)

    print(Day_Schedule)

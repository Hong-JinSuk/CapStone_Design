from 알바생_옵션입력 import employ_info
from 시간표_수요조사 import pre_backtrack
import pandas as pd
import numpy as np

if __name__=="__main__":

    Dict, Name_list = employ_info() # 직원 정보 집합, 직원 이름 리스트
    Day_Schedule = pre_backtrack(Dict,Name_list)

    print(Day_Schedule)

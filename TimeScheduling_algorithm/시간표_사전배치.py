import pandas as pd

def pre_place(Day_Schedule, isvisited):
    new_isvisited = pd.DataFrame(False, index=Day_Schedule.index, columns=Day_Schedule.columns)
    
    for col in Day_Schedule.columns:
        for row in Day_Schedule.index:
            values = Day_Schedule.loc[row, col].split(',')
            
            if len(values) > 1:
                Day_Schedule.loc[row, col] = ','.join(values)
            elif len(values) == 1:
                new_isvisited.loc[row, col] = True
                
                # 같은 열에 같은 이름을 갖는 원소 제거
                for other_row in Day_Schedule.index:
                    if other_row != row:
                        other_values = Day_Schedule.loc[other_row, col].split(',')
                        if values[0] in other_values:
                            other_values.remove(values[0])
                            Day_Schedule.loc[other_row, col] = ','.join(other_values)
    
    # 이름이 모두 없어진 칸을 'x'로 변경
    for col in Day_Schedule.columns:
        for row in Day_Schedule.index:
            if len(Day_Schedule[col][row]) == 0:
                Day_Schedule[col][row] = 'x'
    
    # 기존 isvisited와 새로운 isvisited가 같은지 확인
    if new_isvisited.equals(isvisited):
        return isvisited, Day_Schedule
    
    # 새로운 isvisited로 재귀 호출
    return pre_place(Day_Schedule, new_isvisited)
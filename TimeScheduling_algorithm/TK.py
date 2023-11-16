import tkinter as tk
from tkinter import ttk
import pandas as pd
import sys
import heapq
import random

Days=['월','화','수','목','금','토','일']
Times=['open','mid','close']
my_schedule = None  # 전역으로 선언한 my_schedule

def generate_store_data(num):
    
    columns = ['월', '화', '수', '목', '금', '토', '일']
    index = ['open', 'mid', 'close']
    store_data_list = []

    for i in range(1,num+1):
        # 무작위로 True 또는 False 값을 생성하여 데이터 프레임을 만듭니다.
        data = [[random.choice(["가능", "불가능"]) for _ in columns] for _ in index]

        # 데이터 프레임 생성
        timetable_df = pd.DataFrame(data, columns=columns, index=index)

        store_name = f'가게 {i}'

        # 거리를 100미터에서 2000미터 사이에서 무작위로 생성
        distance = random.randint(100, 2000)

        # 시급을 무작위로 생성
        hourly_wage = random.randint(10, 15) * 1000

        # 10개의 가게 데이터 생성
        store_data_list.append([store_name,timetable_df,distance,hourly_wage])
    
    return store_data_list

def Schedule_Score(Schedule_table, Worker_table, Len, money):
    # 가중치 설정, 만약에 open mid 일할 수 있는데, open만 < open and mid 가 높게
    # 즉 짧게 일하는게 여러날보다는 길게 일하는게 몇 일 안되는게 좋음!!
    score=0 # 이 점수가 높은 순이 좋음
        
    for day in Schedule_table.columns:

        weight=1
        weight_list=0
        for time in Schedule_table.index:
            # 연속되는 날일 수록 *2로 가중치를 늘려줌
            if str(Schedule_table.loc[time, day]) == "가능" and str(Worker_table.loc[time, day]) == "가능":
                weight*=2
                #print(f"Day: {day}, Time: {time}")
            # 연속적인 일이 끊기면 가중치 더해줌.
            if (str(Schedule_table.loc[time, day]) == "불가능" or time == Schedule_table.index[-1]) and weight > 1:
                score+=weight
                weight=0
    score += (((money/9600) * 5) - (Len/100))
    return -score, Schedule_table

def save_schedule(root,entry_widgets):
    #root.destroy()
    root=tk.Tk()
    root.title("스케쥴 입력")
    global my_schedule
    my_schedule = pd.DataFrame("불가능", index=Times, columns=Days)  # 초기화
    # Days(요일) 레이블 생성
    for j, day in enumerate(Days):
        day_label = tk.Label(root, text=day)
        day_label.grid(row=0, column=j + 1)

    

    for i, time in enumerate(Times):
        time_label = tk.Label(root, text=time)
        time_label.grid(row=i + 1, column=0, padx=(5, 0))
        for j, day in enumerate(Days):
            entry = tk.Entry(root)
            entry.grid(row=i + 1, column=j + 1)
            entry_widgets[i][j] = entry

    next_button = tk.Button(root, text="저장 완료", command=lambda: next_1(my_schedule, entry_widgets, root))
    next_button.grid(row=len(Times) + 1, columnspan=len(Days) + 1, pady=10)
    
def next_1(my_schedule, entry_widgets, root):
    root.withdraw()  # 현재 창 숨김
    new_window = tk.Toplevel(root)  # 새 창 열기
    for i, time in enumerate(Times):
        for j, day in enumerate(Days):
            entry_value = entry_widgets[i][j].get()
            if entry_value == '1':
                my_schedule.loc[time, day] = "가능"

    new_window.title("스케쥴 출력")
    
    tree=ttk.Treeview(new_window,columns=list(my_schedule.columns), show='headings')
    for column in my_schedule.columns:
        tree.heading(column, text=column)
        tree.column(column, width=100)

    # DataFrame 데이터를 Treeview에 추가
    for row in my_schedule.itertuples(index=False):
        tree.insert("", "end", values=row)

    tree.grid()

    root.mainloop()

def Recommand(root, Schedule_table_list, my_schedule): # 거리랑, 시급, 알바 시간표 모두 출력해야함
    root=tk.Tk()
    root.title("가게 추천 페이지")

    treeview = ttk.Treeview(root, columns=Days, show="headings", height=30)
    
    for col in Days:
        treeview.heading(col, text=col)
        treeview.column(col, width=200)

    shop_rankings=[]
    
    for shop_info in Schedule_table_list:
        Name=shop_info[0]
        df=shop_info[1]
        Len=shop_info[2]
        money=shop_info[3]
        Score, Shop_Table = Schedule_Score(df, my_schedule, Len, money)
        print(Score)
        if Score in shop_rankings:
            Score+=0.1

        heapq.heappush(shop_rankings, (Score,Shop_Table,Name,Len,money))
        
    Index=1
    while shop_rankings:
        shop_ranking = heapq.heappop(shop_rankings)
        Score, df, Name, Len, money = shop_ranking[0], shop_ranking[1], shop_ranking[2], shop_ranking[3], shop_ranking[4]
        treeview.insert("", "end", values=["{},거리(m):{},시급:{}".format(Name, Len, money)])
        for time in Times:
            values = [str(df.loc[time,day]) for day in Days]
            treeview.insert("", "end", values=values)
        Index+=1

    treeview.grid()
    
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("내 옵션 입력")
    root.geometry("400x360+100+100")
    root.resizable(True, True)

    label = tk.Label(root, text="메뉴")
    label.grid(row=0, column=0)
    label.config(font=("Arial", 13))
    Schedule_table_list=generate_store_data(10)
    
    my_schedule = pd.DataFrame("불가능", index=Times, columns=Days)
    entry_widgets = [[None] * len(Days) for _ in range(len(Times))]

    # 저장 버튼 생성
    save_button = tk.Button(root, text="스케쥴 입력&수정", command=lambda: [save_schedule(root, entry_widgets)])
    save_button.grid(row=len(Times) + 1, columnspan=len(Days) + 1, pady=10)
    
    # 추천 버튼 생성
    Recommand_button=tk.Button(root, text="가게 추천", command=lambda : [Recommand(root, Schedule_table_list, my_schedule)], width =15)
    Recommand_button.grid(row=len(Times) + 2, columnspan=len(Days) + 1, pady=10)

    # 종료 버튼
    end_button=tk.Button(root, text="종료", command=exit, width=15)
    end_button.grid(row=len(Times)+3, columnspan=len(Days)+1, pady=10)

    root.mainloop()
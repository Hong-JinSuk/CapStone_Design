def input_name(Name_list):
    print('이름을 입력해 주세요 :', end=' ')
    Name = input()
    Name_list.append(Name)
    return Name, Name_list

def input_part():
    print('파트를 입력해 주세요 :', end =' ')
    Part = input()
    return Part

def input_DayTime():
    DayTime={}
    for i in range(1):
        print('일하는 날을 입력해주세요 :', end=' ')
        Day=input()
        print('일하는 시간을 입력해주세요 :', end=' ')
        Time=list(input().split())
        DayTime[Day]=Time
    return DayTime

def make_dict(Name,Part,DayTime):
    return {Part : DayTime}

def employ_info():
    print("직원 수를 입력해 주세요 : ")
    Case = int(input()) # Case = 사람 수
    Dict={}
    Name_list=[]

    for i in range(Case):
        Name, Name_list = input_name(Name_list)
        Part = input_part()
        DayTime = input_DayTime()
        Dict[Name] = make_dict(Name, Part, DayTime)

    return Dict, Name_list

# if __name__=="__main__":

#     Dict , Name_list= main() # 개개인의 옵션이 저장되 시간표 트리
#     print(Name_list)
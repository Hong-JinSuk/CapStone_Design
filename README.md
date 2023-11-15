# :computer: CapStone_Design

### :school: ChungBukNationalUniversity - ComputerEnginnering
<br></br>

:calendar: Since 2023-03-20 ~ ongoing
<br></br>

:two_men_holding_hands: Member Info

- [Hong-JinSuk](http://github.com/Hong-JinSuk) - CBNU_ComputerEnginnering, [E-mail](n9805h@naver.com) : n9805h@naver.com
- [ByeongJun-Jang](http://github.com/ByeongJun-Jang) - CBNU_ComputerEnginnering, [E-mail](qudwns8616@gmail.com) : qudwns8616@gmail.com
- [Junho-Yoo](https://github.com/junhoyoo00) - CBNU_ComputerEnginnering, [E-mail](juno2744@naver.com) : juno2744@naver.com
- [Juhyub-Lee](https://github.com/dlwnguq1101) - CBNU_ComputerEnginnering, [E-mail](dlwnguq1101@naver.com) : juno2744@naver.com
<br></br>
#### :study: Activity
- [x] 3/13 team meeting
- [x] 3/20 Topic selection
- [x] 3/27 preparing for presentation
- [x] 4/3 PPT presentation
- [x] 4/8 algorithm function setting
- [x] 4/28 feedback by professor
- [x] 5/1 Submission of mid-course
- [x] 7/1~8/31 Django Study & Deployment and Recommendation Algorithm Study
- [x] 10/1~10/17 User Interface Renewal & Implementation of features
- [x] 11/2 College of Electrical & Computing Engineering Capstone Design Exhibition
- [x] 11/9 Final PPT presentation

<br></br>
  Model Compositoin
```
Accounts { // ceo_accounts 동일
	id: number;        
	username: string;  
	useremail: string; 
  password: string;  
  created_at: date;  
}

Boards {  // ceo_boards 동일
    id: number;       
    contents: string; 
    title: string;    
    writer:; 
    created_at: date; 
    updated_at: date; 
}

Timetable{  // ceo_timetable 동일
  id: number;
  username: string;
  open_mon: boolean;
  mid_mon: boolean;
  '''
  '''
  '''
  mid_sun: boolean;
  close_sun: boolean;
}
```

Environments
```
python3 --version
Python 3.10.7

python3 -m django --version
4.2.5
```

Project
```
project capde
-------------
capde
├── capde
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── accounts
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── ceoaccounts
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── boards
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── ceoboards
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── profileapp
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── timetable
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
└── ceotimetable
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── forms.py
    ├── tests.py
    ├── urls.py
    └── views.py
```
    
Execution
```
> cd capde

> python3 manage.py runserver
```

money = float(input('輸入你想投入的本金：'))
year = int(input('輸入你想投資的期限：'))
rate = float(input('輸入投資的年化收益率: '))
mm = int(input('''0.每日 1.每月 3.每3月 6.每6月 12.每年 選擇複利方式： '''))
 

def day_return(money,year,rate=0.06):
    '方案：每日利息加入本金複投'
    for y in range(year):
        for day in range(365):
            money = money*rate/365 + money
        print('第%d年结束時，本利合計：%.2f' % (y+1,money))

def new_func(): 
    return 0.06
 
def month_return(money,year,mm,rate=0.06):
    '方案：每月利息加入本金複投'
    for y in range(year):
        cs = 12//mm
        for month in range(cs):
            money = money*rate/cs + money
        print('第%d年結束時，本利合計：%.2f' % (y+1,money))
 
def year_return(money,year,rate=0.06):
    '方案：每年利息加入本金複投'
    for y in range(year):
        money = money*rate + money
        print('第%d年結束時，本利合計：%.2f' % (y+1,money))
 
if mm == 0:
    day_return(money,year,rate)
elif mm in (1,2,3,4,6):
    month_return(money,year,mm,rate)
elif mm == 12:
    year_return(money,year,rate)
else:
    print('mm 輸入有誤！')

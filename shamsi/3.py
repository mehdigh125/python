import math
import datetime


def today(year,month,day):
    m_Year=year
    m_month=month
    m_day=day
    t1=datetime.date(int(year),int(month),int(day))
    t2=datetime.date(int(year),1,1)
    t3 =t1-t2
    t3=str(t3)
    m_upday=0
    if t3[1]==' ':
        m_upday = int(t3[0:1])
    if t3[2]==' ':
        m_upday=int(t3[0:2])
    if t3[3] == ' ':
        m_upday = int(t3[0:3])
    m_upday=int(m_upday)+1
    t4=datetime.date(int(year),1,1)
    t5=datetime.date(int(year)-1,1,1)
    t6=t4-t5
    t6=str(t6)
    t6=t6[0:3]
    YearLenght=int(t6)
    sh_upday=int(m_upday)-79
    if (sh_upday<1) and (YearLenght==365):
        sh_upday =int(m_upday) + 286
    if (sh_upday<1) and (YearLenght==366):
        sh_upday =int(m_upday) + 287

    if (sh_upday<=186):
        len_month_sh=31
    if (sh_upday>186) and (sh_upday<=336):
        len_month_sh=30
    if (sh_upday>336):
        len_month_sh=29
    if (sh_upday == 0):
        len_month_sh=29
        sh_upday=365
    if len_month_sh==31:
        X =sh_upday / 31
        sh_month = math.floor(X)
        if math.floor(X)!=X:
            sh_month =sh_month + 1
    if len_month_sh == 30:
        X = (sh_upday - 186) / 30
        sh_month = math.floor(X) + 6
        if math.floor(X)!= X:
            sh_month = sh_month + 1
    if len_month_sh == 29:
        sh_month = 12
    iLoop = 1
    sh_lupday = 0
    while (iLoop <=(sh_month - 1)):
        if  iLoop <= 6:
            len_month_sh = 31
        if iLoop > 6 and iLoop <= 11:
            len_month_sh = 30
        if iLoop == 12:
            len_month_sh = 29
        sh_lupday =sh_lupday + len_month_sh
        iLoop =iLoop +1
    if sh_lupday==0 or sh_lupday=='':
         sh_lupday=0
    sh_day=sh_upday-sh_lupday
    sh_year=int(m_Year)-621
    if int(m_upday) <= 79:
        sh_year =sh_year - 1

    if int(sh_month) < 10:
        sh_month = '0' +str(sh_month)
    print(str(sh_year) +'/'+ str(sh_month) +'/'+ str(sh_day))
    if YearLenght==366:
        print('سال کبیسه است')
    else:
        print('سال کبیسه نیست')

    #print(f"m_Year={m_Year},m_month={m_month},m_day={m_day},t3={t3},m_upday={m_upday},t6={t6},yearlenght={YearLenght},sh_upday={sh_upday},len_month_sh={len_month_sh},sh_month={sh_month},iloop={iLoop},sh_lupday={sh_lupday},sh-day={sh_day},sh_year={sh_year}")

    return

date1 = input('please date:')

try:
    if len(date1)==8 and date1.isdecimal():
        year = date1[0:4]
        month = date1[4:6]
        day = date1[6:8]
    if date1.find('/')!=-1 :
        year,month,day=date1.split('/')
    if date1.find(' ')!=-1:
        year,month,day=date1.split(' ')
    if date1.find('-')!=-1:
        year,month,day=date1.split('-')
    if len(month)==1:
        month='0'+str(month)
    if len(day)==1:
        day='0'+str(day)

    today(year,month,day)

except :
     print('تاریخ با فرمت درست وارد نمایید به عنوان مثال 2023/05/06')





def t_DATE_LIT(t):  #update
    r'\'\d{4}\-(0?[1-9]|10|11|12)\-(30|31|((0|1|2)?[0-9]))\'' # Year-Month-Day
    date_tokens = t.value.split("-")
    print(date_tokens)
    date_tokens[0] = date_tokens[0][1:]
    date_tokens[2] = date_tokens[2][:-1]
    t.value = date(int(date_tokens[0]), int(date_tokens[1]), int(date_tokens[2]))
    print("date_lit value:", t.value)
    return t


def t_DATE_UNIT(t):
    r'(second|minute|day|week|month|quarter|year)'
    print('dateunit')

def p_date_function(p):
    '''date_function : ADDDATE OPENPAR date_exp COMMA date_exp CLOSEPAR
             | CURDATE OPENPAR CLOSEPAR
             | CURRENT_DATE OPENPAR CLOSEPAR
             | CURRENT_DATE
             | DATEDIFF OPENPAR date_exp COMMA date_exp CLOSEPAR
             | DAY OPENPAR date_exp CLOSEPAR
             | DAYNAME OPENPAR date_exp CLOSEPAR
             | DAYOFMONTH OPENPAR date_exp CLOSEPAR
             | DAYOFWEEK OPENPAR date_exp CLOSEPAR
             | DAYOFYEAR OPENPAR date_exp CLOSEPAR
             | LAST_DAY OPENPAR date_exp CLOSEPAR
             | MAKEDATE OPENPAR num_exp COMMA num_exp CLOSEPAR
             | MONTH OPENPAR date_exp CLOSEPAR
             | MONTHNAME OPENPAR date_exp CLOSEPAR
             | SUBDATE OPENPAR date_exp COMMA INTERVAL num_exp DATE_UNIT CLOSEPAR
             | YEAR OPENPAR date_exp CLOSEPAR'''

#print p[1], p[2], p[3], p[4]
    if p[1] == 'current_date' or p[1] == 'curdate': #CURRENT_DATE(), CURRENT_DATE, CURDATE()
        print (time.strftime("%Y-%m-%d"))
    elif p[1] == 'datediff':
        print(abs(p[3] - p[5]).days)
    elif p[1] == 'day':
        print('pasok sa day')
    elif p[1] == 'dayname':
        print('pasok sa dayname')
        #d1 = datetime.strptime(p[3], "%Y-%m-%d")
        #print(d1.day)
    elif p[1] == 'last_day':
        print('pasok sa lastday')
    elif p[1] == 'makedate':
        dt = date(year=p[3],month=1,day=1)
        dayCount = p[5] - 1
        dtdelta = timedelta(days=dayCount)
        finalDate = dt + dtdelta
        print(finalDate)
    elif p[1] == 'month':   #fix inclusin in monthunit
        print('pasok sa month')
        print(p[3].month)
    elif p[1] == 'monthname':
        print('pasok sa monthname')
        print(p[3].strftime("%B"))
    elif 

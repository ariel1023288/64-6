def f(money,interest,month)
    result=0
    for i in range(month)#跑每個月的錢
    #i是目前跑到幾個月
    #代表還有month-i個月要跑
        rseult += money*((interest+100)/100)**(month-i)
    #interest代表的是%數，所以要+100然後除以100
    return result
    #當存錢時還剩下month個月，代表要跑month個月的月利
print(f(100,100,5))
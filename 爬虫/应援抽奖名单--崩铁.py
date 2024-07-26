import requests
import re
import keyboard
import time

a=0
while a==0:
    print("正在请求...")
    #开始计时请求所用的时间
    T1 = time.perf_counter()
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }
    response = requests.get("https://api.bilibili.com/x/lottery/win/list?sid=newLottery_3485dc6a-2d22-11ef-ab09-e8b47005dab5", headers = headers)
    html = response.text
    #判断是否请求成功
    if response.ok:
        T2 = time.perf_counter()
        T = T2 - T1
        #保留2位小数
        print("请求成功(用时",'%.2f'%T,"s)",sep="")
        print("")
        #数据处理
        obj = re.compile(r'"name".*?"ctime".*?:(?P<time>.*?),.*?"name".*?"(?P<name>.*?)"',re.S)
        result = obj.finditer(html)
        for i in result:
            #计算奖品已发放时间
            time1 = int(i.group("time"))
            ctime = time.time()
            time2 = int((ctime-time1)/60)
            if time2>60:
                dw="h"
                time2 = time2/60
                time2 = '%.1f'% time2
            else:
                dw = "min"
            print(i.group("name"),"(",time2,dw,"前)",sep="")
    else:
        print("请求失败")
    print("")
    print("按A键再次请求")
    keyboard.wait("a")
import requests
import re
import keyboard
import time

a=0
while a==0:
    print("原神-1,崩铁-2,崩3-3,鸣潮-4,绝区零-5")
    #判断选择
    while True:
        if keyboard.is_pressed('1'):
            wz = "https://api.bilibili.com/x/lottery/x/win/list?csrf=cd3696a21a7387a347bd89707d53d166&sid=4ERA1wloghvy3q00"
            break
        elif keyboard.is_pressed('2'):
            wz = "https://api.bilibili.com/x/lottery/win/list?sid=newLottery_3485dc6a-2d22-11ef-ab09-e8b47005dab5"
            break
        elif keyboard.is_pressed('3'):
            wz = "https://api.bilibili.com/x/lottery/x/win/list?csrf=cd3696a21a7387a347bd89707d53d166&sid=4ERA1wloghvrwd00"
            break
        elif keyboard.is_pressed('4'):
            wz = "https://api.bilibili.com/x/lottery/win/list?sid=newLottery_d0175833-338e-11ef-ab09-e8b47005dab5"
            break  
        elif keyboard.is_pressed('5'):
            wz = "https://api.bilibili.com/x/lottery/win/list?sid=newLottery_9b6fe571-379e-11ef-ab09-e8b47005dab5"
            break                  
    print("正在请求...")
    #开始计时请求所用的时间
    T1 = time.perf_counter()
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }
    response = requests.get(wz, headers = headers)
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
            #单位转换
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
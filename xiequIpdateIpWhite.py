"""
new Env('携趣更新IP');
9 9 9 9 * xiequIpdateIpWhite.py
by:fjcqv
"""
import requests
import re
import os
def getIP():
    try:
        r=requests.get("https://api.ipify.org/")
        if r.status_code==200:
            return r.text
        return False
    except:
        return False
def is_valid_ipv4(ip_str):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    match = re.fullmatch(pattern, ip_str)
    return match is not None

def xiequ(xiequAPI,ip_str):
    try:
        r1=requests.get("{}&act=del&ip=all".format(xiequAPI))
        if r1.status_code==200 :
            print("删除所有记录：{}".format(r1.text))
        r2 = requests.get(
            "{}&act=add&ip={}".format(xiequAPI,ip_str))
        if r1.status_code == 200:
            print("添加一条记录：{}".format(r2.text))


    except:
        pass
if __name__ == '__main__':
    xiequAPI=os.environ['XIEQU_IPWHITE_API']
    print(xiequAPI.startswith("http://op.xiequ.cn/IpWhiteList.aspx"))
    if xiequAPI.startswith("http://op.xiequ.cn/IpWhiteList.aspx"):
        ip = getIP()
        if ip and is_valid_ipv4(ip):
            print("当前IP：{}".format(ip))
            xiequ(xiequAPI,ip)



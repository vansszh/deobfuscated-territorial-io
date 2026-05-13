import requests,re,os
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse

def download_territorial():
    u="https://territorial.io"
    print(f"Fetching {u}...")
    hdrs={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    try:
        r=requests.get(u,headers=hdrs); r.raise_for_status()
    except Exception as e: print(f"Error fetching the main page: {e}"); return
    sp=BeautifulSoup(r.text,'html.parser')
    for sc in sp.find_all("script",src=True):
        s=sc['src']; su=urljoin(u,s)
        print(f"Inlining script: {su}")
        try:
            sr=requests.get(su,headers=hdrs); sr.raise_for_status()
            ns=sp.new_tag("script"); ns.string=sr.text; sc.replace_with(ns)
        except Exception as e: print(f"Failed to inline script {s}: {e}")
    for lk in sp.find_all("link",rel="stylesheet"):
        h=lk.get('href')
        if not h: continue
        cu=urljoin(u,h); print(f"Inlining style: {cu}")
        try:
            cr=requests.get(cu,headers=hdrs); cr.raise_for_status()
            nt=sp.new_tag("style"); nt.string=cr.text; lk.replace_with(nt)
        except Exception as e: print(f"Failed to inline style {h}: {e}")
    for img in sp.find_all("img",src=True): pass
    out="territorial_all_in_one.html"
    open(out,"w",encoding="utf-8").write(str(sp)); print(f"Successfully saved to {out}")

if __name__=="__main__": download_territorial()

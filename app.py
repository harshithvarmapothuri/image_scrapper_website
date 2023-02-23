import os
import logging
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
from flask import Flask,render_template,request
import requests


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search",methods=["POST"])
def start():
    if(request.method=="POST"):
        query=request.form["search"]
        query=query.replace(" ","+")
        link="https://www.google.com/search?q="+query+"&tbm=isch&ved=2ahUKEwjN9LTK2ar9AhX3HbcAHQ3RA5AQ2-cCegQIABAA&oq=sudhanshu+kumar+&gs_lcp=CgNpbWcQARgAMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIECAAQHjIGCAAQBRAeMgYIABAFEB46BAgjECc6BggAEAcQHlDhAljhAmCSEGgAcAB4AIABbYgB0wGSAQMwLjKYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=PN32Y83mIfe73LUPjaKPgAk&bih=746&biw=1536&rlz=1C1RXQR_enIN1032IN1032"
        data=requests.get(link)
        final=bs(data.content,"html.parser")
        imgs=final.find_all("img")
        del imgs[0]
        l=[]
        for i in imgs:
            l.append(i["src"])
        return render_template("result.html",image_urls=l)

if __name__=="__main__":
    app.run(host="0.0.0.0",port="8000")
from fastapi import FastAPI
import requests
import urllib
from _datetime import datetime
from datetime import timedelta
import pandas as pd
import os, sys

app = FastAPI()

apiID = "26a50a98f1b7f4aa4"
apiKey = "AIzaSyCTFjqO5tMO1R6uNck2oW4Zy77NL_9P6_g"
googleAPIUrl = "https://customsearch.googleapis.com/customsearch/v1"

setPage = 10
#원하시는 페이지 정수(1 ~ 10)를 입력해주세요.

def getItems(query, page):
    global apiID, apiKey, googleAPIUrl
    googleAPIResponse = requests.get("%s?q=%s&sort=date&start=%d&cx=%s&key=%s" % (googleAPIUrl, query, page, apiID, apiKey))
    
    return googleAPIResponse.json()["items"]


def writeTSV(items, file):
    item = None

    for item in items:

        file.write("%s\t%s\t%s\n" % (item["title"], item["link"], item["snippet"]))
        # 순서는 제목, url, 글 내용 입니다.   


def reWriteTSV():

    df = pd.read_csv("/googleSearchResult.tsv", sep="\t", names=["title", "url", "content"])

    content = df["content"].to_numpy()
    dateAr = []
    now = datetime.today()
    postDate, date, c = None, None, None

    for c in content:
        date = c.split("...")[0]
        postDate = date.split(" ")

        if postDate[2].__contains__("ago"):
            postDate = now - timedelta(days=int(postDate[0]))
            postDate = int(datetime.strftime(postDate, '%Y%m%d'))
        else:
            postDate = datetime.strptime(date, '%b %d, %Y ')
            postDate = int(datetime.strftime(postDate, '%Y%m%d'))

        dateAr.append(postDate)

    df["date"] = dateAr
    df = df.sort_values(by="date")
    df = df[["date", "title", "url", "content"]]
    df.to_csv("/gsrSortByDate.tsv", encoding="utf-8", index=False, sep="\t")


@app.get("/search")
def searchGoogle(keyword):
    try:
        global setPage
        query = requests.utils.quote(keyword)
        setPage = setPage * 10 - 8
        f = open("/googleSearchResult.tsv", "a", encoding="utf-8")

        page, items = None, None
        # 반복문 안에서의 변수 선언을 싫어합니다.

        for page in range(1, setPage, 10):
            try:
                items = getItems(query, page)
                writeTSV(items, f)
            except KeyError:
                # 글 내용 키 값인 "snippet" 이 없는 경우가 존재합니다.
                continue
        f.close()

        reWriteTSV()

        return {'result': "성공"}

    except Exception as e:
        print(e)
        return {'result': "실패"}


@app.post("/search")
def searchGoogle(keyword):
    try:
        global setPage
        query = requests.utils.quote(keyword)
        setPage = setPage * 10 - 8
        f = open("/googleSearchResult.tsv", "a", encoding="utf-8")

        page, items = None, None
        # 반복문 안에서의 변수 선언을 싫어합니다.

        for page in range(1, setPage, 10):
            try:
                items = getItems(query, page)
                writeTSV(items, f)
            except KeyError:
                # 글 내용 키 값인 "snippet" 이 없는 경우가 존재합니다.
                continue
        f.close()

        reWriteTSV()

        return {'result': "성공"}

    except Exception as e:
        print(e)
        return {'result': "실패"}
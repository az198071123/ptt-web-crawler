# -*- coding: utf-8 -*-
from datetime import datetime
import json
from json import JSONDecodeError
import os
from subprocess import call
import sys
import traceback
from typing import List

import requests
from requests.exceptions import ReadTimeout

from PttWebCrawler.crawler import PttWebCrawler
from model.mongo import Articles
from functools import partial

watch = ["微波爐", "風扇", "電扇", "內湖", "松山", "Mac", "iPhone"]
ignore = [
    "[公告]",
]

WATCH_CONFIG = {
    "give": ["微波爐", "風扇", "電扇", "內湖", "松山", "Mac", "iPhone"],
    "BuyTogether": ["youtube"],
}

IFTTT_TOKEN = os.environ.get("IFTTT_TOKEN", "")
IFTTT_EVENT = "ptt_give_observer"
IFTTT_WEBHOOKS_URL = (
    f"https://maker.ifttt.com/trigger/{IFTTT_EVENT}/with/key/{IFTTT_TOKEN}"
)

# def isset(v):
#     try:
#         type(eval(v))
#     except:
#         return False
#     else:
#         return True


def send_ifttt_webhook(value1, value2):
    # data = {'value1': f'{value1}', 'value2': f'{value2}'}
    data = {"value1": f"{value1}\n{value2}"}
    res = requests.post(IFTTT_WEBHOOKS_URL, data=data)
    print_log(dict(url=IFTTT_WEBHOOKS_URL, res=res), "IFTTT respone")


def print_log(log, *tag):
    lineno = sys._getframe().f_back.f_lineno
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tags = f"[{now}][:{lineno}]"
    for t in tag:
        tags += f"[{t}]"
    print(f"{tags}: {log}")


def print_exception(e):
    traceback.print_exc(file=sys.stdout)


def run_ptt_give_crawler():
    board = "give"
    # last_page = PttWebCrawler.getLastPage(board)
    # start_no, end_no = last_page - 1, last_page
    start_no, end_no = 0, 0
    loadfile_before = f"{board}-{start_no}-{end_no}-save.json"

    # set default
    articles_before = []
    articles_after = []

    # read file
    if os.path.isfile(loadfile_before):
        with open(loadfile_before, "r") as reader:
            remove = False
            try:
                jf_defore = json.loads(reader.read())
                articles_before = jf_defore["articles"]
                print_log(f"articles_before len({len(articles_before)})")
            except JSONDecodeError as e:
                print_exception(e)
                remove = True
        if remove:
            os.remove(loadfile_before)

    loadfile_after = PttWebCrawler(as_lib=True).parse_articles(start_no, end_no, board)

    if os.path.isfile(loadfile_after):
        jf_after = None
        with open(loadfile_after, "r") as reader:
            try:
                jf_after = json.loads(reader.read())
                articles_after = jf_after["articles"]
                print_log(f"articles_after len({len(articles_after)})")
            except JSONDecodeError as e:
                print_exception(e)
                print_log(jf_after, "jf_after")
                raise
        os.replace(loadfile_after, loadfile_before)

    # diff_v1(articles_before, articles_after)
    diff_v2(articles_after)
    return True


def run_ptt_give_crawler_v2():
    board = "give"
    start_no, end_no = 0, 0
    PttWebCrawler(as_lib=True).crawl_articles(start_no, end_no, board, on_crawled)


def run_ptt_give_crawler_v3():
    for board, watch in WATCH_CONFIG.items():
        start_no, end_no = 0, 0
        PttWebCrawler(as_lib=True).crawl_articles(
            start_no, end_no, board, partial(on_crawled_v2, watch=watch)
        )


def diff_v1(articles_before: List[dict], articles_after: List[dict]):
    # diff 策略: A-B 差集
    # diff(articles_before, articles_after)
    before_map = {item["article_id"]: item for item in articles_before}
    after_map = {item["article_id"]: item for item in articles_after}
    diff_ids = after_map.keys() - before_map.keys()

    # check result
    if diff_ids:
        for article_id in diff_ids:
            content = after_map[article_id]
            notify(content)
    else:
        print_log("no diff")


def diff_v2(articles_after: List[dict]):
    for item in articles_after:
        find = Articles.objects.filter(pk=item["article_id"])
        if not find:
            notify(item)
        Articles(**item).save()


def on_crawled(json_string: str):
    article = json.loads(json_string)
    if "article_id" not in article:
        print_log(article, "on_crawled")
        return
    find = Articles.objects.filter(pk=article["article_id"]).first()
    if not find:
        notify(article, watch)
        Articles(**article).save()
    else:
        find.update(**article, updated_at=datetime.now())


def on_crawled_v2(json_string: str, watch: list):
    article = json.loads(json_string)
    if "article_id" not in article:
        print_log(article, "on_crawled_v2")
        return
    find = Articles.objects.filter(pk=article["article_id"]).first()
    if not find:
        notify(article, watch)
        Articles(**article).save()
    else:
        find.update(**article, updated_at=datetime.now())


def notify(item: dict, watch: list):
    article_id = item["article_id"]
    title = item["article_title"].replace('"', '\\"')
    content = item["content"].replace('"', '\\"')
    date = item["date"]

    # chekc ignore
    for i in ignore:
        if i.lower() in title.lower():
            print_log(f"title={title}", "ignore")
            return

    # notify mac os
    print_log(f"article_id={article_id}, title={title}", "notification")
    call(
        [
            "osascript",
            "-e",
            f'display notification "{content}" with title "{title}" subtitle "{date}" sound name "Pop"',
        ]
    )

    # notify phone
    for w in watch:
        if w.lower() in title.lower() or w.lower() in content.lower():
            # call(["osascript", "-e", f'display alert \"{title}\" message \"{cont}\"'])
            send_ifttt_webhook(title, content)
            break


if __name__ == "__main__":
    try:
        print_log(f"=========== start({datetime.now().timestamp()}) =========== ")
        # run_ptt_give_crawler()
        # run_ptt_give_crawler_v2()
        run_ptt_give_crawler_v3()
        print_log(f"=========== end({datetime.now().timestamp()}) =========== ")
    except ReadTimeout as e:
        print_exception(e)
    except Exception as e:
        title = "give 爬蟲錯誤"
        print_log(title, "notification")
        # cmd = 'display notification \"test\" with title \"title\" subtitle \"subtitle\" sound name \"Glass\"'
        cmd = (
            f'display notification "{type(e)}" with title "{title}" sound name "Glass"'
        )
        call(["osascript", "-e", cmd])
        print_exception(e)

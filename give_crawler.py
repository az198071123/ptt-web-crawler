# -*- coding: utf-8 -*-
import json
import os
import sys
from datetime import datetime
from json import JSONDecodeError
from subprocess import call

import requests
from requests.exceptions import ReadTimeout

from PttWebCrawler.crawler import PttWebCrawler
import traceback

watch = ['微波爐', '風扇', '內湖', '松山', ]
ignore = ['[公告]', ]

IFTTT_TOKEN = os.environ.get('IFTTT_TOKEN', '')
IFTTT_EVENT = 'ptt_give_observer'
IFTTT_WEBHOOKS_URL = f'https://maker.ifttt.com/trigger/{IFTTT_EVENT}/with/key/{IFTTT_TOKEN}'

# def isset(v):
#     try:
#         type(eval(v))
#     except:
#         return False
#     else:
#         return True


def send_ifttt_webhook(value1, value2):
    # data = {'value1': f'{value1}', 'value2': f'{value2}'}
    data = {'value1': f'{value1}\n{value2}'}
    res = requests.post(IFTTT_WEBHOOKS_URL, data=data)
    print_log(dict(url=IFTTT_WEBHOOKS_URL, res=res), 'IFTTT respone')


def print_log(log, *tag):
    lineno = sys._getframe().f_back.f_lineno
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tags = f'[{now}][:{lineno}]'
    for t in tag:
        tags += f'[{t}]'
    print(f'{tags}: {log}')


def print_exception(e):
    traceback.print_exc(file=sys.stdout)


def run_ptt_give_crawler():
    board = 'give'
    # last_page = PttWebCrawler.getLastPage(board)
    # start_no, end_no = last_page - 1, last_page
    start_no, end_no = 0, 0
    loadfile_before = f'{board}-{start_no}-{end_no}-save.json'

    # set default
    articles_before = []
    articles_after = []

    # read file
    if os.path.isfile(loadfile_before):
        with open(loadfile_before, 'r') as reader:
            remove = False
            try:
                jf_defore = json.loads(reader.read())
                articles_before = jf_defore['articles']
                print_log(f"articles_before len({len(articles_before)})")
            except JSONDecodeError as e:
                print_exception(e)
                remove = True
        if remove:
            os.remove(loadfile_before)

    loadfile_after = PttWebCrawler(as_lib=True).parse_articles(start_no, end_no, board)

    if os.path.isfile(loadfile_after):
        jf_after = None
        with open(loadfile_after, 'r') as reader:
            try:
                jf_after = json.loads(reader.read())
                articles_after = jf_after['articles']
                print_log(f"articles_after len({len(articles_after)})")
            except JSONDecodeError as e:
                print_exception(e)
                print_log(jf_after, 'jf_after')
                raise
        os.replace(loadfile_after, loadfile_before)

    # diff 策略: A-B 差集
    before_map = {item["article_id"]: item for item in articles_before}
    after_map = {item["article_id"]: item for item in articles_after}
    diff_ids = after_map.keys() - before_map.keys()

    # check result
    if diff_ids:
        for article_id in diff_ids:
            content = after_map[article_id]
            title = content['article_title']
            cont = content['content']
            url = content['url']

            #
            is_continue = False
            for i in ignore:
                if i in title:
                    print_log(f'ignore({title})')
                    is_continue = True
            if is_continue:
                continue

            #
            print_log(f'article_id={article_id}, title={title}', 'notification')
            call(["osascript", "-e",
                  f'display notification \"{cont}\" with title \"{title}\" subtitle \"{url}\" sound name \"Pop\"'])

            #
            for w in watch:
                if w in title or w in cont:
                    call(["osascript", "-e", f'display alert \"{title}\" message \"{cont}\"'])
                    send_ifttt_webhook(title, cont)
                    break

    else:
        print_log('no diff')
    return True


if __name__ == '__main__':
    try:
        ts = datetime.now().timestamp()
        print_log(f'=========== start({ts}) =========== ')
        run_ptt_give_crawler()
        print_log(f'=========== end({ts}) =========== ')
    except ReadTimeout as e:
        print_exception(e)
    except Exception as e:
        cmd = f'display notification \" {e} \" with title \"give 爬蟲錯誤 {type(e)}\" sound name \"Glass\"'
        call(["osascript", "-e", cmd])
        print_exception(e)

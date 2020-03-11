# -*- coding: utf-8 -*-
import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.test_json1 = {
            "articles": [
                {
                    "article_id": "M.1580712320.A.F59",
                    "article_title": "[公告] 二月置底檢舉建議區 刪文多因標題有誤",
                    "author": "gogin (愛喝可樂的勾勾)",
                    "board": "give",
                    "content": "武漢肺炎來襲 希望大家出門可以多洗手 都躲過這次的危機 本月月重點還是在標題部分 希望大家可以依照板規使用標題發文 請依照 [贈送] 地點 物品 現在未依照此順序者 文章砍除 可以想索取者可方便閱讀 如果有任何違反板規的文章 請到這裡檢舉 並請附上下列資訊： （一）文章代碼(AID)。 （二）違規人之ID。 （三）違規行為與板規。 如 12345678 /gogin/板規13 贈送菸酒 /可用空格代替 而發文標題請依照以下格式辦理 即日起執行 贈與發文標題請依照以下格式辦理 [贈送] 地點 物品 EX: [贈送] 新莊 不用的複合印表機 如果為郵寄或店對店等 地點可以改為全國 或直接地點改郵寄或店對店 送出後得在標題或推文加註，送出後標題不得把贈送物項目刪除 [贈送] 蘆洲 Android平板電腦(送出) [送出] 蘆洲 Android平板電腦 [贈送] (送出)Android平板電腦 Ｘ [贈送] 送出 這樣不能 以上未依格式發文直接刪文。",
                    "date": "Mon Feb  3 14:45:17 2020",
                    "ip": "114.24.219.16",
                    "message_count": {
                        "all": 3,
                        "boo": 0,
                        "count": 0,
                        "neutral": 3,
                        "push": 0
                    },
                    "messages": [{
                        "push_content": "#1UGhUuOs 　kaikai160203　贈送隱形眼鏡盒",
                        "push_ipdatetime": "02/12 19:59",
                        "push_tag": "→",
                        "push_userid": "kanakin"
                    }, {
                        "push_content": "上面已處理",
                        "push_ipdatetime": "02/17 10:01",
                        "push_tag": "→",
                        "push_userid": "gogin"
                    }, {
                        "push_content": "#1UIgDurH  清空",
                        "push_ipdatetime": "02/19 00:16",
                        "push_tag": "→",
                        "push_userid": "tonybbbb"
                    }],
                    "url": "https://www.ptt.cc/bbs/give/M.1580712320.A.F59.html"
                }
            ]
        }

        self.test_json2 = {
            "articles": [
                {
                    "article_id": "M.1580712320.A.F59",
                    "article_title": "[公告] 二月置底檢舉建議區 刪文多因標題有誤",
                    "author": "gogin (愛喝可樂的勾勾)",
                    "board": "give",
                    "content": "武漢肺炎來襲 希望大家出門可以多洗手 都躲過這次的危機 本月月重點還是在標題部分 希望大家可以依照板規使用標題發文 請依照 [贈送] 地點 物品 現在未依照此順序者 文章砍除 可以想索取者可方便閱讀 如果有任何違反板規的文章 請到這裡檢舉 並請附上下列資訊： （一）文章代碼(AID)。 （二）違規人之ID。 （三）違規行為與板規。 如 12345678 /gogin/板規13 贈送菸酒 /可用空格代替 而發文標題請依照以下格式辦理 即日起執行 贈與發文標題請依照以下格式辦理 [贈送] 地點 物品 EX: [贈送] 新莊 不用的複合印表機 如果為郵寄或店對店等 地點可以改為全國 或直接地點改郵寄或店對店 送出後得在標題或推文加註，送出後標題不得把贈送物項目刪除 [贈送] 蘆洲 Android平板電腦(送出) [送出] 蘆洲 Android平板電腦 [贈送] (送出)Android平板電腦 Ｘ [贈送] 送出 這樣不能 以上未依格式發文直接刪文。",
                    "date": "Mon Feb  3 14:45:17 2020",
                    "ip": "114.24.219.16",
                    "message_count": {
                        "all": 3,
                        "boo": 0,
                        "count": 0,
                        "neutral": 3,
                        "push": 0
                    },
                    "messages": [{
                        "push_content": "#1UGhUuOs 　kaikai160203　贈送隱形眼鏡盒",
                        "push_ipdatetime": "02/12 19:59",
                        "push_tag": "→",
                        "push_userid": "kanakin"
                    }, {
                        "push_content": "上面已處理",
                        "push_ipdatetime": "02/17 10:01",
                        "push_tag": "→",
                        "push_userid": "gogin"
                    }, {
                        "push_content": "#1UIgDurH  清空",
                        "push_ipdatetime": "02/19 00:16",
                        "push_tag": "→",
                        "push_userid": "tonybbbb"
                    }],
                    "url": "https://www.ptt.cc/bbs/give/M.1580712320.A.F59.html"
                },
                {
                    "article_id": "M.1580893099.A.DAF",
                    "article_title": "[公告] 禁止贈送醫療相關物品提醒",
                    "author": "gogin (愛喝可樂的勾勾)",
                    "board": "give",
                    "content": "大家好 我是很懶的板主gogin 最近全球新型2019新冠狀病毒(武漢肺炎)全球肆虐 希望大家勤洗手來對抗 在此板主群跟大家做個小提醒 最近到處缺貨的醫療用口罩 是屬於醫療用品 是在板規14 醫療用品之範圍內 而酒精與酒精棉片亦為醫療用品 也在不得贈送規範內 請大家注意此板規 違規者 禁言一年該文章退文 順道一提 該板規有修正新增部分 如贈送物品名稱有在以上範圍內但非醫藥用品請先標明， 不然視同違反此板規。 請大家遵守板規 ",
                    "date": "Wed Feb  5 16:58:17 2020",
                    "ip": "114.24.219.16",
                    "message_count": {
                        "all": 0,
                        "boo": 0,
                        "count": 0,
                        "neutral": 0,
                        "push": 0
                    },
                    "messages": [],
                    "url": "https://www.ptt.cc/bbs/give/M.1580893099.A.DAF.html"
                }
            ]
        }

    def test_diff_none(self):
        t1 = {item["article_id"]: item for item in self.test_json1["articles"]}
        t2 = {item["article_id"]: item for item in self.test_json2["articles"]}
        diff = {article_id: content for article_id, content in t1.items() if article_id not in t2}
        self.assertFalse(diff)

    def test_diff_not_none(self):
        t1 = {item["article_id"]: item for item in self.test_json1["articles"]}
        t2 = {item["article_id"]: item for item in self.test_json2["articles"]}
        diff = {article_id: content for article_id, content in t2.items() if article_id not in t1}
        self.assertTrue(diff)

    def test_diff_same(self):
        t1 = {item["article_id"]: item for item in self.test_json1["articles"]}
        t2 = {item["article_id"]: item for item in self.test_json1["articles"]}
        diff = {article_id: content for article_id, content in t2.items() if article_id not in t1}
        self.assertFalse(diff)


if __name__ == '__main__':
    unittest.main()

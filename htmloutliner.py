#! c:/Python27/python.exe
# -*- coding: utf-8 -*-

import urllib2

def output_outline(url):
    raw_html = ""
    parsed_html = ""

    tmp_html = urllib2.urlopen(url)
    raw_html = tmp_html.read()
    parsed_html = raw_html

    return parsed_html


if __name__ == "__main__":

    print u"HTML解析開始"

    outline = output_outline("http://www.google.co.jp")

    print u"----HTML START----"
    print outline
    print u"----HTML END----"

    print u"HTML解析終了"


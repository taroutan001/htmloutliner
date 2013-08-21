#! c:/Python27/python.exe
# -*- coding: utf-8 -*-

import urllib2
from HTMLParser import HTMLParser


class CommonHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.tab  = ""
        self.val  = None
        self.data = []

    def handle_starttag(self,tagname,attributes):

        print self.tab + "<" + tagname + ">"

        self.tab += "\t"
        for attr in attributes:
            tmptmp = attr
            print self.tab + "@" + attr[0] + "=" + attr[1]

    def handle_endtag(self,tagname):
        self.tab = self.tab[:-1]
        print self.tab + "</" +tagname + ">"

    def handle_data(self,data):
        print ""


def output_outline(url):
    raw_html = ""
    parsed_html = ""

    tmp_html = urllib2.urlopen(url)
    raw_html = tmp_html.read()
    parsed_html = raw_html

    return parsed_html


if __name__ == "__main__":

    print u"HTML解析開始"
    url = "http://www.google.co.jp"
    opened_url = urllib2.urlopen(url)
    raw_html = opened_url.read()

    parser = CommonHTMLParser()
    parser.feed(raw_html)

    parser.close()

    #outline = output_outline("http://www.google.co.jp")


    #print u"----HTML START----"
    #print outline
    #print u"----HTML END----"

    print u"HTML解析終了"


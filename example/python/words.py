"""
    URL로부터 파일을 가져와 단어를 print 함.
Usage:

    python words.py <URL>
"""

from urllib.request import urlopen

import sys


def fetch_words(url):
    """
    url주소에서 파일을 가져와 단어 리스트를 반환합니다.
    :param url: 불러올 url
    :return:
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """
    items를 print
    :param items: 
    :return: 
    """
    for item in items:
        print(item)


def main(url):
    '''
    url을 받아 단어를 print 함
    :param url: url
    :return:
    '''
    words = fetch_words(url)
    print_items(words)
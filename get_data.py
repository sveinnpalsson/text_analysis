from multiprocessing import Pool
from multiprocessing import cpu_count
import urllib.request
import os
from os.path import join
from lxml.html import fromstring

urls = open("urls_visir_dec18.txt","r").read().split("\n")

def parse(i):
    url = urls[i]
    page = url.split('/')[-1]
    body = fromstring(urllib.request.urlopen(url).read())
    text = body.xpath("//*[contains(@class, 'article-single__content')]")[0].text_content().strip()
    header = body.xpath("//title")[0].text_content().strip()
    filename = join("article_texts",page)
    with open(filename+'.txt','w') as f:
        f.write(url+'\n')
        f.write(header)
        f.write('\n')
        f.write(text)
    print('Saved file %s' % filename)
    return i


def main():
    pool = Pool(cpu_count()-1)
    os.makedirs("article_texts",exist_ok=True)
    for i in pool.imap_unordered(parse,range(len(urls))):
        continue

if __name__ == "__main__":
    main()


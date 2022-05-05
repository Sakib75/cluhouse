import os


files = os.listdir('./input/')

for file in files:
    os.system(f"scrapy crawl clubhouse_spider -a input_file=input/{file} -o output/output_{file}")
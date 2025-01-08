# scrapy-example
## example of use of scrapy

## step 1 create project
```
scrapy startproject spider_tutorial
```

## step 2 create spider
```
cd spider_tutorial
scrapy genspider www.worldometers.info/world-population/population-by-country
```

## test spider
```
scrapy shell
```
## then execute this code
```
r = scrapy.Request(url='')
fetch(r)
response.body
response.xpath('//h1/text()').get()
response.xpath('//td/a/text()').get()
```
## run spider
```
scrapy crawl worldometers
```
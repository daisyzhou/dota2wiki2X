# scratch work to test stuff
from lxml import html

print 'NOTE: for some reason this only works if the html has been formatted (tabulated, etc)'

with open('earthshaker.html') as f:
    single_page = html.fromstring(f.read(), parser=html.html_parser)
    f.close()

print(single_page)
print(single_page.xpath('///text()'))
body = single_page.getchildren()[1]

print 'rows in outermost table (no dota info)'
table_body = body.getchildren()[1].getchildren()
print(table_body)
rows = table_body[0].getchildren()
print(rows)
# for r in rows:
#     if r[0].text != None or r[1].text != None:
#         print(r[0].text, r[1].text)


print 'STEP BY STEP'
print(len(single_page.xpath('//body')))
body = single_page.xpath('//body')[0]
print(body)
print(body.getchildren())
global_wrapper = body.xpath('//div[@id="global-wrapper"]')[0]
print(global_wrapper)
page_wrapper = global_wrapper.xpath('//div[@id="pageWrapper"]')[0]
print(page_wrapper)
content = page_wrapper.xpath('//div[@id="content"][@class="mw-body"]')[0]
print(content)
body_wrapper = content.xpath('//div[@id="bodyWrapper"]')[0]
print(body_wrapper)
body_content = body_wrapper.xpath('//div[@id="bodyContent"]')[0].xpath('//div[@id="mw-content-text"][@class="mw-content-ltr"]')[0]
print(body_content)
abilities = body_content.xpath('//h2/span[@id="Abilities"]')[0]
print(abilities)

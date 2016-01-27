# scratch work to test stuff
from lxml import html

print 'NOTE: for some reason this only works if the html has been formatted (tabulated, etc)'

with open('earthshaker.html') as f:
    single_page = html.fromstring(f.read(), parser=html.html_parser)
    f.close()

body = single_page.xpath('//body')[0]
content = \
    body.xpath('//div[@id="global-wrapper"]')[0]\
            .xpath('//div[@id="pageWrapper"]')[0]\
            .xpath('//div[@id="content"][@class="mw-body"]')[0]\
            .xpath('//div[@id="bodyWrapper"]')[0]\
            .xpath('//div[@id="bodyContent"]')[0]\
            .xpath('//div[@id="mw-content-text"][@class="mw-content-ltr"]')[0]

infobox_rows = content.xpath('//table[@class="infobox"]/tr')

name = infobox_rows[0].xpath('td/table/tr/th')[0].text.lstrip()
print("Name: %s" % name)

# Strength/Agility/Intelligence base + growth
print("attr base + growth")
attributes = infobox_rows[2]
attributes_rows = attributes.xpath('td/table/tr/th')
for row in attributes_rows:
    attr_name = row.xpath('a')[0].attrib['title']
    base = row.xpath('b')[0].text
    growth = row.xpath('b')[0].tail.strip(' +')
    print('Attribute: %s, %s+%s' % (attr_name, base, growth))

# various attrs at different levels (base, 1, 16, 25)
stats = infobox_rows[3]

# attrs that don't change per level like movement speed, turn rate, etc
other_attrs = infobox_rows[4]

abilities = content.xpath('//h2/span[@id="Abilities"]')[0]
print(abilities)

# scratch work to test stuff
from lxml import html

print 'NOTE: for some reason this only works if the html has been formatted (tabulated, etc)'

def parse_attributes(attributes_rows):
    for row in attributes_rows:
        attr_name = row.xpath('a')[0].attrib['title']
        base = row.xpath('b')[0].text
        growth = row.xpath('b')[0].tail.strip(' +')
        print('Attribute: %s, %s+%s' % (attr_name, base, growth))


def parse_stats(stats_rows):
    header = stats_rows[0] #  unused, just says base/1/16/25
    hit_points = stats_rows[1].xpath('td')
    # hit_points[0] is empty because it's the header column
    print('base hp: %s' % hit_points[1].text)
    print('level 1 hp: %s' % hit_points[2].text)
    print('level 16 hp: %s' % hit_points[3].text)
    print('level 25 hp: %s' % hit_points[4].text)
    health_regen = stats_rows[2].xpath('td')
    # health_regen[0] is empty because it's the header column
    print('base health regen: %s' % health_regen[1].text)
    print('level 1 health regen: %s' % health_regen[2].text)
    print('level 16 health regen: %s' % health_regen[3].text)
    print('level 25 health regen: %s' % health_regen[4].text)

    # TODO: mana, manan regen, attack damage, armor, attack speed

def parse_single_hero(single_page):
    """
    :param single_page: html document, parsed for example using html.fromstring
    :return: TODO
    """
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
    parse_attributes(attributes_rows)

    # various attrs at different levels (base, 1, 16, 25)
    stats_rows = infobox_rows[3].xpath('td/table/tr')
    parse_stats(stats_rows)

    # attrs that don't change per level like movement speed, turn rate, etc
    other_attrs = infobox_rows[4]

with open('earthshaker.html') as f:
    single_page = html.fromstring(f.read(), parser=html.html_parser)
    parse_single_hero(single_page)
    f.close()

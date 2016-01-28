# scratch work to test stuff
from lxml import html

from representation.hero import Hero

print 'NOTE: for some reason this only works if the html has been formatted (indented properly, separate lines, etc)'


def parse_attributes(attributes_rows, hero):
    for row in attributes_rows:
        attr_name = row.xpath('a')[0].attrib['title']
        base = row.xpath('b')[0].text
        growth = row.xpath('b')[0].tail.strip(' +')
        hero.attr_growth[attr_name] = (base, growth)


def parse_stats(stats_rows, hero):
    header = stats_rows[0] #  unused, just says base/1/16/25
    for row in stats_rows[1:]:
        row_elems = row.xpath('td')
        attr_name = row_elems[0].xpath("b/a")[0].text
        if attr_name is None:
            attr_name = row_elems[0].xpath("b/a/span")[0].text
        hero.scaling_attrs[attr_name] = (row_elems[1].text, row_elems[2].text, row_elems[3].text, row_elems[4].text)

def parse_other_attrs(other_attr_rows, hero):
    for row in other_attr_rows:
        name_elem = row.xpath('td/b/a')
        if len(name_elem) > 0:
            name = name_elem[0].text
        else:
            name = row.xpath('td/b')[0].text
        value = row.xpath('td')[1].text.lstrip()
        # Some of the values are in a span.
        if len(value.strip()) == 0:
            value = row.xpath('td/span[@id="tooltip"]')[0].text
        hero.kv_attrs[name] = value

def parse_single_hero(single_page):
    """
    :param single_page: html document, parsed for example using html.fromstring
    :return: TODO
    """
    hero = Hero()

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
    hero.name = name

    # Strength/Agility/Intelligence base + growth
    attributes = infobox_rows[2]
    attributes_rows = attributes.xpath('td/table/tr/th')
    parse_attributes(attributes_rows, hero)

    # various attrs at different levels (base, 1, 16, 25)
    stats_rows = infobox_rows[3].xpath('td/table/tr')
    parse_stats(stats_rows, hero)

    # attrs that don't change per level like movement speed, turn rate, etc
    other_attrs = infobox_rows[4].xpath('td/table/tr')
    parse_other_attrs(other_attrs, hero)
    hero.pretty_print()

with open('earthshaker.html') as f:
    single_page = html.fromstring(f.read(), parser=html.html_parser)
    parse_single_hero(single_page)
    f.close()

# https://www.hackerrank.com/challenges/xml-1-find-the-score


def score(xml):
    import xml.etree.ElementTree as etree
    tree = etree.fromstring(xml)
    return sum([len(i.attrib) for i in tree.iter()])

if __name__ == '__main__':
    xml = '\n'.join([raw_input() for i in range(input())])
    print score(xml)

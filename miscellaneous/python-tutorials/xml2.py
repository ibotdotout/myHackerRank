# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth


def depth(xml):
    def _depth(tags):
        dp = 0
        if tags is not None:
            for i in tags:
                dp = max(dp,  _depth(i) + 1)
        return dp

    import xml.etree.ElementTree as etree
    tree = etree.fromstring(xml)
    return _depth(tree)


if __name__ == '__main__':
    xml = '\n'.join([raw_input() for i in range(input())])
    print depth(xml)

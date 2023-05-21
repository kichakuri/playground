import re


def get_first_regex():
    urls = """
        hello
        2020-05-20
        http://python-engineer.com
        http://www.pyeng.net
        https://gadeassociates.co.ke
        https://www.zeraki.app
        """

    #    pattern=re.compile(r'https:?://(www\.)?([a-zA-Z-]+)(\.\w+)')
    #    matches=pattern.finditer(urls)

    my_string = 'hello world. you are the best world'
    pattern = re.compile(r'Hello', re.I)
    matches = pattern.finditer(my_string)
    for match in matches:
        print(match)

#    subbed_urls = pattern.sub(r"\2\3",urls)
#    print(subbed_urls)

#        print(match.group(0))
#        print(match.group(1))
#        print(match.group(2))
#        print(match.group(3))
#        print(match.start(), match.end())
#        print(match.span)
#        print(match.group()[0])

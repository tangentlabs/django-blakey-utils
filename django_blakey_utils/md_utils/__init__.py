import re

class MarkdownPatterns:
    #![Alt text](/path/to/img.jpg "Optional title")
    IMAGE_INLINE_PATTERN = re.compile(r"""!\[(?P<name>([^\]]|\n)*?)\]   # ![Alt text]
            (?P<url_data>
                \(                                                  # (
                    (?P<url>[^\s\'\"]*)                             # /path/to/img.jpg
                    (?P<title_data>
                        \s*?                                         # whitespaces
                        ([\"\'](?P<title>(.|\n)*)[\"\'])?                # "Optional title", optional
                    )
                \)                                                  # )
            )""",  re.VERBOSE)
    #[an example](http://example.com/ "Title") for links that are like:
    LINK_INLINE_PATTERN = re.compile(r"""([^!]|^)\[(?P<name>([^\]]|\n)*?)\] # [an example]
            (?P<url_data>
                \(                                              # (
                    (?P<url>[^\s\'\"]*)                         # http://example.com/
                    (?P<title_data>
                        \s*?                                     # whitespaces
                        ([\"\'](?P<title>(.|\n)*)[\"\'])?            # "Title", optional
                    )
                \)                                              # )
            )""",  re.VERBOSE)
    GROUP_URL, GROUP_NAME, GROUP_TITLE, GROUP_URL_DATA, GROUP_TITLE_DATA = ("url", "name", "title", "url_data", "title_data")

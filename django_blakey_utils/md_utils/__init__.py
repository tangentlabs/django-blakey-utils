import re

class MarkdownPatterns:
    #![Alt text](/path/to/img.jpg "Optional title")
    IMAGE_INLINE_PATTERN = re.compile(r"""!\[(?P<name>[^\]]*?)\]   # ![Alt text]
             (?P<url_data>
                 \(                                                  # (
                     (?P<url>[^\'\"]*?)                             # /path/to/img.jpg
                     (?P<title_data>
                         \s*?                                         # whitespaces
                         ([\"\'](?P<title>(.|\s)*)[\"\'])?                # "Optional title", optional
                     )\s*
                 \)                                                  # )
             )""",  re.VERBOSE)
    #[an example](http://example.com/ "Title") for links that are like:
    LINK_INLINE_PATTERN = re.compile(r"""
(([^!])|^) # cannot start with !
 \[
 (?P<name>
                 (                     # link name can have image nested
                 [^\[\]]*?|
                 ( [^\[\]]*
                 \[
                 (.|\s)*?
                 \]
                 [^\[\]]*?)
                 )
 )\]
            (?P<url_data>
                \(                                              # (
                    (?P<url>[^\'\"]*?)                             # url
                     (?P<title_data>
                         \s*?                                         # whitespaces
                         ([\"\'](?P<title>(.|\s)*)[\"\'])?                # "Optional title", optional
                     )\s*
                \)                                              # )
            )""",  re.VERBOSE)
    GROUP_URL, GROUP_NAME, GROUP_TITLE, GROUP_URL_DATA, GROUP_TITLE_DATA = ("url", "name", "title", "url_data", "title_data")

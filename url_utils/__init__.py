import urllib
import urlparse

def add_get_parameters(url, **kwargs):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4], keep_blank_values=True, strict_parsing=False))
    query.update(**kwargs)
    url_parts[4] = urllib.urlencode(query)
    return urlparse.urlunparse(url_parts)

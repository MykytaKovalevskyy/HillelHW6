from urllib import parse
from http.cookies import SimpleCookie


def parse_parameters(query: str) -> dict:
    return dict(parse.parse_qsl(parse.urlsplit(query).query))


def parse_cookies(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('https://www.python.org?') == {}
    assert parse_parameters('https://www.google.com/search?q=python&rlz=1C1GCEJ_enPL879PL879&sxsrf=AOaemvLDGaqzG7g'
                            'Q540fg3xMB0s9qEmJag%3A1637058472990&ei=qIeTYf_-O6zprgTVrKioCA&oq=python&gs_lcp=Cgdnd3Mt'
                            'd2l6EAMyBAgjECcyBAgjECcyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAE'
                            'MgUIABCABDoECAAQQzoFCC4QgAQ6CwguEIAEEMcBENEDOgsILhCABBDHARCjAjoKCAAQgAQQhwIQFDoHCCMQsQIQ'
                            'JzoECAAQCkoECEEYAFAAWNIQYO4RaAFwAngAgAF1iAGeBZIBAzUuMpgBAKABAcABAQ&sclient=gws-wiz&ved=0a'
                            'hUKEwj_8oiG1pz0AhWstIsKHVUWCoUQ4dUDCA4&uact=5') == {
               'q': 'python', 'rlz': '1C1GCEJ_enPL879PL879', 'sxsrf':
               'AOaemvLDGaqzG7gQ540fg3xMB0s9qEmJag:1637058472990',
               'ei': 'qIeTYf_-O6zprgTVrKioCA', 'oq': 'python',
               'gs_lcp': 'Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQg'
                         'AQyBQgAEIAEMgUIABCABDoECAAQQzoFCC4QgAQ6CwguEIAEEMcBENEDOgsILhCABBDHARCjAjoKCAAQgAQQhwIQFD'
                         'oHCCMQsQIQJzoECAAQCkoECEEYAFAAWNIQYO4RaAFwAngAgAF1iAGeBZIBAzUuMpgBAKABAcABAQ',
               'sclient': 'gws-wiz', 'ved': '0ahUKEwj_8oiG1pz0AhWstIsKHVUWCoUQ4dUDCA4', 'uact': '5'}
    assert parse_parameters('https://www.olx.pl/elektronika/gry-konsole/?search%5Bfilter_float_price%3Afrom%5D=500'
                            '&search%5Bfilter_enum_state%5D%5B0%5D=used') ==\
           {'search[filter_float_price:from]': '500', 'search[filter_enum_state][0]': 'used'}
    assert parse_parameters('https://www.facebook.com/search/top?q=friend') == \
           {'q': 'friend'}
    assert parse_parameters('https://allegro.pl/listing?string=iphone&offerTypeAuction=2') == {
               'string': 'iphone', 'offerTypeAuction': '2'}


    # Tests for function "parse_cookies"

    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('name=Dima;id=007') == {'name': 'Dima', 'id': '007'}
    assert parse_cookies('text=%D0%BD%D0%BE%D1%81%D0%BA%D0%B8; class=0; redirected=1') == \
           {'text': '%D0%BD%D0%BE%D1%81%D0%BA%D0%B8', ' class': '0', ' redirected': '1'}
    assert parse_cookies('name=Dima;age=20;height=194;weight=80') ==\
           {'name': 'Dima', 'age': '20', 'height': '194', 'weight': '80'}

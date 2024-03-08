countries = (
    {"country": "뉴질랜드", "code": 554, "alpha3": "NZL", "alpha2": "NZ"},
    {"country": "대한민국", "code": 410, "alpha3": "KOR", "alpha2": "KR"},
    {"country": "미국", "code": 840, "alpha3": "USA", "alpha2": "US"},
)

def print_country(country, code, alpha3, alpha2):
    print(f"{country} {code} {alpha3} {alpha2}")

def print_all_countries(countries):
    for i in countries:
        print_country(**i)


print_all_countries(countries)

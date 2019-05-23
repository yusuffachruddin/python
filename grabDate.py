from dateutil.parser import parse

parse("Today is 12-01-18", fuzzy_with_tokens=True)
parse("Today is 20190703", fuzzy_with_tokens=True)
parse("I'm born in 3 July 1984", fuzzy_with_tokens=True)
parse("Today is December 1, 2018", fuzzy_with_tokens=True)

parse("Today is Dec 1 2018", fuzzy_with_tokens=True)

parse("Today is Dec 1", fuzzy_with_tokens=True)

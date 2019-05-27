from dateparser.search import search_dates

search_dates("find 12/15/18 in this string")

search_dates("Today is 12-01-18")
search_dates("Today is December 1, 2018")

search_dates("Today is Dec 1 2018")

search_dates("Today is Dec 1")
search_dates("Today is Dec 1 16")

search_dates("Today is Dec 1 14")

search_dates("Today is Nov 30 12")

results = search_dates("Today is December 1, 2018")
# exclude results matching to “today”
need = [result for result in results if result[0].lower() != "today"]

for x in need:
    date_string = x[0]
date_string

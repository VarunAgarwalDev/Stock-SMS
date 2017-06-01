import requests
from lxml import html
from bs4 import BeautifulSoup

companies = ["AMD", "NVDA", "INTC"]

PERCENT_CHANGE_THRESHOLD_MIN = .25

def get_data(inputCompany):
    url = "https://finance.yahoo.com/quote/" + inputCompany + "?p=" + inputCompany
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    # This will get all the data from the summary table
    table_data = soup.find("div", {"id":"quote-summary"})
    table_rows = table_data.find_all("span")

    summary_table = {}
    count = 0
    #
    # while count < len(table_rows)/2:
    #     summary_table[table_rows[count].text.decode()] = table_rows[count+1].text.decode()
    #     count+=2

    summary_table["Percent Change"] = soup.find("span", {"data-reactid":"37"}).text
    summary_table["Current Price"] = soup.find("span", {"data-reactid":"36"}).text

    return summary_table

for company in companies:
    tempData = get_data(company)
    curChange = float(tempData["Percent Change"].split()[1][2:-2])
    if (curChange) > PERCENT_CHANGE_THRESHOLD_MIN:
        print("" + company + " has changed: " + str(curChange) + "%")
        # Send SMS with the name of the company to check AND the percent change


# print(get_data("NVDA"))

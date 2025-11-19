import requests
from bs4 import BeautifulSoup, Tag


class SiteReader:
    def __init__(self, url: str):
        self.url = url

    def read_site(self) -> list[Tag]:
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        area = soup.find("div", class_="mainArea")
        return area.find_all("section")
    
    def search_rule(self) -> list[Tag]:
        rule_list = []
        for section in self.read_site():
            title = section.find("h4")
            if title and title.text == "日本陸上競技連盟競技規則":
                rule_list.append(section)
        return rule_list

if __name__ == "__main__":
    site_reader = SiteReader("https://www.jaaf.or.jp/about/rule/")
    print(site_reader.search_rule())

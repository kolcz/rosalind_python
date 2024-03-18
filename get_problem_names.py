import sys
import requests
from html.parser import HTMLParser

class SimpleHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print("starttag", tag)
    def handle_data(self, data):
        print("data", data)

if __name__ == "__main__":

    base_url = "https://rosalind.info/problems/list-view/?location="
    groups = ("python-village", "bioinformatics-stronghold", "bioinformatics-armory", "bioinformatics-textbook-track", "algorithmic-heights")

    args = sys.argv
    match len(args):
        case 2:
            url = base_url + args[1]
        case _:
            print("Specify problem group. Available groups are:\n" + "/".join(groups) + "\n")
            sys.exit(1)

    response = requests.get(url)
    
    if response.status_code == 200:
        parser = SimpleHTMLParser()
        parser.feed(response.text)


    
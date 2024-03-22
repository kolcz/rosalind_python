import sys
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    base_url = "https://rosalind.info/problems/list-view/?location="
    groups = ("python-village", "bioinformatics-stronghold", "bioinformatics-armory", "bioinformatics-textbook-track", "algorithmic-heights")

    args = sys.argv
    match len(args):
        case 2:
            if args[1] in groups:
                url = base_url + args[1]
            else:
                print("Group isn't recognized! Available groups are:\n" + "/".join(groups) + "\n")
                sys.exit(1)
        case _:
            print("Specify problem group! Available groups are:\n" + "/".join(groups) + "\n")
            sys.exit(1)

    response = requests.get(url)
    with open("response.html", "w") as f:
        f.write(response.text)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        table = soup.find("table")
        print(len(table.find_all("a"))) #TODO: parse links to get problem id's

    
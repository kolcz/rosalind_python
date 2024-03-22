import sys
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import os.path

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

    try:
        response = requests.get(url)
    except ConnectionError:
        print("Connection error!")
        sys.exit(1)
    
    problems = set()
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        table = soup.find("table")
        links = table.find_all("a")
        for link in links:
            href = link.get("href")
            if href.startswith("/problems/"):
                problem = href.split("/")[2]
                problems.add(problem)
                
    problems_dir = "problems"
    problems_path = os.path.join(problems_dir, f"{args[1]}.txt")
    with open(problems_path, "w") as f:
        f.write("\n".join(problems))
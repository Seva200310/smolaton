
import requests
import json
from bs4 import BeautifulSoup





# import wikisearch
class Articles:
    def __init__(self):
        pass
    def search(self):
        with open("file.json","r", encoding="utf-8") as file:
            data = json.load(file)
            ans = []
            for link in data:
                rep = [",", " ", "-", "'", "(", ")"]
                for item in rep:
                    if item in link:
                        link = link.replace(item, "_")
                url = "https://ru.wikipedia.org/wiki/" + link
                ans.append(url)
                return ans


    def parsing(self, new_parameter):
        countm = []
        url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BC%D0%BE%D0%BB%D0%B5%D0%BD%D1%81%D0%BA"

        response = requests.get(url)
        src = response.text
        with open('test1.html', 'w', encoding='utf-8') as f:
            res = f.write(src)

        for i in self.search():
            count = 0
            url = i
            response = requests.get(url)
            src = response.text

            # Create BeautifulSoup object
            soup = BeautifulSoup(src, 'html.parser')

            # Replace all links with a specific parameter

            for link in soup.find_all('a', href=True):
                link['href'] = link['href'] + new_parameter
                count +=1
            countm.append(count)
            # Save the modified HTML content
            with open('modified_test1.html', 'w', encoding='utf-8') as modified_file:
                modified_file.write(str(soup))
            return countm

    def level_setter(self,link, links):
        levels = {'E': range(1, 6), 'D': range(6, 11), 'C': range(11, 16), 'B': range(16, 21), 'A': range(21, 26)}

        for level, link_range in levels.items():
            if links in link_range:
                return level
        return

        level = determine_level(links)
        return f"articles.bib = {{{link}, {level}, {links}}}"

    def transcription(text):
        mapping = {
            'А': 'A', 'а': 'a',
            'В': 'B',
            'Е': 'E', 'е': 'e',
            'К': 'K',
            'М': 'M',
            'О': 'O', 'о': 'o',
            'Р': 'P', 'р': 'p',
            'С': 'C', 'с': 'c',
            'у': 'y',
            'Х': 'X', 'х': 'x'
        }
        r = ''
        for char in text:
            if char in mapping:
                r += mapping[char]
            else:
                r += char
        return r





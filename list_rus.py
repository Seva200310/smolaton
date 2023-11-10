levels = {'E': range(1, 6), 'D': range(6, 11), 'C': range(11, 16), 'B': range(16, 21), 'A': range(21, 26)}

input_articles = {'h//12': 11, 'h//123': 22, 'h//1234': 7}
def determine_level(links):
    for level, link_range in levels.items():
        if links in link_range:
            return level
    return

def generate_article(link, links):
    level = determine_level(links)
    return f"articles.bib = {{{link}, {level}, {links}}}"


for article, links in input_articles.items():
    print(generate_article(article, links))
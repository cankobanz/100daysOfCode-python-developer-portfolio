from bs4 import BeautifulSoup
import requests

response = requests.get(
    'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
data = response.text
soup = BeautifulSoup(data, "html.parser")

with open("top100film.txt", mode="w", encoding="utf-8") as file:
    for p in soup.find_all(name="h3", class_="title"):
        movie_name_order = p.getText()
        file.write(movie_name_order + "\n")

# response = requests.get('https://news.ycombinator.com/news')
# data = response.text
#
# soup = BeautifulSoup(data, "html.parser")
#
# article_link = []
# article_text = []
# article_upvote = [int(score.getText().split()[0])
#                   for score in soup.find_all(name="span", class_="score")]
#
# articles = soup.select(selector=".titleline")
#
# for article in articles:
#     article_link.append(article.select_one(selector='a').get("href"))
#     article_text.append(article.getText())
#
# zipped_articles = zip(article_link, article_text, article_upvote)
#
# highest_index = article_upvote.index(max(article_upvote))
#
# print(article_text[highest_index], article_link[highest_index])

# with open("https://www.cmpe.boun.edu.tr/~say/") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")

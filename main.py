import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pprint import pprint

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_correct_years_text():
    days = 365 * 1920
    years = (datetime.datetime.now() - datetime.timedelta(days=days)).year
    names = {
        1: 'год',
        2: 'года',
        3: 'года',
        4: 'года',
    }
    last_two_numbers = str(years)[-2:]
    if last_two_numbers in range(11, 21):
        return f'{years} лет'
    return f'{years} {names[int(last_two_numbers)]}'


def get_wines_from_file():
    excel_df = pd.read_excel('wine.xlsx', sheet_name='Лист1', na_values='nan', keep_default_na=False)
    getted_wines = excel_df.to_dict()
    count_new_wines = len(getted_wines['Категория'].keys())

    wines = collections.defaultdict(list)
    for index in range(count_new_wines):
        category = getted_wines['Категория'][index]
        wines[category].append({
            'Картинка': getted_wines['Картинка'][index],
            'Категория': getted_wines['Категория'][index],
            'Название': getted_wines['Название'][index],
            'Сорт': getted_wines['Сорт'][index],
            'Цена': getted_wines['Цена'][index],
            'Акция': getted_wines['Акция'][index],
        })
    return wines


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    correct_years_text = get_correct_years_text()
    wines = get_wines_from_file()

    rendered_page = template.render(years=correct_years_text, wines=wines)
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()  # place main logic here


if __name__ == '__main__':
    main()

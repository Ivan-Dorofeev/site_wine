import argparse
import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_correct_years_text():
    difference_age = datetime.datetime.now().year - 1920
    names = {
        1: 'год',
        2: 'года',
        3: 'года',
        4: 'года',
    }
    last_two_numbers_of_year = str(difference_age)[-2:]
    if last_two_numbers_of_year in range(11, 21):
        return f'{difference_age} лет'
    return f'{difference_age} {names[int(last_two_numbers_of_year)]}'


def get_wines_from_file():
    parser = argparse.ArgumentParser(
        description='Программа принимает на вход название файла, который считывает'
                    ' и добавляем информацию по нему на сайт'
    )
    parser.add_argument('file_name', help='Введите имя excel файла')
    args = parser.parse_args()

    excel_df = pd.read_excel(args.file_name, sheet_name='Лист1', na_values='nan', keep_default_na=False)
    getted_wines = excel_df.to_dict()

    wines = collections.defaultdict(list)
    for number_wine, category_wine in getted_wines['Категория'].items():
        wines[category_wine].append({
            'Картинка': getted_wines['Картинка'][number_wine],
            'Категория': getted_wines['Категория'][number_wine],
            'Название': getted_wines['Название'][number_wine],
            'Сорт': getted_wines['Сорт'][number_wine],
            'Цена': getted_wines['Цена'][number_wine],
            'Акция': getted_wines['Акция'][number_wine],
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

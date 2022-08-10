import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def correct_years_text(years):
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


days = 365 * 1920
years = (datetime.datetime.now() - datetime.timedelta(days=days)).year
correct_years_text = correct_years_text(years)

excel_df = pd.read_excel('wine.xlsx', sheet_name='Лист1')
wines = excel_df.to_dict()

rendered_page = template.render(years=correct_years_text, wines=wines)
with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

"""
Используем шаблонизатор jinja2
"""
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

import os
import sys

sys.path.append('../')


def render(template_name, folder='templates', **kwargs):
    """
    Минимальный пример работы с шаблонизатором
    :param template_name: имя шаблона
    :param folder: папка с шаблонами
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    file_loader = FileSystemLoader(folder)
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    content = template.render(**kwargs).encode('utf-8')

    return content


if __name__ == '__main__':
    # Пример использования
    output_test = render('authors.html', folder='\\mysite\\templates', object_list=[{'name': 'Leo'}, {'name': 'Kate'}])
    print(output_test)

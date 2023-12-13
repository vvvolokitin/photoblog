from flask import Blueprint, render_template, request

from functions import load_posts


main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    template_folder='templates'
)


@main_blueprint.route('/')
def main_page() -> str:
    """
    Возвращает главную страницу.

    Вывод на главную страницу поисковой строки и функции добавления поста.

    Возвращаемое значение:
        str: главная страница сайта.
    """
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page() -> str:
    """
    Возвращает поисковую страницу.

    Вывод на экран результатов поискового запроса.

    Возвращаемое значение:
        str: Результат поискового запроса.
    """
    search_word = request.args['s']
    posts = [
        element for element in load_posts() if search_word.lower()
        in element['content'].lower()
    ]
    return render_template(
        'post_list.html',
        search_word=search_word,
        posts=posts
    )

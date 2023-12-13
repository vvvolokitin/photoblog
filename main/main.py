from flask import Blueprint, render_template

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

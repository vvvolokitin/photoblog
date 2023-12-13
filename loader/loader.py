from flask import Blueprint, render_template, request

from functions import load_posts


loader_blueprint: Blueprint = Blueprint(
    'loader_blueprint',
    __name__,
    url_prefix='/post',
    static_folder='static',
    template_folder='templates'
)


@loader_blueprint.route('/form/')
def main_page() -> str:
    """
    Возвращает страницу загрузки.

    Возвращаемое значение:
        str: Страница загрузки поста.
    """
    return render_template('post_form.html')

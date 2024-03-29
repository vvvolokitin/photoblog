from flask import Blueprint, render_template, request

import logging

from functions import load_posts, upload_posts


logging.basicConfig(encoding='utf-8', level=logging.INFO)

loader_blueprint: Blueprint = Blueprint(
    'loader_blueprint',
    __name__,
    url_prefix='/post',
    static_folder='static',
    template_folder='templates'
)


@loader_blueprint.route('/form/')
def loader_page() -> str:
    """
    Возвращает страницу загрузки.

    Возвращаемое значение:
        str: Страница загрузки поста.
    """
    return render_template('post_form.html')


@loader_blueprint.route('/upload/', methods=['GET', 'POST'])
def upload_page():
    """
    Загрузка поста.

    Возвращаемое значение:
        None.
    """
    try:
        file = request.files['picture']
        filename = file.name
        content = request.values['content']
        posts = load_posts()
        posts.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        upload_posts(posts)
        file.save(f'uploads/images/{filename}')
        if filename.split('.')[-1].lower() not in ('png', 'jpeg', 'jpg'):
            logging.info(f'Файл не изображение {filename}')
    except FileNotFoundError:
        logging.error('Ошибка при загрузке файла')
        return '<h1>Файл не найден</h1><br><a href="//" class="link">Назад</a>'
    else:
        return render_template(
            'post_uploaded.html',
            pic=f'/uploads/images/{filename}',
            content=content
        )

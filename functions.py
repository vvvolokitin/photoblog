import json


POST_PATH = 'posts.json'


def load_posts() -> list[dict[str, str]]:
    """
    Возвращает список постов.

    Возвращаемое значение:
        posts_list: list[dict[str, str]]: Информация о постах.
    """
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts_list: list[dict[str, str]] = json.load(file)
    return posts_list


def upload_posts(posts):
    """
    Загружает пост.
    """
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file)

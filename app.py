from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    apps = [
        {"name": "МАКС", "rating": "4,2", "icon": "max.webp", "category": "Общение", "url": "https://www.rustore.ru/catalog/app/ru.oneme.app"},
        {"name": "VK Видео", "rating": "4,6", "icon": "vk-video.webp", "category": "Развлечения", "url": "https://www.rustore.ru/catalog/app/com.vk.vkvideo"},
        {"name": "ВКонтакте", "rating": "4,2", "icon": "vk.webp", "category": "Общение", "url": "https://www.rustore.ru/catalog/app/com.vkontakte.android"},
    ]
    return render_template("index.html", apps=apps)


if __name__ == "__main__":
    app.run()

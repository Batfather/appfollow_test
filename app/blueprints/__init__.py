from .news import news_blueprint


def register_blueprints(app):
    app.register_blueprint(news_blueprint)

from flask import (
    Blueprint,
    jsonify,
    request,
    abort
)
from webargs.flaskparser import parser
from .schemas import get_posts_schema
from app import mongo

news_blueprint = Blueprint('news', __name__)


@news_blueprint.route('/posts', methods=['GET'])
def get_posts():
    args = parser.parse(get_posts_schema, request, location='query')
    news = mongo.db.news.find()
    news_list = [{"title": news_item["title"],
                  "url": news_item["url"],
                  "created_at": news_item["created_at"]}
                 for news_item in news]
    order = args.get('order', None)
    limit = args.get('limit', 5)
    offset = args.get('offset', 0)

    if order:
        news_list = sorted(news_list, key=lambda x: x[order])

    start = offset
    stop = limit + offset
    news_list = news_list[start:stop]

    return jsonify(news_list), 200


@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    abort(400, err.messages)

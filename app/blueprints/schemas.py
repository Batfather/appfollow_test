from webargs import fields, validate

get_posts_schema = {
    'order': fields.String(validate=validate.OneOf(choices=['url', 'title', 'created_at']),),
    'limit': fields.Integer(validate=validate.Range(min=0, max=100)),
    'offset': fields.Integer(validate=validate.Range(min=0, max=100)),
}
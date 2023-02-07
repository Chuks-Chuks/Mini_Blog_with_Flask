from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

blog_endpoint = 'https://api.npoint.io/c790b4d5cab58020d391'
blog_request = requests.get(blog_endpoint)
blog_data = blog_request.json()
post_objects = [Post(posts['id'], posts['title'], posts['subtitle'], posts['body']) for posts in blog_data]
print(post_objects)



@app.route('/')
def home():
    return render_template("index.html", blog=post_objects)


@app.route('/post/<int:blog_id>')
def post(blog_id):
    read_blog = None
    for blog_ in post_objects:
        if blog_.id == blog_id:
            read_blog = blog_
    return render_template('post.html', open_blog=read_blog)


if __name__ == "__main__":
    app.run(debug=True)

import csv

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    # 1. Open the post html and get the contents as a string
    post_file = open('post.html', 'r')
    post_html = post_file.read()
    post_file.close()

    # 2. Create a new list that will hold all the html for your blog posts
blog_html_content = []

    # 3. Open the csv file and read it using the CSV library. This will give you a list of rows.
    # See: https://docs.python.org/3/library/csv.html#csv.DictReader


    with open('data.csv') as csvfile:
    # same as csvfile = open('data.csv') and closes after indent
        blog_posts = csv.DictReader(csvfile)


    # 4. Loop over each row in the CSV. Each row is a blog post.
        for post in blog_posts:
            print(post['category'], post['title'], post['body'], post['author'], post['date'], post['image'])

    # 5. Take post_html and replace {{title}} {{body}} {{author}} with the data in each blog post csv row
    post_html.replace({{title}}, post['title'])
    post_html.replace({{body}}, post['body'])
    post_html.replace({{author}}, post['author'])

    # 6. Add the post_html to the new list you created above.

blog_html_content.append(post_html)

    # 7. Join all the items in your new list together into a single string. Name this string "blog_post_html".




    # 8. Open the index.html file and replace {{blog_posts}} with the blog post string you just created.
    index_file = open('index.html', 'r')
    index_html = index_file.read()

    # index_html = index_html.replace('{{blog_posts}}', blog_post_html)

    index_file.close()

    return index_html

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

    # post_html now contains a string of all the contents of post.html file

    # 2. Create a new list that will hold all the html for your blog posts
    blog_html_content = []
    # this is an empty list. save it for later

    # 3. Open the csv file and read it using the CSV library. This will give you a list of rows.
    # See: https://docs.python.org/3/library/csv.html#csv.DictReader


    with open('data.csv') as csvfile:

    # essentially the same as csvfile = open('data.csv') and closes after indent.
    #   we've created a variable, opened it, and we will close it after the indent

        blog_posts = csv.DictReader(csvfile)
        # This is saying, create a variable (a container) and name it
        #       "blog_posts" and fill it with the list from my csv file

    # So now, post_html contains a string of all contents of post.html file, and
    #      blog_posts contains (a list of?) all of the contents in csv file.

    #   post.html is the framework for the individual blog post and data.csv contains the specific
    #       info to populate into the posts

    #   so posts_html needs to be populated with blog_posts

    # 4. Loop over each row in the CSV. Each row is a blog post.
        for post in blog_posts:

            print(post['category'], post['title'], post['body'], post['author'], post['date'], post['image'])

            #prints the contents of blog_posts (a list of everything in data.csv)
            # Apparently, this prints to terminal, but not to the browser. I need another statement
            # somewhere to pull and populate individual posts

    # 5. Take post_html and replace {{title}} {{body}} {{author}} with the data in each blog post csv row

            unique_post = post_html

            unique_post = unique_post.replace("{{category}}", post['category'])
            unique_post = unique_post.replace("{{title}}", post['title'])
            unique_post = unique_post.replace("{{body}}", post['body'])
            unique_post = unique_post.replace("{{author}}", post['author'])
            unique_post = unique_post.replace("{{date}}", post['date' ])
            unique_post = unique_post.replace("{{image}}", post['image'])

    # 6. Add the post_html to the new list you created above.

            blog_html_content.append(unique_post)
            # all the contents of post.html that were read and stored in post_html are now list items
            # in the list blog_html_content

    # 7. Join all the items in your new list together into a single string. Name this string "blog_post_html".

    blog_post_html = "".join(blog_html_content)


    # 8. Open the index.html file and replace {{blog_posts}} with the blog post string you just created.
    index_file = open('index.html', 'r')
    index_html = index_file.read()

    index_html = index_html.replace('{{blog_posts}}', blog_post_html)

    index_file.close()

    return index_html

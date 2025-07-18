from flask import Flask, render_template, redirect, url_for
from datetime import date
from base import app, db
from model import BlogPost
from form import PostForm

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    all_posts = db.session.execute(db.select(BlogPost))
    posts = all_posts.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title = form.post_title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.image_url.data,
            author=form.author.data,
            date=date.today().strftime("%d/%m/%Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make_post.html")



# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    # Fetch a BliogPost record from the database by ID.
    post = db.get_or_404(BlogPost, post_id)

    #Create a form pre-filled with the blog post data (only on GET)
    edit_form = PostForm(title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body)
    
    # On POST, validate and update the post
    if edit_form.validate_on_submit():
        post.title = edit_form.post_title
        post.subtitle = edit_form.subtitle
        post.body = edit_form.body
        post.img_url = edit_form.image_url
        post.author = edit_form.author
        db.session.commit()
        return redirect(url_for("show_post"), post_id=post.id)

    return render_template("make-post.html", form=edit_post, is_edit=True)



# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

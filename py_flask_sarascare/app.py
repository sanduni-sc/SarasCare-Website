from flask import Flask

app = Flask(__name__)


#creating routes for pages     
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/index.php/about-us/')
def about():
    return render_template('about-us.html', title='About')

@app.route('/index.php/mcd/')
def mcd():
    return render_template('mcd.html', title='Monthly Charity Drive')

@app.route('/index.php/acd/')
def acd():
    return render_template('acd.html', title='Annual Charity Drive')

@app.route('/index.php/portfolio/')
def portfolio():
    return render_template('portfolio.html', title='Portfolio')

@app.route('/index.php/testimonials/')
def testimonial():
    return render_template('testimonials.html', title='Testimonials')

@app.route('/index.php/blog/')
def blog():
    return render_template('blog.html', title='Blog')

@app.route('/index.php/contact-us/')
def contact():
    return render_template('contact-us.html', title='Contact')

if __name__ == '__main__':
    app.run(port=8000, debug=True)


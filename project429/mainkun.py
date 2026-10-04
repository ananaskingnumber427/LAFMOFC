from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])


def title_mew():
    songlok = ''
    if request.method == 'POST':
        songlok = request.form.get('loksong', type=str)
    return render_template('base_mew.html', loksong=songlok)

     
@app.route("/eatinrats")
def post1():
    return render_template('post_1.html')


@app.route("/flush")
def post2():
    return render_template('post_2.html')


@app.route("/cristalinedreams")
def post3():
    return render_template('post_3.html')


@app.route("/chumbucketkitty")
def post4():
    return render_template('post_4.html')

@app.route("/themkittybones")
def post5():
    return render_template('post5.html')

@app.route("/guilotina")
def post6():
    return render_template('post_6.html')

@app.route("/sweetdelicious")
def post7():
    return render_template('post_7.html')

@app.route("/throbingking")
def post8():
    return render_template('post_8.html')
       


    
app.run(debug=True)

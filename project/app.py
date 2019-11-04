from flask import Flask, render_template, url_for, request, redirect
from database import Database
from retrieve import retrieve_info, add_query

Database.initialise(user='postgres', password='1234', database='cs460',
                    host='localhost', port="5433")

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def homepage():
    if request.method == 'POST':
        task_content = request.form['content']
        print(task_content)
        try:
            result = retrieve_info(task_content)
            return render_template('pa1_website_QID.html', header='Executed Successfully', result=result)
        except:
            return render_template('pa1_website_QID.html', header='Something went wrong', result='')
    else:
        return render_template('pa1_website_QID.html', header='Welcome enter your query', result='')


@app.route('/checks_in', methods=['POST', 'GET'])
def check_in():
    if request.method == 'POST':
        user_id = request.form['checksinUser_id']
        business_id = request.form['checksinBusiness_id']
        day_of_week = request.form['options']
        date = request.form['checksinDate']
        to_add = "insert into checks_in (business_id, user_id, check_in_date) values ('" + business_id + "', '" + user_id + "', '" + date + "')"
        print(to_add)
        if day_of_week != '':
            try:
                add_query(to_add)
                result = retrieve_info("select * from checks_in where user_id = '" + user_id + "'")
                # now update day
                day_update = "update checkins set " + day_of_week + " = " + day_of_week + " + 1 where business_id = '" + business_id + "'"
                add_query(day_update)
                return render_template('pa1_website_userCheckin.html', header='Executed successfully', result=result)
            except:
                return render_template('pa1_website_userCheckin.html', header='Something went wrong', result='')
        else:
            return render_template('pa1_website_userCheckin.html', header='You must choose a day', result='')
    else:
        return render_template('pa1_website_userCheckin.html', header='Execute something to see what happens',
                               result='')


@app.route('/write_reviews', methods=['POST', 'GET'])
def write_review():
    if request.method == 'POST':
        user_id = request.form['reviewUser_id']
        print(type(user_id))
        business_id = request.form['reviewBusiness_id']
        print(type(business_id))
        date = request.form['checksinDate']
        print(type(date))
        review_text = request.form['text']
        print(type(review_text))
        stars = request.form['options']
        print(type(str(stars)))
        tuple1 = retrieve_info('select * from reviews')
        print(tuple1)
        num = str(len(retrieve_info('select * from reviews')))
        print(type(num))
        print('' + user_id + business_id + date + review_text + stars)
        to_add = "insert into reviews (review_id, business_id, user_id, stars, review_date, votes_funny, votes_useful, votes_cool, review_text) values (" + num + ",'" + business_id + "','" + user_id + "'," + stars + ",'" + date + "', 0, 0, 0, '" + review_text + "')"
        print(to_add)
        if stars != '':
            try:
                add_query(to_add)
                result = retrieve_info('select * from reviews')
                add_query("update users set review_count = review_count + 1 where user_id = '" + user_id  +"'")
                return render_template('pa1_website_writeReview.html', header='Executed successfully', result=result)
            except:
                return render_template('pa1_website_writeReview.html', header='Something went wrong', result='')
        else:
            return render_template('pa1_website_writeReview.html', header=' Please choose a star', result='')
    else:
        return render_template('pa1_website_writeReview.html', header='Execute something to start', result='')


app.run(port=5000)

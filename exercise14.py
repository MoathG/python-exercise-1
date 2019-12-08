# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:19:57 2019

@author: Moath
"""

from flask import Flask
from flask import Flask,render_template
app = Flask(__name__)

# =============================================================================
# @app.route('/')
# def index():
#     return 'This is the Index page'
# 
# @app.route('/hello')
# def hello():
#     return "Hello World!"
# 
# @app.route('/members')
# def member():
#     return "Members page"
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================


# =============================================================================
# @app.route('/index/<int:marks>')
# def mark(marks):
#     return render_template('index.html',marks=marks)
# 
# if __name__ == '__main__':
#     app.run()
# =============================================================================


@app.route('/index')
def Q3():
    return render_template('app.html')
if __name__=='__main__':
    app.run()
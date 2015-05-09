'''This is the library files for all used code that needs to be
used multi times'''
import binascii
import cgi
import hashlib
import http.cookies
import os
import sqlite3
import time
import cgitb
cgitb.enable()

HTML_DIR = 'html\\'
REDIRECT_DIR = 'redirect\\'
DB_DIR = 'db\\'
COOKIE_MAX_AGE = 300
# COOKIE_DOMAIN = 'wiki.fallenofftheedge.com'
COOKIE_PATH = '/'
RAT_START = 1000


def open_conn(database):
    '''Open SQL Connection to a given sqlite databsase'''
    conn = sqlite3.connect(database)
    c = conn.cursor()
    return (conn, c)


def save_conn(conn):
    '''Savesthe conn'''
    conn.commit()


def save_close_conn(conn):
    '''Saves and closes the conn'''
    conn.commit()
    conn.close()


def close_conn(conn):
    '''Closes the database conn'''
    conn.close()


def get_cookies():
    '''returns a cookie opject of the request header sent to the server from
    the client'''
    cookie = http.cookies.BaseCookie()
    if 'HTTP_COOKIE' in os.environ:
        cookie.load(os.environ['HTTP_COOKIE'])
        return cookie
    return None


def print_header(cookie=''):
    '''Prints the standard HTTP header needed by CGI along with any cookie data
    sent to the function - cookie must be a cookie object'''
    print('Content-type: text/html')
    print('Status: 200 OK')
    print(cookie)
    if not cookie == '':
        print()


def get_html(filepath):
    '''For the given path it returns a str of all the data in that file.
    \n and all'''
    file = open(filepath)
    txt = file.read()
    return txt


def print_me(filename):
    '''prints file to screen - use for redirects'''
    file = open(filename)
    txt = file.read()
    print(txt)


def get_cgi_data():
    '''gets the cgi data from the last form the client summited'''
    cgidata = cgi.FieldStorage()
    return cgidata


def cookie_wright(sessionid, exp, username):
    '''give the imput data it returns a session cookie ment to be placed in the
    print_header function to send to the client'''
    cookie = http.cookies.BaseCookie()
    cookie['id'] = sessionid
    cookie['exp'] = exp
    cookie['username'] = username
    for morsel in cookie:
        cookie[morsel]['max-age'] = COOKIE_MAX_AGE
        # cookie[morsel]['domain'] = COOKIE_DOMAIN
        cookie[morsel]['path'] = COOKIE_PATH
    return cookie

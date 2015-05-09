import cgi
import cgitb
cgitb.enable()
from wiki import *

def link_pages_():
    pass
    # [[.*?]]
    # [[page_name | display]]
    # <a href='/index.py?=page_name' title='page_name'>display</a>


def templates():
    pass
    # {{.*?}}
    # {{Template_name}}
    # <tags>andtext and stuffs</tags> # may be multi line!!!


def main():
    conn, c = open_conn(DB_DIR + 'wiki.db')
    c.execute('SELECT data FROM pages WHERE title="main"')
    print_header()
    data = c.fetchone()
    print(data[0])
    close_conn(conn)

if __name__ == '__main__':
    main()

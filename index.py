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
    # os.environ["REQUEST_METHOD"] = "GET"
    # os.environ["QUERY_STRING"] = "title=HiHoHiHoItsOffToWorkWeGo"

    form = get_cgi_data()
    title = form.getfirst('title')
    if title == None: title = 'Main'

    conn, c = open_conn(DB_DIR + 'wiki.db')
    title = (title,)
    c.execute('SELECT data FROM pages WHERE title=?', title)
    data = c.fetchone()

    print(data[0])
    close_conn(conn)


    '''
    c.execute('SELECT data FROM pages WHERE title="main"')

    data = c.fetchone()
    print(data[0])
    close_conn(conn)
    '''


if __name__ == '__main__':
    print_header()
    main()

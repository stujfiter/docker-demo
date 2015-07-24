import web
        
urls = (
    '/users', 'users',
    '/(.*)', 'hello'
)

app = web.application(urls, globals())
db = web.database(dbn='postgres', host='postgres', db='dockerdemo', user='postgres', pw='mypasswd')

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'

        return 'Hello, ' + name + '!'

class users:
    def GET(self):
        entries = db.select('person')
        users = '<html><head></head><body><ol>'
        for person in entries:
            users += '<li>' + person.name + '</li>';

        users += '</ol></body></html>'
        return users

if __name__ == "__main__":
    app.run()

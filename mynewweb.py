import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return open(r'httpdoc\hello.html','r').read()

if __name__ == "__main__":
    app.run()

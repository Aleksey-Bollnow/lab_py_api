import cherrypy
import myprocessor

p = myprocessor.MyProcessor()

def test_local(x):
	return x + 2

class MyWebService(object):
    """
    make run-first
    make run
    вызывать по адресу http://localhost:8081/process
    или http://localhost:8081/process?dd=222 для GET, DELETE
    можно добавить для POST и PUT доп/данные в теле запроса {"some_params":[123,456]}
    make stop
    make clear
    """
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self, **params):
        rest_method = cherrypy.request.method
        data_in = {}
        data_out_tmp = {}
        data_out = {}

        if (rest_method == 'POST'):
            data_in = cherrypy.request.json
            data_out, data_out_tmp = p.myFunction(data_in)

        if (rest_method == 'GET'):
            data_in = params
            data_out, data_out_tmp = p.myFunction(data_in)

        if (rest_method == 'PUT'):
            data_in = cherrypy.request.json

        if (rest_method == 'DELETE'):
            data_in = params

        output = {"test_local":test_local(5), "handle_method":rest_method, "data_in":data_in, "data_out":data_out, "data_out_tmp":data_out_tmp }
        return output

if __name__ == '__main__':
    cherrypy.quickstart(MyWebService(), '/', {'global': {'server.socket_host':'0.0.0.0','server.socket_port': 8081}})

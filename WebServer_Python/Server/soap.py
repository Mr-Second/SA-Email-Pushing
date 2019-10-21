from spyne import Application
from spyne import rpc
from spyne import ServiceBase
from spyne import String, Array
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import re
from Server.Mail import MySendMail
import time


class SoapService(ServiceBase):

    @rpc(String, String, _returns=String)
    def sendEmali(self, _url, _payload):
        flag = MySendMail(_url, str(time.strftime('%Y-%m-%d %H:%M:%S')), _payload)
        if flag:
            return "Y"
        return "N"

    @rpc(Array(String),  String, _returns=String)
    def sendEmaliBatch(self, _urls, _payload):
        flag = True
        for _url in _urls:
            flag = MySendMail(_url, str(time.strftime('%Y-%m-%d %H:%M:%S')), _payload) and flag
        if flag:
            return "Y"
        return "N"

    @rpc(String, _returns=String)
    def validateEmailAddress(self, _url):
        p = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if p.match(_url):
            return "Y"
        else:
            return "N"


soap_app = Application([SoapService], 'spyne.examples.mail.soap',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

wsgi_app = WsgiApplication(soap_app)

if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    # configure the python logger to show debugging output
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_app)
    server.serve_forever()

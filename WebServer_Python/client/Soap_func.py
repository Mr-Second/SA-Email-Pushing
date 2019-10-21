from suds.client import Client

# 要访问的Webservice地址
url = "http://47.94.134.159:8000/?wsdl"


def sendEmail(_url: str, _payload: str):
    client = Client(url)
    res = (client.service.sendEmali(_url, _payload) == "Y")
    return res


def sendEmaliBatch(_url: list, _payload: str):
    client = Client(url)
    curl = dict({"string": _url})
    res = (client.service.sendEmaliBatch(curl, _payload) == "Y")
    return res


def validateEmailAddress(_url: str):
    client = Client(url)
    res = (client.service.validateEmailAddress(_url) == "Y")
    return res


if __name__ == '__main__':
    print(validateEmailAddress("906747215@qq.com"))

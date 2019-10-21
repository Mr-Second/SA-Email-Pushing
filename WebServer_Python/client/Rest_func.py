import requests

URL = "http://47.94.134.159:8080/"


def _sendEmail(_url: str, _payload: str):
    parameter = {"_url": _url, "_payload": _payload}
    response = requests.post(URL+"sendEmail", json=parameter)
    return response.text == "Y"


def _sendEmaliBatch(_url: list, _payload):
    parameter = {"_url": _url, "_payload": _payload}
    response = requests.post(URL+"sendEmailBatch", json=parameter)
    return response.text == "Y"
    pass


def _validateEmailAddress(_url: str):
    parameter = {"_url": _url}
    response = requests.post(URL+"validateEmailAddress", json=parameter)
    return response.text == "Y"

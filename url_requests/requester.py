import requests as rq
from requests.exceptions import HTTPError
from url_request import *


class Requester(object):
    # Singleton
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Requester, cls).__new__(cls)
        return cls.instance

    def make_request(self, req, **kwargs):
        try:
            resp = rq.get(req.url, kwargs)
            resp.raise_for_status()
        except HTTPError as err:
            pass
        except Exception as err:
            pass
        else:
            return req.handle_data(resp, self)
        req.error()

    def _make_stream_request(self, req):
        return self.make_request(req, stream=True)

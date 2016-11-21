import requests

from .exceptions import CoherenceTypeNotAvailable, EndpointDown, WrongContentType

class Palmetto(object):
    all_coherence_types = [
            "ca",
            "cp",
            "cv",
            "npmi",
            "uci",
            "umass"
        ]

    def __init__(self,
        palmetto_uri="http://palmetto.aksw.org/palmetto-webapp/service/"):
        self.palmetto_uri = palmetto_uri

    def _request_by_service(self, words, service_type, content_type="text"):
        request_uri = self.palmetto_uri + service_type

        payload = {}
        payload["words"] = " ".join(words)
        r = requests.post(request_uri, data=payload)
        if(not r.ok):
            raise EndpointDown(request_uri)

        if content_type == "text":
            return r.text
        elif content_type == "bytes":
            return r.content
        else:
            raise WrongContentType(content_type)

    def _get_df(self, words):
        df = self._request_by_service(words, service_type="df", content_type="bytes")
        return df

    def _get_coherence(self, words, coherence_type):
        if coherence_type not in self.all_coherence_types:
            raise CoherenceTypeNotAvailable(coherence_type)

        coherence = self._request_by_service(words, coherence_type)

        return float(coherence)

    def get_coherence(self, words, coherence_type="cv"):
        """
            Return a coherence of a list of words.

            Default coherence type: cv -- the best performing coherence
            Input: a list of words, i.e. ['pen', 'pineapple', 'apple']
            Output: a float number less than 1, i.e. 0.53493
        """
        return self._get_coherence(words, coherence_type)

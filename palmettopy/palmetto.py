import requests

from .exceptions import CoherenceTypeNotAvailable, EndpointDown

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
        coherence_uri="http://palmetto.aksw.org/palmetto-webapp/service/"):
        self.coherence_uri = coherence_uri

    def _get_coherence(self, words, coherence_type):
        if coherence_type not in self.all_coherence_types:
            raise CoherenceTypeNotAvailable(coherence_type)

        coherence_uri = self.coherence_uri + coherence_type

        payload = {}
        payload["words"] = " ".join(words)
        r = requests.post(coherence_uri, data=payload)
        if(not r.ok):
            raise EndpointDown(coherence_uri)
        coherence = float(r.text)

        return coherence

    def get_coherence(self, words, coherence_type="cv"):
        """
            Return a coherence of a list of words.

            Default coherence type: cv -- the best performing coherence
            Input: a list of words, i.e. ['pen', 'pineapple', 'apple']
            Output: a float number less than 1, i.e. 0.53493
        """
        return self._get_coherence(words, coherence_type)

import requests
import socket
from io import BytesIO

from .fastcoherence import calculate_coherence_fast
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
        try:
            r = requests.post(request_uri, data=payload, timeout=5)
        except BaseException:
            raise EndpointDown(request_uri)

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

    def _parse_df_stream_to_doc_ids(self, words, df):
        df_stream = BytesIO(df)
        doc_id_sets = []
        _words = list(reversed(words[:]))
        while True:
            position_before_scan = df_stream.tell()
            doc_ids = self._get_next_set_of_documents(df_stream)
            if doc_ids and _words:
                word = _words.pop()
                doc_id_sets.append((word, set(doc_ids)))
            elif _words:
                word = _words.pop()
                doc_id_sets.append((word, set([])))
            position_after_scan = df_stream.tell()
            if position_before_scan == position_after_scan:
                break
        return doc_id_sets

    def get_df_for_words(self, words):
        """
        Return DF for each of the words.

        Return data structure as follows:
        [(word_a, set()), (word_b, set()), ...],
        where set() is a set of all document ids containing word
        """
        df_stream = self._get_df(words)
        return self._parse_df_stream_to_doc_ids(words, df_stream)

    def _get_next_set_of_documents(self, byte_buffer):
        doc_ids = []
        length = self.convert_4_bytes_to_int(byte_buffer.read(4))
        for i in range(0, length):
            doc_id = self.convert_4_bytes_to_int(byte_buffer.read(4))
            doc_ids.append(doc_id)

        return doc_ids

    def convert_4_bytes_to_int(self, _bytes):
        return int.from_bytes(_bytes, byteorder="big")

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

    def get_coherence_fast(self, words):
        """
            Retrieve coherence based on document frequencies.

            Not normalized, i.e. can be any number > 0.
        """
        doc_id_sets = self.get_df_for_words(words)
        return calculate_coherence_fast(words, doc_id_sets, corpus_size=4264684)

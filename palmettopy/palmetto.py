import requests
from io import BytesIO

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

    def _parse_df_stream_to_doc_ids(self, df):
        df_stream = BytesIO(df)
        doc_id_sets = []
        while True:
            position_before_scan = df_stream.tell()
            doc_ids = self._get_next_set_of_documents(df_stream)
            if doc_ids:
                doc_id_sets.append(set(doc_ids))
            position_after_scan = df_stream.tell()
            if position_before_scan == position_after_scan:
                break
        return doc_id_sets

    def _get_next_set_of_documents(self, byte_buffer):
        doc_ids = []
        length = self.convert_4_bytes_to_int(byte_buffer.read(4))
        for i in range(0, length):
            doc_id = self.convert_4_bytes_to_int(byte_buffer.read(4))
            doc_ids.append(doc_id)

        return doc_ids


    def convert_4_bytes_to_int(self, _bytes):
        return int.from_bytes(_bytes, byteorder="big")

    def _calculate_intersection_for_doc_ids(self, doc_id_sets):
        _fix_doc_id_set = doc_id_sets[0]
        for i in range(1, len(doc_id_sets)):
            _fix_doc_id_set.intersection_update(doc_id_sets[i])
        return len(_fix_doc_id_set)

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
        df_bytes = self._get_df(words)
        doc_id_sets = self._parse_df_stream_to_doc_ids(df_bytes)
        return self._calculate_intersection_for_doc_ids(doc_id_sets)

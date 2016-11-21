"""Custom palmettopy exceptions."""

class CoherenceTypeNotAvailable(Exception):
    """Raised when coherence is not available in Palmetto."""

    def __init__(self, coherence):
        self.coherence = coherence


class EndpointDown(Exception):
    """Raised when endpoint is not reachable."""

    def __init__(self, endpoint):
        self.endpoint = endpoint


class WrongContentType(Exception):
    """Raised when content type is not available."""

    def __init__(self, content_type):
        self.content_type = content_type

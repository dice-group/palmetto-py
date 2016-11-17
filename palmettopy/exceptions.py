"""Custom palmettopy exceptions."""

class CoherenceTypeNotAvailable(Exception):
    """Raised when coherence is not available in Palmetto."""

    def __init__(self, coherence):
        self.coherence = coherence


class EndpointDown(Exception):
    """Raised when endpoint is not reachable."""

    def __init__(self, endpoint):
        self.endpoint = endpoint

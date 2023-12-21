class RateLimitException(Exception):
    def __init__(self, message="API rate limit exceeded"):
        self.message = message
        super().__init__(self.message)

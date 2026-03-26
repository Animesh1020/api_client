class APIError(Exception):
    #Base class for API errors
    pass

class NotFoundError(APIError):
    #Raised when resource is not found
    pass

class UnauthorizedError(APIError):
    #Raised when authentication fails
    pass

class BadRequestError(APIError):
    #Raised for invalid requests
    pass


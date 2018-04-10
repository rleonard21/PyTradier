class TradierException(Exception):
    # Base class for all exceptions within this library
    pass

class APIException(TradierException):
    def __init__(self, error_type, error_message):


        error_str = '{}: \'{}\''.format(error_type, error_message)

        super(APIException, self).__init__(error_str)  # Display the error message through the Exception superclass

        #self.error_type = error_type
        #self.error_message = error_message

        #print self.error_type
        #print self.error_message

class ClientException(TradierException):

    def __init__(self, error_message):
        super(ClientException, self).__init__(error_message)

        self.message = error_message



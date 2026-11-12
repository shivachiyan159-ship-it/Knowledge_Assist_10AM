import sys
import traceback


class CustomException(Exception):
    # attributes
    # methods
    # constructir
    def __init__(self, error_message, error_detail=None):
        # normalize message
        normal_message = str(error_message)

        exc_type = exc_value = exc_tb = None

        # checking exception types
        if error_detail is None:
            exc_type, exc_value, exc_tb = sys.exc_info()
        else:
            if hasattr(error_detail, "exc_info"):  # CustomException("division failesd",sys)
                exc_type, exc_value, exc_tb = error_detail.exc_info()
            # CustomException("division failesd",e)
            elif isinstance(error_detail, BaseException):
                exc_type, exc_value, exc_tb = type(
                    error_detail), error_detail, error_detail.__traceback__
            else:
                exc_type, exc_value, exc_tb = sys.exc_info()

        # walk through last trace back
        last_tb = exc_tb  # [validate(),authenticate(),bunesslogic()]
        while last_tb and last_tb.tb_next:
            last_tb = last_tb.tb_next  # last_tb=bunesslogic()

        # setting all properties from lasttarace back
        self.file_name = last_tb.tb_frame.f_code.co_filename
        self.line_no = last_tb.tb_lineno
        self.error_message = normal_message

        if exc_type and exc_tb:
            self.traceback_str = " ".join(
                traceback.format_exception(*sys.exc_info()))
        else:
            self.traceback_str = ""

        super().__init__(self.__str__())

    def __str__(self):
        return f"""
            Error in {self.file_name} at line num {self.line_no}
            Messgae: {self.error_message}
            traceback: {self.traceback_str}
        """


# CustomException("division failesd")
# CustomException("division failesd", sys)
# CustomException("division failesd", e)

# login button click


def login():
    # validate()
    # authenticate() (checking in db)
    # bunesslogic() error
    # homepage()

    # tarce back contains
    # validate()
    # authenticate() (checking in db)
    # bunesslogic() error
    pass

class PyramisException(Exception):
    """
    Base Exception Class to detect compile-time errors.
    """

    pass


class PyramisNameError(PyramisException):
    pass


class UDFNameError(PyramisNameError):
    pass


class MACRONameError(PyramisNameError):
    pass


class PyramisTypeError(PyramisException):
    pass


class PyramisSyntaxError(PyramisException):
    pass


class PyramisInstantiationError(PyramisException):
    pass


class PyramisOutOfScopeError(PyramisException):
    pass


class PyramisWildCardNameError(PyramisException):
    pass


class PyramisIllegalShadowError(PyramisException):
    pass


class PyramisSymbolOutOfScopeError(PyramisException):
    pass


class PyramisAttributeError(PyramisException):
    pass


class PyramisIncompatibleCallSignatureError(PyramisException):
    pass


class CompilerScopeNameError(PyramisException):
    pass


class CompilerTypeInferenceError(PyramisException):
    pass


class PyramisEventNotCalledError(PyramisException):
    pass


class PyramisCallOrderError(PyramisException):
    pass


if __name__ == "__main__":
    raise PyramisEventNotCalledError("NGSetupRequest, line 2")

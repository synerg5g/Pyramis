#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import inspect


class PyramisException(Exception):
    """Base exception for all virtual OS related errors.

    This class closely resembles OSError with the exception of different
    error codes and lack of the `winerror` attribute. Call signature:

    PyramisException([arg])
    PyramisException(errno, strerror[, filename[, filename2]])
    """

    __slots__ = (
        "_characters_written",
        "errno",
        "filename",
        "filename2",
        "strerror",
        "_filename",
        "_lineno",
    )

    __errnomap = None

    def __new__(cls, *args):
        """Return a new instance of PyramisException or one of its subclasses.

        The subclass is chosen based on the value of the first argument,
        as long as a second argument is present.
        """
        if cls is PyramisException and 2 <= len(args) <= 4:
            if cls.__errnomap is None:
                cls.__errnomap = {
                    1: PyramisCompilerException
                    # FIXME: Extend as needed
                    # Python's OSError has a bunch of subclasses,
                    # some of them covering multiple error numbers.
                }
            newcls = cls.__errnomap.get(args[0])
            if newcls is not None:
                return newcls(*args)
        self = Exception.__new__(cls, *args)
        for attr in PyramisException.__slots__:
            setattr(self, attr, None)
        return self

    def __init__(self, *args):
        """Initialize VirtualOSError with the given values."""
        a = len(args)
        if 2 <= a <= 4:
            self.errno = args[0]
            self.strerror = args[1]
            if a > 2:
                self.args = args[:2]
                self.filename = args[2]
                if a > 3:
                    self.filename2 = args[3]
                else:
                    # Set default value for filename
                    self.filename = inspect.getsourcefile(self.__class__)

                    # Infer lineno from the traceback
                    frame = inspect.currentframe().f_back
                    self._lineno = frame.f_lineno
            else:
                # Set default values for filename and _lineno
                self.filename = inspect.getsourcefile(self.__class__)

                # Infer lineno from the traceback
                frame = inspect.currentframe().f_back
                self._lineno = frame.f_lineno

    def __delattr__(self, attr):
        """Delete the attribute if it’s not a special one, else set it to None."""
        if attr in PyramisException.__slots__:
            setattr(self, attr, None)
        else:
            Exception.__delattr__(self, attr)

    def __str__(self):
        """Return string representation."""
        if self.errno is not None and self.strerror is not None:
            if self.filename is None:
                return "[Errno {!s}] {!s} (File: {}, Line: {})".format(
                    self.errno, self.strerror, self._filename, self._lineno
                )
            if self.filename2 is None:
                return "[Errno {!s}] {!s}: {!r} (File: {}, Line: {})".format(
                    self.errno,
                    self.strerror,
                    self.filename,
                    self._filename,
                    self._lineno,
                )
            return "[Errno {!s}] {!s}: {!r} -> {!r} (File: {}, Line: {})".format(
                self.errno,
                self.strerror,
                self.filename,
                self.filename2,
                self._filename,
                self._lineno,
            )
        return Exception.__str__(self)

    @property
    def characters_written(self) -> int:
        """Number of characters written before the error occurred."""
        if self._characters_written is None:
            raise AttributeError("characters_written")
        return self._characters_written

    @characters_written.setter
    def characters_written(self, value: int) -> None:
        """Number of characters written before the error occurred."""
        if type(value) is int:
            self._characters_written = value
            return
        try:
            value = value.__index__()
        except Exception:
            # OSError does it more or less the same way
            pass
        else:
            if type(value) is int:
                self._characters_written = value
                return
        raise TypeError(
            "'{}' object cannot be interpreted as an integer".format(
                type(value).__name__
            )
        )

    @characters_written.deleter
    def characters_written(self) -> None:
        """Number of characters written before the error occurred."""
        self._characters_written = None


class PyramisCompilerException(PyramisException):
    """Exception raised under special circumstances.

    See help(PyramisException) for accurate signature.
    """

    pass


if __name__ == "__main__":
    try:
        raise PyramisException(1, 3, "")
    except PyramisException as e:
        # e._filename will be __file__, and e._lineno will be the line number where the exception is raised
        raise

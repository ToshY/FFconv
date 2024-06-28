class MKVmergeError(Exception):
    """
    Custom exception class for MKVmerge-related errors.

    This exception is raised when MKVmerge fails with a non-zero exit code.

    Attributes:
        exit_code (int): The exit code of the failed MKVmerge process.
        message (str): The error message associated with the failure.

    Args:
        message (str): The error message associated with the failure.
        exit_code (int): The exit code of the failed MKVmerge process.
    """

    ERROR_MESSAGE = "MKVmerge failed with exit code `{exit_code}`: {message}."

    def __init__(self, message, exit_code):
        self.exit_code = exit_code
        self.message = self.ERROR_MESSAGE.format(message=message, exit_code=exit_code)
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ProcessError(Exception):
    """
    Custom exception class for process-related errors.

    This exception is raised when a process fails with a non-zero exit code.

    Attributes:
        exit_code (int): The exit code of the failed process.
        message (str): The error message associated with the failure.

    Args:
        message (str): The error message associated with the failure.
        exit_code (int): The exit code of the failed process.
    """

    ERROR_MESSAGE = "Process failed with exit code `{exit_code}`: {message}."

    def __init__(self, message, exit_code):
        self.exit_code = exit_code
        self.message = self.ERROR_MESSAGE.format(message=message, exit_code=exit_code)
        super().__init__(self.message)

    def __str__(self):
        return self.message


class FFmpegError(Exception):
    """
    Custom exception class for FFmpeg-related errors.

    This exception is raised when FFmpeg fails with a non-zero exit code.

    Attributes:
        exit_code (int): The exit code of the failed FFmpeg process.
        message (str): The error message associated with the failure.

    Args:
        message (str): The error message associated with the failure.
        exit_code (int): The exit code of the failed FFmpeg process.
    """

    ERROR_MESSAGE = "FFmpeg failed with exit code `{exit_code}`: {message}."

    def __init__(self, message, exit_code):
        self.exit_code = exit_code
        self.message = self.ERROR_MESSAGE.format(message=message, exit_code=exit_code)
        super().__init__(self.message)

    def __str__(self):
        return self.message


class StreamOrderError(Exception):
    """
    Custom exception class for source stream order related errors.

    This exception is raised when stream order does not follow convention video - audio - subtitles.
    """

    ERROR_MESSAGE = (
        "Stream order does not follow convention of video - audio - subtitles. Resort the streams before "
        "continuing."
    )

    def __init__(self):
        self.message = self.ERROR_MESSAGE
        super().__init__(self.message)

    def __str__(self):
        return self.message


class StreamTypeMissingError(Exception):
    """
    Custom exception class for stream type related errors.

    This exception is raised when at least one stream of type video, audio or subtitle is missing.

    Attributes:
        message (str): The error message associated with the failure.

    Args:
        message (str): The error message associated with the failure.
    """

    ERROR_MESSAGE = (
        "File does not contain stream type `{stream_type}`. File needs at least 1 video (`v`), 1 audio (`a`) and 1 "
        "subtitle (`s`) stream."
    )

    def __init__(self, message):
        self.message = self.ERROR_MESSAGE.format(stream_type=message)
        super().__init__(self.message)

    def __str__(self):
        return self.message
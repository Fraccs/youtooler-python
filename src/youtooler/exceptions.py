class DurationUnestablishedException(Exception):
    '''Raised if the duration of a video couldn't be established'''
    pass

class LevelNotInRange(Exception):
    '''Raised if level is not in the range 1..10'''
    pass

class LogMessageException(Exception):
    '''Raised if a log/warning/error message that doesn't exist is requested'''
    pass

class InvalidUrl(Exception):
    '''Raised if the video's url is not valid'''
    pass

class TorDataDirectoryException(Exception):
    '''Raised if an error with the TOR data directory occours (usually OSError)'''
    pass

class TorHashingException(Exception):
    '''Raised if TOR fails to hash a password'''
    pass

class TorStartFailedException(Exception):
    '''Raised if TOR fails to startup'''
    pass

class UnsecureLength(Exception):
    '''Raised if an unsecure length is passed when generating a secure password'''
    pass

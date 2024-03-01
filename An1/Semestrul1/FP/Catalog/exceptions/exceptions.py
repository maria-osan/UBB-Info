class ShowManagerException(Exception):
    pass


class ValidationException(ShowManagerException):
    def __init__(self, msgs):
        """
        :param msgs: lista de mesaje de eroare
        :type msgs: msgs
        """
        self.__err_msgs = msgs

    def getMessages(self):
        return self.__err_msgs

    def __str__(self):
        return 'Validation Exception: ' + str(self.__err_msgs)


class RepositoryException(ShowManagerException):
    def __init__(self, msg):
        self.__msg = msg

    def getMessage(self):
        return self.__msg

    def __str__(self):
        return 'Repository Exception: ' + str(self.__msg)


class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "ID duplicat.")


class StudentNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Studentul nu a fost gasit.")


class DisciplinaNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Disciplina nu a fost gasita.")


class NotaNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Nota nu a fost gasita.")


class NotEnoughRatingsException(ShowManagerException):
    def __init__(self):
        pass


class CorruptedFileException(ShowManagerException):
    def __init__(self):
        pass

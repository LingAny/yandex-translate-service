from abc import ABCMeta
from abc import abstractmethod


class AsyncDataContextFactory(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def create(self):
        """
        :rtype: DataContext
        """
        return NotImplemented

from abc import ABC, abstractmethod

class Machine:
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Photocopier(Printer, Scanner):
    def print(self, document):
        print("printing...")

    def scan(self, document):
        print("scanning...")
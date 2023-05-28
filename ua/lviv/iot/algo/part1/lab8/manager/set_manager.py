from .printer_manager import PrinterManager
from models.printer import Printer


class SetManager:
    """
    set manager of printers
    """
    def __init__(self, printers: list[Printer] = None):
        """
        :param: printers - list of Printers
        """
        self.printer_manager = PrinterManager(printers)

    def __iter__(self):
        """
        make iteration of printers set of prefered type of paper
        """
        self.index = 0
        self.current_paper_type_index = 0
        return self

    def __next__(self):
        """
        next iteration of prefered type of paper
        """
        if self.index < len(self.printer_manager.printers):
            printer = self.printer_manager.printers[self.index]
            paper_type_set = printer.prefered_type_of_paper_set

            if self.current_paper_type_index < len(paper_type_set):
                paper_type = list(paper_type_set)[
                    self.current_paper_type_index]
                self.current_paper_type_index += 1
                return paper_type
            else:
                self.index += 1
                self.current_paper_type_index = 0
                return self.__next__()
        else:
            raise StopIteration

    def __len__(self):
        """
        length of all printers' prefered type of paper
        """
        count = 0
        for printer in self.printer_manager.printers:
            for _ in printer.prefered_type_of_paper_set:
                count += 1
        return count

    def __getitem__(self, index):
        """
        make new list of printers' prefered type of paper and return one type in "index"

        :param: index - index of printers' prefered type of paper
        """
        paper_types = []
        for printer in self.printer_manager.printers:
            paper_types.extend(printer.prefered_type_of_paper_set)

        if index >= len(paper_types):
            raise IndexError("Index out of range")

        return paper_types[index]

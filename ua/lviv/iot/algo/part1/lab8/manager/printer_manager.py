import copy
from decorators.using_time_file import using_time_file
from decorators.result_of_method_file import result_of_method_file
from models.printer import Printer


class PrinterManager:
    """
    Manager of Printers
    """

    def __init__(self, printers: list[Printer] = None):
        """
            :param: printers - list of Printers
        """
        self.printers = list(printers)

    def __len__(self):
        """
        returns length of printers list
        """
        return len(self.printers)

    def __getitem__(self, index):
        """
        :param: index - The index of the item
        """
        return self.printers[index]

    def __iter__(self):
        """
        returns iterator of printers in manager
        """
        return iter(self.printers)

    @using_time_file
    def load_all_paper(self, count):
        """
        loads paper to all printers

        :param: count - amount of paper to load
        """
        [x.load_paper(count) for x in self.printers]
        return self.printers

    def print_with_all_printers(self, pages):
        """
        Print something from all printers

        :param: pages - amount of paper to print
        """
        [x.print(pages) for x in self.printers]
        return self.printers

    @result_of_method_file
    def numerated_list(self):
        """
        returns list of printers with an ordinal number
        """
        temp_list = []
        for index, printer in enumerate(self.printers, start=1):
            temp_list.append(f"{index}, {printer}")
        return temp_list

    @result_of_method_file
    def load_paper_with_comparing(self, count):
        """
        loads paper to printers and returns comparing of old printer and new printer

        :param: count - amount of paper to load
        """
        old_printer = copy.deepcopy(self.printers)
        return [f"{obj} : {res}" for obj, res in zip(old_printer, self.load_all_paper(count))]

    @using_time_file
    def check_printers_tray_capacity_more_than(self, number):
        """
        checking if there any or all printers in the list have paper tray capacity more than "number"

        :param: number - mininum number of tray capacity
        """
        result = {"all - ": all(printer.paper_tray_capacity > number for printer in self.printers),
                  "any - ": any(printer.paper_tray_capacity > number for printer in self.printers)}
        return result

    def add_printer(self, printer: Printer = None):
        """
        adding Printer to a list
        """
        self.printers.append(printer)

    def see_all_printers(self):
        """
        prints all printers in a list
        """
        for printer in self.printers:
            print(printer)

    def find_all_with_paper_count_more_than(self, number):
        """
        returns all printers with paper count more than "number"
        """
        return filter(lambda printer: printer.remaining_pages_count() > number, self.printers)

    def find_all_with_paper_tray_capacity_more_than(self, number):
        """
        returns all printers with paper tray capacity more than "number" 
        """
        return filter(lambda printer: printer.paper_tray_capacity > number, self.printers)

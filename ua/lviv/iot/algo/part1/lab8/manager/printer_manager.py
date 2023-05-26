from models.printer import Printer


class PrinterManager:
    """
    Manager of Printers
    """

    def __init__(self, printers: list[Printer] = None):
        """
        field:
            :param: printers - list of Printers
        """
        self.printers = list(printers)

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

from exceptions.paper_error import PaperError
from exceptions.overload_paper_error import OverloadError
from exceptions.logger import loggering
from .printer import Printer


class LaserPrinter(Printer):
    """
    class LaserPrinter
    """

    def __init__(self, model="unmodeled", type_of="Laser", is_color=True, is_duplex=True,
                 paper_tray_capacity=300, paper_count=0, capacity_of_toner=10, printed_pages=0):
        """
        field:
           :param: model - model of printer
           :param: type_of - type of printer(Ink, Laser...)
           :param: is_color - black/white or colorful
           :param: is_duplex - if printer duplex or not
           :param: paper_tray_capacity - max number of pages which can be put in printer
           :param: paper_count - number of pages loaded now
           :param: prefered_type_of_paper_set - set of prefered type of paper
           :param: capacity_of_toner - remaining capacity of toner
           :param: printed_pages - how much paper printer already spent
        """
        super().__init__(model=model, type_of=type_of, is_color=is_color, is_duplex=is_duplex,
                         paper_tray_capacity=paper_tray_capacity, paper_count=paper_count, 
                         prefered_type_of_paper_set={"Laser paper", "Plain Office paper"})
        self.capacity_of_toner = capacity_of_toner
        self.printed_pages = printed_pages

    def __str__(self):
        return super().__str__() + f", capacity_of_toner={self.capacity_of_toner}, printed_pages={self.printed_pages})"

    @loggering(PaperError, "console")
    def print(self, pages):
        """
        prints the specified number of pages
        """
        if self.paper_count >= pages:
            self.paper_count -= pages
        else:
            raise PaperError(pages, self.paper_count, "laz")

    @loggering(OverloadError, "console")
    def load_paper(self, count):
        """
        loads the specified number of paper into tray
        """
        if (self.paper_count + count) <= self.paper_tray_capacity:
            self.paper_count += count
        else:
            raise OverloadError(count, self.paper_tray_capacity - self.paper_count, "laz")

    def remaining_pages_count(self):
        """
        calculate remaining paper to print
        """
        return self.paper_count

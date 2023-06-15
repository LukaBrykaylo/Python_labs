from exceptions.paper_error import PaperError
from exceptions.overload_paper_error import OverloadError
from exceptions.logger import loggering
from .printer import Printer


class MatrixPrinter(Printer):
    """
    class MatrixPrinter
    """

    def __init__(self, model="unmodeled", type_of="Matrix", is_color=True, is_duplex=True,
                 paper_tray_capacity=200, paper_count=0, number_of_pins=8, is_speed=False):
        """
        field:
           :param: model - model of printer
           :param: type_of - type of printer(Ink, Laser...)
           :param: is_color - black/white or colorful
           :param: is_duplex - if printer duplex or not
           :param: paper_tray_capacity - max number of pages which can be put in printer
           :param: paper_count - number of pages loaded now
           :param: prefered_type_of_paper_set - set of prefered type of paper
           :param: number_of_pins - number of printer's pins
           :param: is_speed - if printer speed or not
        """
        super().__init__(model=model, type_of=type_of, is_color=is_color, is_duplex=is_duplex,
                         paper_tray_capacity=paper_tray_capacity, paper_count=paper_count,
                         prefered_type_of_paper_set={"Continuous form paper", "Plain Listing paper"})
        self.number_of_pins = number_of_pins
        self.is_speed = is_speed

    def __str__(self):
        return super().__str__() + f", number_of_pins={self.number_of_pins}, is_speed={self.is_speed})"
  
    @loggering(PaperError, "file")
    def print(self, pages):
        """
        prints the specified number of pages
        """
        if self.paper_count >= pages:
            self.paper_count -= pages
        else:
            raise PaperError(pages, self.paper_count, "Mat")

    @loggering(OverloadError, "file")
    def load_paper(self, count):
        """
        loads the specified number of paper into tray
        """
        if (self.paper_count + count) <= self.paper_tray_capacity:
            self.paper_count += count
        else:
            raise OverloadError(count, self.paper_tray_capacity - self.paper_count, "Mat")

    def remaining_pages_count(self):
        """
        calculate remaining paper to print
        """
        return self.paper_count

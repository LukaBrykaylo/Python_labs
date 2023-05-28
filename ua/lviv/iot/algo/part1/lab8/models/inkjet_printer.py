from .printer import Printer


class InkjetPrinter(Printer):
    """
    class InkjetPrinter
    """

    REQUIRED_COLOUR_PER_PAGE = 10

    def __init__(self, model="unmodeled", type_of="Inkjet", is_color=True, is_duplex=True,
                 paper_tray_capacity=300, paper_count=0, is_CMYK=True, level_of_paints=100):
        """
        field:
           :param: model - model of printer
           :param: type_of - type of printer(Ink, Laser...)
           :param: is_color - black/white or colorful
           :param: is_duplex - if printer duplex or not
           :param: paper_tray_capacity - max number of pages which can be put in printer
           :param: paper_count - number of pages loaded now
           :param: prefered_type_of_paper_set - set of prefered type of paper
           :param: is_CMYK - if printer CMYK or not
           :param: level_of_paints - remaining level of paints
        """
        super().__init__(model=model, type_of=type_of, is_color=is_color, is_duplex=is_duplex,
                         paper_tray_capacity=paper_tray_capacity, paper_count=paper_count, 
                         prefered_type_of_paper_set={"Glossy paper", "Semi-gloss paper"})
        self.is_CMYK = is_CMYK
        self.level_of_paints = level_of_paints

    def __str__(self):
        return super().__str__() + f", is_CMYK={self.is_CMYK}, level_of_paints={self.level_of_paints})"

    def print(self, pages):
        """
        prints the specified number of pages
        """
        if (self.paper_count - pages) >= 0:
            self.paper_count -= pages
        else:
            self.paper_count = 0

    def load_paper(self, count):
        """
        loads the specified number of paper into tray
        """
        if (self.paper_count + count) <= self.paper_tray_capacity:
            self.paper_count += count
        else:
            self.paper_count = self.paper_tray_capacity

    def remaining_pages_count(self):
        """
        calculate remaining paper to print
        """
        if self.level_of_paints >= 10:
            return self.level_of_paints / self.REQUIRED_COLOUR_PER_PAGE
        else:
            return 0

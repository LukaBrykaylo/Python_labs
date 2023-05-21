from .printer import Printer


class SublimationPrinter(Printer):
    """
    class SublimationPrinter
    """

    def __init__(self, model="unmodeled", type="Sublimation", is_color=True, is_duplex=True,
                 paper_tray_capacity=200, paper_count=0, temperature=10):
        """
        field:
           model - model of printer
           type - type of printer(Ink, Laser...)
           is_color - black/white or colorful
           is_duplex - if printer duplex or not
           paper_tray_capacity - max number of pages which can be put in printer
           paper_count - number of pages loaded now
           temperature - temperature of printer
        """
        super().__init__(model=model, type=type, is_color=is_color, is_duplex=is_duplex,
                         paper_tray_capacity=paper_tray_capacity, paper_count=paper_count)
        self.temperature = temperature

    def __str__(self):
        return super().__str__() + f", temperature={self.temperature})"

    def print(self, pages):
        """
        prints the specified number of pages
        """
        if (self.paper_count - pages) >= 0:
            self.paper_count -= pages
        else:
            self.paper_count = 0

    def loadPaper(self, count):
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
        return self.paper_count

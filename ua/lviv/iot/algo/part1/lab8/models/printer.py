from abc import ABC, abstractclassmethod


class Printer(ABC):
    """
    Abstract printer class
    """

    @abstractclassmethod
    def __init__(self, model="unmodeled", type="Laser", is_color=True, is_duplex=True, paper_tray_capacity=300, paper_count=0):
        """
        field:
           model - model of printer
           type - type of printer(Ink, Laser...)
           is_color - black/white or colorful
           is_duplex - if printer duplex or not
           paper_tray_capacity - max number of pages which can be put in printer
           paper_count - number of pages loaded now
        """
        self.model = model
        self.type = type
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.paper_tray_capacity = paper_tray_capacity
        self.paper_count = paper_count

    @abstractclassmethod
    def __str__(self):
        return f"Printer (model={self.model}, type={self.type}, is color={self.is_color},\
 is duplex={self.is_duplex}, paper tray capacity={self.paper_tray_capacity}, paper count={self.paper_count}"

    @abstractclassmethod
    def print(self, pages):
        """
        prints the specified number of pages
        """
        if (self.paper_count - pages) >= 0:
            self.paper_count -= pages
        else:
            self.paper_count = 0

    @abstractclassmethod
    def loadPaper(self, count):
        """
        loads the specified number of paper into tray
        """
        if (self.paper_count + count) <= self.paper_tray_capacity:
            self.paper_count += count
        else:
            self.paper_count = self.paper_tray_capacity

    @abstractclassmethod
    def remaining_pages_count(self):
        """
        calculate remaining paper to print
        """
        return self.paper_count

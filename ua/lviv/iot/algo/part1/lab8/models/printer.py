from abc import ABC, abstractmethod


class Printer(ABC):
    """
    Abstract printer class
    """

    def __init__(self, model="unmodeled", type_of="Laser", is_color=True, is_duplex=True, paper_tray_capacity=300, paper_count=0, prefered_type_of_paper_set={}):
        """
        field:
           :param: model - model of printer
           :param: type_of - type of printer(Ink, Laser...)
           :param: is_color - black/white or colorful
           :param: is_duplex - if printer duplex or not
           :param: paper_tray_capacity - max number of pages which can be put in printer
           :param: paper_count - number of pages loaded now
           :param: prefered_type_of_paper_set - set of prefered type of paper
        """
        self.model = model
        self.type_of = type_of
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.paper_tray_capacity = paper_tray_capacity
        self.paper_count = paper_count
        self.prefered_type_of_paper_set = prefered_type_of_paper_set

    @abstractmethod
    def __str__(self):
        return f"Printer (model={self.model}, type={self.type_of}, is color={self.is_color},\
 is duplex={self.is_duplex}, paper tray capacity={self.paper_tray_capacity}, paper count={self.paper_count}"

    @abstractmethod
    def print(self, pages):
        """
        prints the specified number of pages
        """
        pass

    def __iter__(self):
        return iter(self.prefered_type_of_paper_set)

    @abstractmethod
    def load_paper(self, count):
        """
        loads the specified number of paper into tray
        """
        pass

    @abstractmethod
    def remaining_pages_count(self):
        """
        calculate remaining paper to print
        """
        pass

    def get_attributes_in_type(self, data_type):
        """
        return all attributes which same as "data_type"

        :param: data_type - type to compare
        """
        pass

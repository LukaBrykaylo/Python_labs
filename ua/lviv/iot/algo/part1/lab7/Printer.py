class Printer:
    """
    Printer class
    """

    def __init__(self, model="unmodeled", type="Laser", is_color=True, is_duplex=True, paper_tray_capacity=300, paper_count=0):
        """
        field:
           __model - model of printer
           __type - type of printer(Ink, Laser...)
           __is_color - black/white or colorful
           __is_duplex - if printer duplex or not
           __paper_tray_capacity - max number of pages which can be put in printer
           __paper_count - number of pages loaded now
        """
        self.__model = model
        self.__type = type
        self.__is_color = is_color
        self.__is_duplex = is_duplex
        self.__paper_tray_capacity = paper_tray_capacity
        self.__paper_count = paper_count

    def __str__(self):
        return f"Printer (model={self.__model}, type={self.__type}, is color={self.__is_color},\
 is duplex={self.__is_duplex}, paper tray capacity={self.__paper_tray_capacity}, paper count={self.__paper_count})"

    @staticmethod
    def get_instance():
        """
        returning instance of printer
        """
        return Printer()

    @property
    def printer_model(self):
        return self.__model

    @printer_model.setter
    def printer_model(self, new_model):
        self.__model = new_model

    @property
    def printer_type(self):
        return self.__type

    @printer_type.setter
    def printer_type(self, new_type):
        self.__type = new_type

    @property
    def printer_is_color(self):
        return self.__is_color

    @printer_is_color.setter
    def printer_is_color(self, new_is_color):
        self.__is_color = new_is_color

    @property
    def printer_is_duplex(self):
        return self.__is_duplex

    @printer_is_duplex.setter
    def printer_is_duplex(self, new_is_duplex):
        self.__is_duplex = new_is_duplex

    @property
    def printer_paper_tray_capacity(self):
        return self.__paper_tray_capacity

    @printer_paper_tray_capacity.setter
    def printer_paper_tray_capacity(self, new_paper_tray_capacity):
        self.__paper_tray_capacity = new_paper_tray_capacity

    @property
    def printer_paper_count(self):
        return self.__paper_count

    @printer_paper_count.setter
    def printer_paper_count(self, new_paper_count):
        self.__paper_count = new_paper_count

    def print(self, pages):
        """
        prints the specified number of pages
        """
        if (self.printer_paper_count - pages) >= 0:
            self.__paper_count -= pages
        else:
            self.__paper_count = 0

    def loadPaper(self, count):
        """
        loads the specified number of paper into tray
        """
        if (self.__paper_count + count) <= self.__paper_tray_capacity:
            self.__paper_count += count
        else:
            self.__paper_count = self.__paper_tray_capacity

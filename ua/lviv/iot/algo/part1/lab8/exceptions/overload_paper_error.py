class OverloadError(Exception):
    def __init__(self, paper_to_put, available_capacity, clas):
        self.paper_to_put = paper_to_put
        self.available_capacity = available_capacity
        self.clas = clas
        super().__init__(self.__str__())

    def __str__(self):
        return f"{self.__class__.__name__}. {self.clas}. So much paper. Paper to put: {self.paper_to_put}, available capacity: {self.available_capacity}"

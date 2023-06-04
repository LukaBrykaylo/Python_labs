class PaperError(Exception):
    def __init__(self, required_paper, available_paper, clas):
        self.required_paper = required_paper
        self.available_paper = available_paper
        self.clas = clas
        super().__init__(self.__str__())

    def __str__(self):
        return f"{self.__class__.__name__}. {self.clas}. Not enough paper. Required pages: {self.required_paper}, available pages: {self.available_paper}"

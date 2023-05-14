from Printer import Printer

if __name__ == '__main__':
    printers = [Printer(), Printer("Modeled", "Inject", True, False, 200, 0),
                 Printer.get_instance(), Printer.get_instance()]

    for printer in printers:
        print(id(printer))

from manager.printer_manager import PrinterManager
from models.inkjet_printer import InkjetPrinter
from models.laser_printer import LaserPrinter
from models.matrix_printer import MatrixPrinter
from models.sublimation_printer import SublimationPrinter

if __name__ == '__main__':
    printers = [InkjetPrinter("Modeled", "Inkject", True, False, 200, 0, True, 2), 
                LaserPrinter("Modeled", "Laser", True, True, 90, 6, 20, 0),
                MatrixPrinter("Modeled", "Matrix", True, False, 200, 0, 8, True),
                SublimationPrinter("Modeled", "Sublimation", True, False, 200, 0, 20)]

    printer_manager = PrinterManager(printers)

    printer_manager.see_all_printers()

    for printer in printer_manager.find_all_with_paper_count_more_than(5):
        print(printer)

    for printer in printer_manager.find_all_with_paper_tray_capacity_more_than(100):
        print(printer)
# encoding: UTF-8

from objectmaphelper import *

cSV_Table_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "CSV Table"}
cSV_Table_New_QToolButton = {"text": "New", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": cSV_Table_MainWindow}
cSV_Table_Column_Names_QInputDialog = {"type": "QInputDialog", "unnamed": 1, "visible": 1, "windowTitle": "CSV Table - Column Names"}
cSV_Table_Column_Names_Enter_a_comma_separated_list_of_column_names_QLabel = {"text": "Enter a comma-separated list of column names", "type": "QLabel", "unnamed": 1, "visible": 1, "window": cSV_Table_Column_Names_QInputDialog}
enter_a_comma_separated_list_of_column_names_QLineEdit = {"buddy": cSV_Table_Column_Names_Enter_a_comma_separated_list_of_column_names_QLabel, "type": "QLineEdit", "unnamed": 1, "visible": 1}
cSV_Table_Column_Names_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": cSV_Table_Column_Names_QInputDialog}
cSV_Table_Unnamed_MainWindow = {"type": "MainWindow", "unnamed": 1, "visible": 1, "windowTitle": "CSV Table - Unnamed"}
cSV_Table_Unnamed_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": cSV_Table_Unnamed_MainWindow, "windowTitle": "File"}
cSV_Table_Unnamed_File_QTableWidget = {"aboveWidget": cSV_Table_Unnamed_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": cSV_Table_Unnamed_MainWindow}
file_0_0_QModelIndex = {"column": 0, "container": cSV_Table_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
file_0_1_QModelIndex = {"column": 1, "container": cSV_Table_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
file_0_2_QModelIndex = {"column": 2, "container": cSV_Table_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
file_0_3_QModelIndex = {"column": 3, "container": cSV_Table_Unnamed_File_QTableWidget, "row": 0, "type": "QModelIndex"}
cSV_Table_File_QToolBar = {"type": "QToolBar", "unnamed": 1, "visible": 1, "window": cSV_Table_MainWindow, "windowTitle": "File"}
cSV_Table_File_QTableWidget = {"aboveWidget": cSV_Table_File_QToolBar, "type": "QTableWidget", "unnamed": 1, "visible": 1, "window": cSV_Table_MainWindow}
file_QExpandingLineEdit = {"container": cSV_Table_Unnamed_File_QTableWidget, "type": "QExpandingLineEdit", "unnamed": 1, "visible": 1}
cSV_Table_Unnamed_New_QToolButton = {"text": "New", "type": "QToolButton", "unnamed": 1, "visible": 1, "window": cSV_Table_Unnamed_MainWindow}
cSV_Table_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "CSV Table"}
file_QHeaderView = {"container": cSV_Table_Unnamed_File_QTableWidget, "orientation": 2, "type": "QHeaderView", "unnamed": 1, "visible": 1}
o1_HeaderViewItem = {"container": file_QHeaderView, "text": 1, "type": "HeaderViewItem", "visible": True}
cSV_Table_Unnamed_File_QMenu = {"aboveWidget": cSV_Table_Unnamed_File_QToolBar, "type": "QMenu", "unnamed": 1, "visible": 1, "window": cSV_Table_Unnamed_MainWindow}
file_1_0_QModelIndex = {"column": 0, "container": cSV_Table_Unnamed_File_QTableWidget, "row": 1, "type": "QModelIndex"}
file_1_1_QModelIndex = {"column": 1, "container": cSV_Table_Unnamed_File_QTableWidget, "row": 1, "type": "QModelIndex"}
file_1_2_QModelIndex = {"column": 2, "container": cSV_Table_Unnamed_File_QTableWidget, "row": 1, "type": "QModelIndex"}
file_1_3_QModelIndex = {"column": 3, "container": cSV_Table_Unnamed_File_QTableWidget, "row": 1, "type": "QModelIndex"}

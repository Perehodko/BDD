# -*- coding: utf-8 -*-

# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed. See the section 'Behaviour Driven Testing' in the 'API
# Reference Manual' chapter of the Squish manual for a comprehensive reference.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("I enter the text")
#   def whenTextEntered(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("I get |integer| different names")
#   def namesReceived(context, numNames):
#      <code here>
#
# Instead of using a string with placeholders, a regular expression can be
# specified. In that case, make sure to set the (optional) 'regexp' argument
# to True.

import names

@Given("the application is running")
def step(context):
    startApplication("csvtable")
    sendEvent("QMoveEvent", waitForObject(names.cSV_Table_MainWindow), 256, 50, 834, 73)

@When("a new table is created")
def step(context):
    clickButton(waitForObject(names.cSV_Table_New_QToolButton))
    sendEvent("QMoveEvent", waitForObject(names.cSV_Table_Column_Names_QInputDialog), 502, 252, 293, 129)
    type(waitForObject(names.enter_a_comma_separated_list_of_column_names_QLineEdit), "column1, column2, columb")
    type(waitForObject(names.enter_a_comma_separated_list_of_column_names_QLineEdit), "<Backspace>")
    type(waitForObject(names.enter_a_comma_separated_list_of_column_names_QLineEdit), "n3, column4")
    clickButton(waitForObject(names.cSV_Table_Column_Names_OK_QPushButton))

@Then("the table should be blank")
def step(context):
    test.compare(waitForObjectExists(names.file_0_0_QModelIndex).text, "")
    test.compare(waitForObjectExists(names.file_0_1_QModelIndex).text, "")
    test.compare(waitForObjectExists(names.file_0_2_QModelIndex).text, "")
    test.compare(waitForObjectExists(names.file_0_3_QModelIndex).text, "")


@Then("table should have zero entries")
def step(context):
    test.compare(waitForObjectExists(names.cSV_Table_File_QTableWidget).rowCount, 0)


@Given("I create a new table with two entries")
def step(context):
    clickButton(waitForObject(names.cSV_Table_New_QToolButton))
    sendEvent("QMoveEvent", waitForObject(names.cSV_Table_Column_Names_QInputDialog), 502, 252, 284, 129)
    type(waitForObject(names.enter_a_comma_separated_list_of_column_names_QLineEdit), "name, surname, email, phone")
    type(waitForObject(names.enter_a_comma_separated_list_of_column_names_QLineEdit), "<Return>")
    mouseClick(waitForObjectItem(names.cSV_Table_Unnamed_File_QTableWidget, "0/0"), 42, 9, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.cSV_Table_Unnamed_File_QTableWidget), "I")
    type(waitForObject(names.file_QExpandingLineEdit), "Anya")
    type(waitForObject(names.file_QExpandingLineEdit), "<Tab>")
    type(waitForObject(names.file_QExpandingLineEdit), "Kay")
    type(waitForObject(names.file_QExpandingLineEdit), "<Tab>")
    type(waitForObject(names.file_QExpandingLineEdit), "anyakay@g.com")
    type(waitForObject(names.file_QExpandingLineEdit), "<Tab>")
    type(waitForObject(names.file_QExpandingLineEdit), "1234")
    mouseClick(waitForObjectItem(names.cSV_Table_Unnamed_File_QTableWidget, "0/0"), 48, 8, Qt.NoModifier, Qt.LeftButton)
    openContextMenu(waitForObject(names.file_QHeaderView), 12, 38, Qt.NoModifier)
    activateItem(waitForObjectItem(names.cSV_Table_Unnamed_File_QMenu, "Append Row"))
    doubleClick(waitForObjectItem(names.cSV_Table_Unnamed_File_QTableWidget, "1/0"), 53, 17, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.file_QExpandingLineEdit), "Lily")
    doubleClick(waitForObjectItem(names.cSV_Table_Unnamed_File_QTableWidget, "1/1"), 3, 12, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.file_QExpandingLineEdit), "Gen")
    doubleClick(waitForObjectItem(names.cSV_Table_Unnamed_File_QTableWidget, "1/2"), 70, 10, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.file_QExpandingLineEdit), "lilygen@y.com")
    doubleClick(waitForObjectItem(names.cSV_Table_Unnamed_File_QTableWidget, "1/3"), 59, 17, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.file_QExpandingLineEdit), "1333")
    mouseClick(waitForObject(names.cSV_Table_Unnamed_File_QTableWidget), 701, 93, Qt.NoModifier, Qt.LeftButton)

@Then("'2' entries should bepresent")
def step(context):
    test.compare(waitForObjectExists(names.cSV_Table_Unnamed_File_QTableWidget).rowCount, 2)

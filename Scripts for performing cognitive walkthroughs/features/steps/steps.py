from sys import path
from behave import *
from functions import myFunctions

@given("the user is on the home page of the search engine")
def step_impl(self):
    myFunctions.enterSemanticWeb(self)

@when('the user performs a textual search for "{text}"')
def step_impl(self, text):
    myFunctions.textualSearch(self, text)
    
@then('resources related to "{text}" are displayed in the All view')
def step_impl(self):
    myFunctions.results(self)
    
@when('the user selects one of the available resources')
def step_impl(self):      
    myFunctions.view(self)
    
@then('a full metadata record describing the resource is displayed in a new tab')
def step_impl(self):
    myFunctions.checkmetadatarecord(self)

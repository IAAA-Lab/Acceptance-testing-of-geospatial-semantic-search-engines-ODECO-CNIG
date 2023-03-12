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

@when('the user displays results')
def step_impl(self):
    myFunctions.display(self)
    
@when('the user applies a faceted filter')
def step_impl(self):      
    myFunctions.faceted_filter(self)

@when('the user applies a faceted filter')
def step_impl(self):      
    myFunctions.faceted_filter(self)
    
@when('the user buys a resource available in the main catalogue section')
def step_impl(self):
    myFunctions.buy_catalogue(self)
    
@when('the user locates a resource available in the main catalogue section')
def step_impl(self):
    myFunctions.locate_catalogue(self)

@when('the user visualises a resource available in the main catalogue section')
def step_impl(self):      
    myFunctions.view(self)

@when('the user filters by products')
def step_impl(self):
    myFunctions.filter_products(self)

@when('the user buys a resource available in the product section')
def step_impl(self):
      myFunctions.buy_product(self)

@when('the user visualises a resource available in the product section')
def step_impl(self):      
    myFunctions.view_product(self)

@when('the user filters by downloads')
def step_impl(self):
    myFunctions.filter_downloads(self)
    
@when('the user locates a resource available in the download section')
def step_impl(self):
    myFunctions.locate_download(self)
    
@when('the user searches for a point in the centre of the map')
def step_impl(self):
    myFunctions.pointSearch(self)

@when('the user downloads a resource available in the main catalogue section')
def step_impl(self):
      myFunctions.download_catalogue(self) 

@when('the user searches for a geometry in the centre of the map')
def step_impl(self):
    myFunctions.geometrySearch(self)

@when('the user loads the file  "{file}"')
def step_impl(self, file):
    myFunctions.fileSearch(self, file)

@when('the user types coordinate "{coord1}" "{coord2}"')
def step_impl(self, coord1, coord2):
    myFunctions.coordinateSearch(self, coord1, coord2)
    
@when('the user enters the cadastral reference "{cadastralReference}"')
def step_impl(self, cadastralReference):
    myFunctions.cadastralSearch(self, cadastralReference)

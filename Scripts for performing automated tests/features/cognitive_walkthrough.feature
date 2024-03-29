Feature: cognitive walkthrough

Scenario: Discover cartographic resources of the autonomous community of "Asturias"
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Asturias"         
    Then resources related to "Asturias" are displayed in the "All" view
    When the user selects one of the available resources
    Then a full metadata sheet describing the resource is displayed in a new tab

Scenario: Download a trail file related to the search for the "Way of El Cid"      
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Way of El Cid"         
    Then resources related to "Way of El Cid" are displayed in the "All" view
    When the user selects one of the available resources
    Then a full metadata sheet describing the resource is displayed in a new tab
    When the user downloads one of the files available in the metadata sheet
    Then the file is downloaded locally

Scenario: Buy the current map of the city of "Toledo"     
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Toledo"         
    Then resources related to "Toledo" are displayed in the "All" view
    When the user selects one of the available resources
    Then a full metadata sheet describing the resource is displayed in a new tab
    When the user buys one of the available resources in the metadata sheet
    Then the selected product is added to the shopping cart

Scenario: Discover general cartographic resources of the region of "Murcia"     
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Toledo"         
    Then resources related to "Toledo" are displayed in the "All" view
    When the user selects the filter of "General Cartography"       
    Then only the resources related to "General Cartography" are displayed

Scenario: View the area of the "Sierra Nevada" National Park on the side map
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Sierra Nevada"         
    Then resources related to "Sierra Nevada" are displayed in the "All" view
    When the user locates one of the available resources
    Then the location of the resource is shown in the side map

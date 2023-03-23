Feature: 01. Search results

Scenario: the user is able to search for resources typing text 
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Madrid"
    Then search results are displayed
    
Scenario: the user is able to search for resources selecting a point on the map
    Given The user is on the home page of the search engine
    When the user searches for a point in the centre of the map'
    Then search results are displayed
    
Scenario: the user is able to search for resources drawing a geometry on the map
    Given The user is on the home page of the search engine
    When the user searches for a geometry in the centre of the map    
    Then search results are displayed

Scenario: the user is able to search for resources uploading a geometry file 
    Given The user is on the home page of the search engine
    When the user loads the file "BTT0101_vivar_del_cid-burgos.gpx"
    Then search results are displayed

Scenario: the user is able to search for resources typing a set of coordinates
    Given The user is on the home page of the search engine
    When the user types coordinate "3.40" "40.30"
    Then search results are displayed

Scenario: the user is able search for resources typing a cadastral reference
    Given The user is on the home page of the search engine
    When the user enters the cadastral reference "9977715VK3797F"
    Then search results are displayed

Feature: 02. Display results

Scenario: the user is able to view a list of resources after performing a search
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Madrid"
    Then search results are displayed   

Feature: 03. Filter results

Scenario: the user is able to filter the list of results with the filters provided
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Madrid"
    Then search results are displayed
    When the user selects the filter of "General Cartography"       
    Then only the resources related to "General Cartography" are displayed

Feature: 04. View metadata

Scenario: the user is able to view the metadata record of a specific resource from the results list
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Madrid"
    Then search results are displayed
    When the user selects the filter of "General Cartography"       
    Then only the resources related to "General Cartography" are displayed

Feature: 05. Locate resource

Scenario: the user is able to locate on the map a specific resource from the result list
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Madrid"
    Then search results are displayed
    When the user locates one of the available resources
    Then the location of the resource is shown in the side map

Feature: 06. Download resource

Scenario: the user is able to download a specific resource from the result list
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Madrid"
    Then search results are displayed
    When the user downloads one of the files available
    Then the file is downloaded locally

Feature: 07. Buy resource

Scenario: the user is able to buy a specific resource from the result list on the map
    Given The user is on the home page of the search engine
    When the user performs a textual search for "Madrid"
    Then search results are displayed
    When the user buys a resource available in the main catalogue section
    Then the selected product is added to the shopping cart

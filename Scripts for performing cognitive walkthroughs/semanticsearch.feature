Feature: View resource
Scenario: Discover cartographic resources of the autonomous community of "Asturias"
    Given the user is on the home page of the search engine
    When the user performs a textual search for "Asturias"
    Then resources related to "Asturias" are displayed in the All view
    When the user selects one of the available resources
    Then a full metadata record describing the resource is displayed in a new tab
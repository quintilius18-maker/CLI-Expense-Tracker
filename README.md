--------------------------------------------------------
Data Flow

    User input -> main.py -> Business Logic -> storage.py -> expenses.csv

--------------------------------------------------------

--------------------------------------------------------
Design Principles
    Single Responsibility Principle
    Separation of Concerns
    Modular Design
    Low Coupling
    High Cohesion
--------------------------------------------------------

--------------------------------------------------------
Error Handling Strategy

    Every user input shall be validated
    Invalid numeric input shall prompt the user again
    Missing files shall be created automatically
    Unexpected exceptions shall display an error message without terminating the application
--------------------------------------------------------

--------------------------------------------------------
Coding Standards
    snake_case naming
    descriptive function names
    functions under ~30 lines where practical
    no duplicated code
    use doc strings for public functions
    organize imports consistently
--------------------------------------------------------
    
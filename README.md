````md
# Architecture Overview

## Data Flow

```text
User Input
     │
     ▼
main.py
     │
     ▼
Business Logic
     │
     ▼
storage.py
     │
     ▼
expenses.csv
````

---

## Design Principles

The application follows these software engineering principles:

* **Single Responsibility Principle (SRP)** – Each module and function has one clearly defined purpose.
* **Separation of Concerns** – User interface, business logic, and data storage are kept independent.
* **Modular Design** – The codebase is divided into reusable and maintainable modules.
* **Low Coupling** – Components have minimal dependencies on one another.
* **High Cohesion** – Related functionality is grouped together within the same module.

---

## Error Handling Strategy

The application is designed to handle errors gracefully:

* Validate all user input before processing.
* Prompt the user again when invalid numeric input is entered.
* Automatically create missing data files (such as `expenses.csv`) when needed.
* Catch unexpected exceptions and display a meaningful error message without terminating the application unexpectedly.

---

## Coding Standards

The project adheres to the following coding standards:

* Use **snake_case** for variables and function names.
* Choose **descriptive function and variable names**.
* Keep functions under **approximately 30 lines** where practical.
* Eliminate duplicate code through reusable functions.
* Include **docstrings** for all public functions.
* Organize imports consistently according to Python style guidelines.
* Write readable, maintainable, and well-commented code when necessary.

```
```

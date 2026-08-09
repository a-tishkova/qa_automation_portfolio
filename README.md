# QA Automation Framework (Python)

This repository contains a test automation framework designed to cover both Frontend (UI) and Backend (API) layers of web applications. The project follows industry-standard design patterns to ensure maintainability, scaling, and clean code principles.

## Tech Stack
- **Language:** Python 3.12+
- **UI Automation:** Playwright
- **API Automation:** Requests
- **Test Runner:** PyTest
- **Architecture Pattern:** Page Object Model (POM)

## Project Structure
- `ui_tests/` — UI end-to-end automation scripts for the SauceDemo e-commerce platform.
  - `pages/` — Page Object classes containing locators and page-specific actions.
- `api_tests/` — Backend API validation scripts.
- `pytest.ini` — Test runner configuration and pythonpath definitions.
- `.gitignore` — Metadata and environment cache exclusion rules.

## Automated Scenarios

### UI Tests (SauceDemo)
1. **Successful Authorization:** Verifies that a valid user can successfully log into the platform and reach the inventory page.
2. **Failed Authorization:** Validates form error behavior and error message text when using incorrect credentials.
3. **Shopping Cart Lifecycle:** Logs in, adds an item (backpack) to the cart, navigates to the cart page, and verifies item match.

### API Tests
1. **Service Availability Check:** Sends a secure GET request to a live banking API endpoint and validates response status codes.

## Getting Started

### Prerequisites
Make sure you have Python installed on your local machine.

### Installation
1. Clone the repository:
```bash
git clone https://github.com
```
2. Set up and activate a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```
3. Install required dependencies:
```bash
pip install -r requirements.txt
```
4. Install Playwright browser binaries:
```bash
playwright install
```

### Running Tests
To execute all automated tests across both suites, run:
```bash
pytest
```


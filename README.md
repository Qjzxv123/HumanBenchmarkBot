# Human Benchmark Automation

This project automates various tests on the Human Benchmark website using Selenium WebDriver. Each test is implemented in a separate Python script.

## Prerequisites

- Python 3.x
- Selenium
- ChromeDriver
- Google Chrome

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install Selenium:
    ```sh
    pip install selenium
    ```
3. Download ChromeDriver from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads) and place it in a known directory.(You will probably have to change your path

## Usage

1. Update the `service` argument in each script to point to the location of your ChromeDriver executable.
2. Run login.py
3. Run the desired test script using Python.

### Example

To run the Aim Trainer test:
```sh
python AimTrainer.py

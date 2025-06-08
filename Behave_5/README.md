# Behave Selenium Automation Framework

This repository contains a sample test automation framework using [Behave](https://behave.readthedocs.io/en/latest/), [Selenium WebDriver](https://www.selenium.dev/), and [Allure Reporting](https://allurereport.org/).  
It demonstrates file upload automation and reporting with Allure.

---

## 📦 Project Structure

```
.
├── features/
│   ├── steps/
│   │   └── step_def.py
│   └── file_upload.feature
├── Helper/
│   └── SeleniumHelper.py
├── Logs/
│   └── logging.py
├── behave_test.log
├── README.md
└── ...
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- [Google Chrome](https://www.google.com/chrome/) and [chromedriver](https://chromedriver.chromium.org/downloads)
- [Allure CLI](https://docs.qameta.io/allure/)  
  Install on Windows using [Scoop](https://scoop.sh/):
  ```sh
  irm get.scoop.sh | iex
  scoop install allure
  ```

### Install Python Dependencies

```sh
pip install selenium behave allure-behave
```

---

## 📝 How to Run Tests

### 1. Run Behave Tests and Generate Allure Results

```sh
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```

### 2. Generate Allure HTML Report

```sh
allure generate allure-results -o allure-report --clean
```

### 3. Open Allure Report in Browser

```sh
allure open allure-report
```

---

## 🧑‍💻 Example Usage

- The test navigates to [https://demo.automationtesting.in/FileUpload.html](https://demo.automationtesting.in/FileUpload.html)
- Verifies the page title, URL, header text, and file input element
- Performs a file upload using Selenium

---

## 🗂️ Logging

Logs are saved to `Logs/behave_test.log`.

---

## 🛠️ Tips

- Use raw strings (`r"path"`) or forward slashes (`"C:/path/to/file"`) for Windows file paths in Python.
- Make sure `chromedriver` is installed and available in your PATH.

---

## 📄 License

This project is for demonstration purposes.

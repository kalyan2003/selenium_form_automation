# Selenium Form Automation – Practice Project 

This project demonstrates form automation using **Selenium WebDriver** in Python. The script interacts with various types of form elements like text fields, radio buttons, dropdowns, checkboxes, sliders, color pickers, file uploads, date pickers, and more on a test webpage.

##  Technologies Used

- **Language**: Python  
- **Automation Tool**: Selenium WebDriver  
- **Browser**: Google Chrome  
- **WebDriver Path**: `C:\Drivers\chromedriver-win64\chromedriver.exe`  
- **Target Site**: [Try Testing This – Form Demo](https://trytestingthis.netlify.app/)

##  Features Automated

- Inputting text into text fields (`First Name`, `Last Name`)
- Selecting gender via **radio buttons**
- Selecting an option from **dropdown**
- Clicking on **checkbox**
- Typing into an input with name selector
- Setting **color** using JavaScript
- Typing into **date field**
- Setting **range slider value** using JavaScript
- **Uploading file** from local storage
- Typing into **number field**
- Filling **textarea** with long text
- Submitting the form and handling alert/confirmation

##  Key Concepts Practiced

- `WebDriverWait` with `expected_conditions` for reliable element interaction
- Using various **locators**: `By.ID`, `By.NAME`, `By.TAG_NAME`, `By.CSS_SELECTOR`
- **Dropdown selection** using `Select` class
- Executing **JavaScript** to manipulate fields like color picker and slider
- **Uploading files** using `send_keys()`
- **Alert simulation** after submission
- Clean input handling using `.clear()` before `.send_keys()`



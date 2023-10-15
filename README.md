# Selenium WebDriver With POM Pattern (Python and pytest)

Selenium is a free and open-source automated testing suite for web applications across different browsers and
platforms¹. It's not just a single tool but a set of different software tools each with a different approach to support
test automation¹. It primarily includes four components:

1. Selenium Integrated Development Environment (IDE)
2. Selenium Remote Control (RC)
3. WebDriver
4. Selenium Grid¹

On the other hand, Selenium WebDriver is a component of the Selenium suite that provides a programming interface to
control a web browser through a program¹. It fits in the same role as Selenium-RC did and has incorporated the original
1.x bindings and included the WebDriver API¹. It refers to both the language bindings and the implementations of the
individual browser controlling code¹.

Here are some key differences between Selenium and Selenium WebDriver:

- WebDriver is faster than Selenium RC because of its simpler architecture³.
- WebDriver directly talks to the browser while Selenium RC needs the help of the RC Server in order to do so³.
- WebDriver's API is more concise than Selenium RC's³.
- WebDriver can support Html Unit while Selenium RC cannot³.
- WebDriver overcomes the limitation of Selenium RC's Single Host origin policy¹.

Source: Conversation with Bing, 9/25/2023

1. What Is Selenium And What Is WebDriver? - Stack
   Overflow. https://stackoverflow.com/questions/54459701/what-is-selenium-and-what-is-webdriver.
2. Difference between Selenium RC and WebDriver - Stack
   Overflow. https://stackoverflow.com/questions/11535950/difference-between-selenium-rc-and-webdriver.
3. Difference between Selenium RC and Selenium
   Webdriver. https://www.geeksforgeeks.org/difference-between-selenium-rc-and-selenium-webdriver/.
4. Selenium IDE vs. WebDriver: Key Differences - Blazemeter. https://www.blazemeter.com/blog/selenium-ide-vs-webdriver.

WebDriver itself is a W3C standard, and the Selenium project is one of the most popular implementations. WebDriver can
handle every type of web UI interaction such as clicking, typing and scraping text.

Many people treat “Selenium WebDriver” as almost synonymous with web UI testing.
Selenium releases WebDriver packages in many popular programming languages.

# Development

## Virtual Environment

### Install PIPENV

```shell
pip install pipenv
```

```shell
pipenv install
```

## Necessary Packages

### Selenium (Test Framework)

```shell
pipenv install selenium
```

### Test Runner (Unit Test Framework)

```shell
pipenv install pytest
```

### Manage Logs

```shell
pipenv install python-json-logger
```

### Parallel Testing

```shell
pipenv install pytest-xdist
```

### Create HTML Report

```shell
pipenv install pytest-html
```

### Install All Packages

```shell
pipenv install selenium pytest python-json-logger pytest-html pytest-xdist
```

## Static Testing

### Install & Verify pre-commit

```shell
pipenv install pre-commit
```

```shell
pre-commit --version
```

### Create Sample Config

```shell
pre-commit sample-config
```

### Run pre-commit

```shell
pre-commit run
```

```shell
pre-commit run --all-files
```

### Create pylint File

```shell
pylint --generate-rcfile >.pylintrc

```
### Assertion
```shell
pipenv install assertpy
```

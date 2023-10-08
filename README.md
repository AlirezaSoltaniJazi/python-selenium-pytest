# BazaarPay Web Automation With Playwright

**Playwright** enables reliable end-to-end testing for modern web apps.

* Cross-browser. Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox.
* Cross-platform. Test on Windows, Linux, and macOS, locally or on CI, headless or headed.
* Cross-language. Use the Playwright API in TypeScript, JavaScript, Python, .NET, Java.
* Test Mobile Web. Native mobile emulation of Google Chrome for Android and Mobile Safari. The same rendering engine
  works on your Desktop and in the Cloud.
* Auto-wait. Playwright waits for elements to be actionable prior to performing actions. It also has a rich set of
  introspection events. The combination of the two eliminates the need for artificial timeouts - the primary cause of
  flaky tests.
* Web-first assertions. Playwright assertions are created specifically for the dynamic web. Checks are automatically
  retried until the necessary conditions are met.
* Tracing. Configure test retry strategy, capture execution trace, videos, screenshots to eliminate flakes.
* Browsers run web content belonging to different origins in different processes. Playwright is aligned with the modern
  browsers architecture and runs tests out-of-process. This makes Playwright free of the typical in-process test runner
  limitations. Multiple everything. Test scenarios that span multiple tabs, multiple origins and multiple users. Create
  scenarios with different contexts for different users and run them against your server, all in one test.
* Trusted events. Hover elements, interact with dynamic controls, produce trusted events. Playwright uses real browser
  input pipeline indistinguishable from the real user. Test frames, pierce Shadow DOM. Playwright selectors pierce
  shadow DOM and allow entering frames seamlessly.
* Browser contexts. Playwright creates a browser context for each test. Browser context is equivalent to a brand new
  browser profile. This delivers full test isolation with zero overhead. Creating a new browser context only takes a
  handful of milliseconds.
* Log in once. Save the authentication state of the context and reuse it in all the tests. This bypasses repetitive
  log-in operations in each test, yet delivers full isolation of independent tests.
* Codegen. Generate tests by recording your actions. Save them into any language.
* Playwright inspector. Inspect page, generate selectors, step through the test execution, see click points, explore
  execution logs.
* Trace Viewer. Capture all the information to investigate the test failure. Playwright trace contains test execution
  screencast, live DOM snapshots, action explorer, test source, and many more.

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

Appium
=========

Appium is a test automation tool for use with native and hybrid iOS applications. It uses the webdriver JSON  wire protocol to drive Apple's UIAutomation. Appium is based on [Dan Cuellar's](http://github.com/penguinho) work on iOS Auto.

Appium uses the [Bottle micro web-framework](http://www.bottlepy.org), and has the goal of working with all off the shelf Selenium client libraries.

There are two big benefits to testing with Appium:

1: Appium uses Apple's UIAutomation library under the hood to perform the automation, which means you do not have to recompile your app or modify in any way to be able to test automate it.

2: With Appium, you are able to write your test in your choice of programming language, using the Selenium WebDriver API and language-specific client libraries. If you only used UIAutomation, you would be required to write tests in JavaScript, and only run the tests through the Instruments application. With Appium, you can test your native iOS app with any language, and with your preferred dev tools.

Quick Start
-----------

To get started, clone the repo:<br />
`git clone git://github.com/hugs/appium`

Next, change into the 'appium' directory, and install dependencies:<br />
`pip install -r requirements.txt`

Create a file in your home folder with that will store your username and password. (This is required to beat a security dialog that can appear when launching your ios app).<br />
`touch ~/appium.py`

The file should read something like:

<pre>[appium]
username = your_username
password = your_password</pre>

To launch an interpreter for sending raw UIAutomation javascript commands run:<br />
`python inpreter.py "path_to_your_ios_.app"`

To launch a webdriver-compatible server, run:<br />
`python server.py "path_to_your_ios_.app"`

Contributing
------------


Mailing List
-----------

<a href="https://groups.google.com/d/forum/appium-discuss">Discussion Group</a>

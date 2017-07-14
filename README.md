# BYInputValidationDemo

This is a demo application to explain the importance of server side input validation. The demo is cartering to those interested in application security or general application developer.

For details check my [blog post here](https://medium.com/@BaYinMin/application-security-what-is-server-side-input-validation-why-is-it-needed-anyway-e0613c733548)

# Dependencies

1. Python 2.7.x

2. Python Flask framework for server side hosting

# Usage

1. Make sure dependencies are installed.

2. Download this application from github

3. Open your terminal, go to the application folder and type **python app.py**.

4. Open your browser and type **localhost:50000** to gain access to application


# Function switching

## To enable vulnerable code

1. Locate app.py file and remove comment from line 12-16
2. Comment off line 19-30
3. Restart server

## To enable fixed code

1. Locate app.py file and remove comment from line 19-30
2. Comment off line 12-16
3. Restart server

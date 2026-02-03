## How to debug using VSCode inside running docker container

### Start docker container using docker compose

'''
docker compose up --build
'''

### Quick Start

#### Create the launch.json file in .vscode/ folder
#### Set a breakpoint in controller.py at line where scan_image starts
#### Press F5 and select "Python: Flask App"
#### Open browser to http://localhost:5000/ui
#### Make a request through Swagger UI
#### VSCode will pause at your breakpoint

Now you can inspect variables, step through code, and debug your Flask API easily!
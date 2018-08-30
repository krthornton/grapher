Primary Requirements:
- Python 3.6.5 (goto https://www.python.org/downloads/release/python-365/ and click "Windows x86-64 executable installer")
- During the installation process above, make sure to check the box for "Add Python 3.6 to PATH" otherwise you won't be able to run this program from the command line


How to build executable:

1. Run 'pyinstaller gui.py --hidden-import PyQt5.sip --noconsole'

   This builds a dist\gui folder to distribute


How to prep dev environment:

1. Run 'pip install virtualenv'

2. Run 'virtualenv venv'

3. Run 'venv\Scripts\activate'

4. Run 'pip install -r requirements.txt'

5. Run 'python gui.py'

   This runs the main ui

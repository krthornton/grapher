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

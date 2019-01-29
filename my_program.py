# Import from module (file):
#from my_module import my_func

#my_func()

# Import from package:
# To make a package, add a file __init__.py in the folder, just leave empty.
# Also in subfolders
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()
mysubscript.sub_report()

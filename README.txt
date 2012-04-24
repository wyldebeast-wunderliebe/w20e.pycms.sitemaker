This package allows you to create a skeleton app based on
w20e.pycms. To create the basic application structure, install this
package, and do:

  # paster create -t pycms_project

To also create a buildout environment for actually running it, do:

  # paster create -t pycms_buildout

If you don't want to install this package globally, just download,
unpack if need be, cd into place where setup.py is and use commands
above.


Most likely you'll want to do something along these lines:

1. Create the project, say 'mysite':
  # paster create -t pycms_project
2. Create a virtualenv with:
  # virtualenv --no-site-packages VENV
3. enter the virtual environment
  # cd VENV; . bin/activate
4. create the buildout structure
  # paster create -t pycms_buildout
  Answer the question as to where the project is: this is the project you
  created in step 1
5. start the engine...
  # python bootstrap.py -c buildout-<whatever you wish>.cfg
  # ./bin/buildout -vN -c buildout-<whatever you wish>.cfg
  # ./bin/paster serve <you ini file>.ini


Making the egg
==============

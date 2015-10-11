Hello World Tempest Plugin
=====================
Basic Tempest plugin structure that runs a Hello World test case.

============
Installation
============
When Tempest runs, it will automatically discover the installed plugins. So we just need to install the Python packages that contains the plugin.

Clone the repository in your machine and install the package from the src tree:

.. code-block:: bash

    $ cd hello-world-tempest-plugin
    $ sudo pip install -e .
    
Using virtual environments
----------
If you run Tempest inside a virtualenv you have to ensure that the Python package containing the plugin is installed in the venv too.

E.g: Installing the plugin in a Tempest (from Rally) venv:

.. code-block:: bash

    $ . ~/.rally/tempest/for-deployment-x-x-x-x-x/.venv/bin/activate
    $ ~/.rally/tempest/for-deployment-x-x-x-x-x/.venv/bin/pip install -e ~/hello-world-tempest-plugin/
    
Validate that the plugin was installed correctly:

.. code-block:: bash  
    
    $ ~/.rally/tempest/for-deployment-x-x-x-x-x/.venv/bin/pip list
    
============
How to run the tests
============
1. To validate that Tempest discovered the test in the plugin, you can run:

   .. code-block:: bash 

    $ testr list-tests | grep hello_world_tempest_plugin
    

   This command will show your complete list of test cases inside the plugin.


2. You can run the test cases by name or running the set names that they used as decorator through testr (Tempest) or Rally:

   .. code-block:: bash  
    
    $ testr run hello_world_tempest_plugin.tests.api.test_hello_world.TestHelloWorld.test_hello_world

   .. code-block:: bash  
    
    $ testr run --subunit smoke | subunit-2to1 | ./tools/colorizer.py
    
   .. code-block:: bash

    $ rally verify start --set smoke

SEPAL recipies' projects
========================

When interacting with SEPAL processes, a user will create "recipes". These recipes can be interconnected and work together inside a single project e.g. the :code:`Mosaics` used in a :code:`Classification`. To help users deal with these interconnections SEPAL is providing a :code:`Project` system that will help them to organize their works.

Overview
--------

Go to the processes interface of SEPAL (:btn:`<fas fa-globe>`) you should see the following, completed by a list of existing recipes if you've already created some in the previous releases.

.. thumbnail:: ../_images/feature/project/project-landing.png
    :title: Landing page of the processes exposing the project interface
    :group: recipe-process
    :align: center
    
the following intercation are available on this page: 

#.   add a recipe 
#.   manage the project 
#.   select a project 
#.   order recipies by name or update date
#.   edit recipes

In the next section we'll present how one can create a new project and manage the existing projects in its SEPAL account. 

Project
-------

.. note::

    Projets are personnal, they cannot be shared and they are not visible to other users.
    
.. tip:: 
    
    For every user a :code:`[no project]` project is created at registration step. This project will be the fallback for every recipes that was created before the publication of the feature. It cannot be deleted or renamed.
    
To create a project, click on :btn:`<fas fa-folder-tree> Projects`. It will open the following interface. then click on :btn:`<fas fa-pencil-alt> Add` to create a new project. Simply fill the name and press :btn:`<fas fa-check> Apply` to validate it. The newly created project will apear in the list. 

.. thumbnail:: ../_images/feature/project/new-project.png
    :title: project management popup windows
    :group: recipe-process
    :width: 49%
    
.. thumbnail:: ../_images/feature/project/project-create.png
    :title: Create project popup windows
    :group: recipe-process
    :width: 49%
    
To remove a project, click on the :btn:`<fas fa-trash>` icon next to its name. All the recipes included in the process will be destroyed as well.
    
.. thumbnail:: ../_images/feature/project/project-list.png
    :title: The list of projects available in your SEPAL account
    :group: recipe-process
    :align: center

Recipes
-------

When entering in the process interface by default no projects are selected, meaning that the user will see all the recipes available in its SEPAL account. All recipes are displayed using the following prototype: :code:`<project name> / <recipe name>`.

.. thumbnail:: ../_images/feature/project/all-recipies.png
    :title: All the recipies available in one account
    :group: recipe-process
    :align: center
    
From this page the user can customize and manage recipes. 

Filter recipies
^^^^^^^^^^^^^^^

click on (3) to filter the recipes according to their project. Once selected, only the recipes included in this project will be displayed. The field is clearable meaning that you can go back to the unfiltered state and select another project. :code:`[no project]` can also be selected. 

.. thumbnail:: ../_images/feature/project/filtered-recipes.png
    :title: The filtered recipes inclued in the "foo 2" project
    :group: recipe-process
    :align: center

Once a project is selected it will appear as "current project" in the project list:

.. thumbnail:: ../_images/feature/project/change-project.png
    :title: The list of project showing the currently selected project
    :group: recipe-process
    :align: center
    
Once a project is selected, any newly created recipe will fallback to the current project.

.. tip::

    If you don't want your recipe to be associated with any project, unfilter the list before clicking on :btn:`<fas fa-plus> Add recipe`. 

Edit recipies 
^^^^^^^^^^^^^

Recipe behavior can be edited directly from this view. Click the :btn:`<fas fa-edit> Edit` button to open the edition interface.

.. thumbnail:: ../_images/feature/project/edit-recipes.png
    :title: The recipe edit interface
    :group: recipe-process
    :align: center
    
from this interface you can:

-   :btn:`<fas fa-check> Select`: Select/unselect all the recipes shown on screen. Any other edition operation will be only applied on the selected recipe(s). 
-   :btn:`<fas fa-random> Move`: Move the selected recipe(s) to another project.
-   :btn:`<fas fa-trash> Remove`: Delete the recipe permanently. 

.. warning::

    Before deleting individual recipes make sure that they are not used as inputs in others. 
    
connect recipes
^^^^^^^^^^^^^^^

When creating recipes, like :code:`Classification` users can use other recipe as input for the process. To avoid flooding the dropdown with to many values only the recipes from the same projet will be displayed (left). If one still want to see all the recipes in the dropdown, click on :btn:`All` and all the recipes will be exposed using project names as headers (right).

.. thumbnail:: ../_images/feature/project/connected-project-only.png
    :title: dropdown that only shows the recipes from the same project
    :group: recipe-process
    :width: 49%
    
.. thumbnail:: ../_images/feature/project/connected-all-recipes.png
    :title: dropdown that shows all the recipes
    :group: recipe-process
    :width: 49%







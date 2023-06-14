SEPAL recipe projects
=====================

When interacting with SEPAL processes, a user will create "recipes", which can be interconnected and work together inside a single project (e.g. the :code:`Mosaics` used in a :code:`Classification`). To help with these interconnections, the SEPAL platform provides a :code:`Project` system to organize users' work.

Overview
--------

Go to the **Processes** interface of SEPAL (:btn:`<fa-solid fa-globe>`) (you should see the following; if you've already created recipes in previous releases, you will see a list of existing recipes).

.. thumbnail:: ../_images/feature/project/project-landing.png
    :title: Landing page for Processes, exposing the project interface
    :group: recipe-process
    :align: center

The following interactions are available on this page:

#.   Add a recipe
#.   Manage a project
#.   Select a project
#.   Order recipes by name, or update date
#.   Edit recipes

Read the following section to understand how users can create a new project and manage existing projects in the SEPAL platform.

Project
-------

.. note::

    Projects are personal. They cannot be shared and they are not visible to other users.

.. tip::

    For every user, a :code:`[no project]` project is created during registration. This project will be the fallback for every recipe that was created before the publication of the feature. It cannot be deleted or renamed.

To create a project, select :btn:`<fa-solid fa-folder-tree> Projects`, which opens the following interface (see figure below). 

Then, select :btn:`<fa-solid fa-pencil> Add` to create a new project. Enter the name and select :btn:`<fa-solid fa-check> Apply`. 

The newly created project will now apear in the list.

.. thumbnail:: ../_images/feature/project/new-project.png
    :title: Project management pop-up windows
    :group: recipe-process
    :width: 49%

.. thumbnail:: ../_images/feature/project/project-create.png
    :title: Create project pop-up windows
    :group: recipe-process
    :width: 49%

To remove a project, select the :btn:`<fa-solid fa-trash>` icon (located next to its name). (Note: all recipes included in the process will be destroyed as well).

.. thumbnail:: ../_images/feature/project/project-list.png
    :title: The list of projects available in your SEPAL account
    :group: recipe-process
    :align: center

Recipes
-------

When entering the process interface, no projects are selected by default, meaning that users will see all of the recipes available in their SEPAL accounts. All recipes are displayed using the following prototype: :code:`<project name> / <recipe name>`.

.. thumbnail:: ../_images/feature/project/all-recipes.png
    :title: All of the recipes available in one account
    :group: recipe-process
    :align: center

From this page, the user can customize and manage recipes.

Filter recipes
^^^^^^^^^^^^^^

Select (3) to filter recipes according to your project. Once selected, only the recipes included in the project will be displayed. The field is clearable, meaning you can go back to the unfiltered state and select another project. :code:`[no project]` can also be selected.

.. thumbnail:: ../_images/feature/project/filtered-recipes.png
    :title: The filtered recipes inclued in the "foo 2" project
    :group: recipe-process
    :align: center

Once a project is selected, it will appear as "current project" in the project list (see figure below).

.. thumbnail:: ../_images/feature/project/change-project.png
    :title: The list of projects, showing the currently selected project
    :group: recipe-process
    :align: center

Once a project is selected and a recipe is created, it will belong to the selected project.

.. tip::

    If you don't want your recipe to be associated with any project, unfilter the list before selecting :btn:`<fa-solid fa-plus> Add recipe`.

Edit recipes
^^^^^^^^^^^^^

Recipe behaviour can be edited directly from this view. Select the :btn:`<fa-solid fa-pen-to-square> Edit` button to open the editing interface.

.. thumbnail:: ../_images/feature/project/edit-recipes.png
    :title: The recipe editing interface
    :group: recipe-process
    :align: center

From this interface, you can:

-   :btn:`<fa-solid fa-check> Select`: Select/unselect all the recipes shown on-screen. Any other editing operation will only be applied on the selected recipe(s).
-   :btn:`<fa-solid fa-shuffle> Move`: Move the selected recipe(s) to another project.
-   :btn:`<fa-solid fa-trash> Remove`: Delete the recipe(s) permanently.

.. attention::

    Before deleting individual recipes, make sure that they are not used as inputs in others.

Connect recipes
^^^^^^^^^^^^^^^

When creating recipes such as :code:`Classification`, users can use other recipes as inputs for the process. To avoid flooding the dropdown list with too many values, only the recipes from the same projet will be displayed (see figure on left). If one still wants to see all of the recipes in the dropdown list, select :btn:`All` and all of the recipes will be displayed using project names as headers (see figure on right).

.. thumbnail:: ../_images/feature/project/connected-project-only.png
    :title: Dropdown list that only shows recipes from the same project
    :group: recipe-process
    :width: 49%

.. thumbnail:: ../_images/feature/project/connected-all-recipes.png
    :title: Dropdown that shows all of the recipes
    :group: recipe-process
    :width: 49%







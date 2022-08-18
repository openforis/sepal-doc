Resources management
====================

SEPAL is providing free access to computation resources meaning that these resources are shared among our users. To prevent exportation mistakes new user are granted few resources that are sufficient for discovering the functionalities and run sub-regional analysis. and there instances are closed automatically when they are not used.

.. note::
    
    The SEPAL user starter pack includes:
    
    - 1 $/month of instance spending
    - 1 $/month of storage spending
    - 20 Gb of storage
    
    
Some projects or works will require more storage to perform province or even country analysis or more instance quota because you need to perform heavier computation processes. THe first solution will be to increase the time span of your instances and then your quota can be raised by administrators to grant you access to more resources.

.. important::

    quota request are studied by hand by our administrator, It can take times.

Resource management
-------------------

First, click on the resource management button. It's in the right side of the footer of the website. It can thus be accessed from any page (terminal, applications or recipes). It's showing the current instance consumption: :btn:`<fas fa-dollar-sign> x.xx/h`.

.. thumbnail:: ../_images/setup/resource/button_from_recipe.png
   :title: the resource management button from a recipe
   :width: 30%
   :group: setup_resource

.. thumbnail:: ../_images/setup/resource/button_from_app.png
   :title: the resource management button from an app
   :width: 30%
   :group: setup_resource

.. thumbnail:: ../_images/setup/resource/button_from_terminal.png
   :title: the resource management button from a terminal
   :width: 30%
   :group: setup_resource

Once you click on this button the resource management popup will open itself. There you'll find the current consumption of all your resources (1) expressed in percentages. when the bar is full you reached one of your montly quota. the second session describe the currently running instances (2) and finally the green button allows you to request extra resources.

.. thumbnail:: ../_images/setup/resource/resource_management.png
   :title: the resource management popup window
   :group: setup_resource

Manage instances 
----------------

AWS instances can be managed from this interface as well. from the User report, each line represent a differnet instance. You can see it's technical characteristics and the hourly quota consumption. click on :btn:`fas fa-trash` to kill it. 

.. thumbnail:: ../_images/setup/resource/edit_instance.png
   :title: edit the instance list by removing or increasing the lifespan of any of them
   :group: setup_resource

If the process you launched is a long computation (e.g. the BFAST application or any change detection algorithm), you don't want to let the SEPAL window open the whole time. To make sure that the process is run in the background, you simply need to ensure that the instance won't be killed before the end of the process. click on :btn:`<fas fa-edit>` to open the instance popup. there the sllider bar represent the amont of time before your instance will be shut down. Increase this value for the estimated duration of your process and you can then safely close the SEPAL browser tab. 

.. warning::

    If you increase the lifespan of your instance, it will continue to consume your quota, check regularly that your process is effectively running to avoid loosing resources for nothing.

.. thumbnail:: ../_images/setup/resource/change_duration.png
   :title: the resource management request form
   :group: setup_resource

Request computation resources
-----------------------------

from the resource manager, click on :btn:`<fas fa-pencil-alt> request additional resources`. It will open the request interface. every field must be completed if you want your request to be considered: 

- change the quota to a value that makes sense (you may not need more storage but simply more instance or vice versa). These values are just suggestions as ultimately the administrator will still be able to change them. (1)
- Give a us a extensive explaination on why you need these resources. key information are the project name, the type of analysis and the AOI. (2)

.. thumbnail:: ../_images/setup/resource/request.png
   :title: the resource management request form
   :group: setup_resource

Once validated the request is send to the administrators that will take measures in the next days to update your profile. They may also contact you directly if they need extra details on your request.

.. thumbnail:: ../_images/setup/resource/notification.png
   :title: the resource management notification that your resource request is being processed
   :group: setup_resource










   
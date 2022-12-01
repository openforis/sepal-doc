Resource management
===================

SEPAL provides free access to computation resources that are shared among our users. To prevent exportation mistakes, new users are granted few resources that are sufficient for discovering the functionalities and running sub-regional analysis. By default, instances are closed automatically when they are not being used.

.. note::
    
    The SEPAL user starter pack includes:
    
    - 0 USD/month of instance spending
    - 0 USD/month of storage spending
    - 0 Gb of storage    

Some actions or projects may require more storage to perform province- or country-analysis; other actions or projects may require more instances to perform heavier computation processes. 

If you need more storage or instances, you can submit a request to our administrators.

.. important::

    Since quota requests are reviewed on a case-by-case basis, response time may vary.

User report
-----------

Click on the User report button located on the lower-right side of the window in Terminal, Applications, or Recipes, and you will see the current instance consumption: :btn:`<fas fa-dollar-sign> x.xx/h`.

.. thumbnail:: ../_images/setup/resource/button_from_recipe.png
   :title: The User report button from a recipe.
   :width: 30%
   :group: setup_resource

.. thumbnail:: ../_images/setup/resource/button_from_app.png
   :title: The user report button from an app.
   :width: 30%
   :group: setup_resource

.. thumbnail:: ../_images/setup/resource/button_from_terminal.png
   :title: The user report button from a terminal.
   :width: 30%
   :group: setup_resource

After clicking on this button, the Resource management pop-up will appear, displaying the current consumption of all of your resources (1) expressed in percentages. A full bar indicates that you reached one of your monthly quotas. The second section describes instances that are currently running (2); the green button allows you to request extra resources.

.. thumbnail:: ../_images/setup/resource/resource_management.png
   :title: The user report popup window.
   :group: setup_resource

Manage instances 
----------------

Amazon Web Services (AWS) instances can be managed from this interface as well. In the User report pop-up, each line represents a different instance. You can see its technical features and the hourly quota consumption. Click on :btn:`fas fa-trash` to stop it. 

.. thumbnail:: ../_images/setup/resource/edit_instance.png
   :title: Edit the instance list by removing or increasing the lifespan of any of them.
   :group: setup_resource

If the process you launched is a long computation (e.g. the BFAST application or any change detection algorithm), you probably don't want to keep the SEPAL window open for the entire time. To make sure that the process is running in the background, you simply need click on :btn:`<fas fa-edit>` to open the instance pop-up, where the slider bar displays the amount of time remaining before your instance will be shut down. Increase this value for the estimated duration of your process and you can then safely close the SEPAL browser tab.

.. attention::

    If you increase the lifespan of your instance, it will continue to consume your quota. Check regularly that your process is running effectively to avoid losing resources.

.. thumbnail:: ../_images/setup/resource/change_duration.png
   :title: Increase the lifespan of a specific instance.
   :group: setup_resource

Request resources
-----------------

From the Resource manager, click on :btn:`<fas fa-pencil-alt> Request additional resources`, which will open the request interface. All of the following fields must be completed if you want your request to be considered: 

- Change the quota to values that meet your needs (e.g. more storage and fewer instances). The values entered are suggestions that the administrator will be able to change, if needed. (1)
- Give an extensive explanation for why you need these resources, as well as the following information: the project name, the type of analysis, and the area of interest (AOI). (2)

.. thumbnail:: ../_images/setup/resource/request.png
   :title: The Resource management request form.
   :group: setup_resource

Once validated, the request is sent to the administrators, who will take measures in the coming days to update your profile. They may also contact you directly if they need any extra details.

.. thumbnail:: ../_images/setup/resource/notification.png
   :title: The Resource management notification communicating that your resource request is being processed.
   :group: setup_resource

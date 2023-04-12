Manage your resources
=====================

Monitor usage and request resources
-----------------------------------

In this article, you can learn how to:

-Understand your **User report**
-Manage instances
-Request resources

SEPAL provides free access to computation resources that are shared among registered users. To prevent exportation mistakes, new users are granted few resources that are sufficient for discovering the functionalities and running sub-regional analysis. By default, instances are closed automatically when they are not being used.

.. note::

    The SEPAL user starter pack includes:

    - 0 USD/month of instance spending
    - 0 USD/month of storage spending
    - 0 Gb of storage

Some actions or projects may require more storage to perform analysis at the province or country level; other actions or projects may require more instances to perform heavier computation processes. If you need more storage or instances, you can submit a quota request to the SEPAL team by following the instructions below.

.. important::

    Since quota requests are reviewed on a case-by-case basis, response time may vary.

User report
-----------

In **Terminal**, **Applications** or **Recipes**, select **User report** on the lower-right side of the window to see your current instance consumption: :btn:`<fa-solid fa-dollar-sign> x.xx/h`.

.. thumbnail:: ../_images/setup/resource/button_from_recipe.png
   :title: The **User report** button from a **Recipe**.
   :width: 30%
   :group: setup_resource

.. thumbnail:: ../_images/setup/resource/button_from_app.png
   :title: The **User report** button from an **Application**.
   :width: 30%
   :group: setup_resource

.. thumbnail:: ../_images/setup/resource/button_from_terminal.png
   :title: The **User report** button from a **Terminal**.
   :width: 30%
   :group: setup_resource

After selecting this button, the **Resource management** pop-up window will appear, displaying the current consumption of all of your resources expressed in percentages (1) (Note: a full bar indicates that you have reached one of your monthly quotas) and instances that are currently running (2).

You can request additional resources by selecting the green button.

.. thumbnail:: ../_images/setup/resource/resource_management.png
   :title: The **User report** pop-up window.
   :group: setup_resource

Manage instances
----------------

Amazon Web Services (AWS) instances can be managed from this interface as well.

In the **User report** pop-up window, each line represents a different instance, where you can see their technical features and the hourly quota consumption.

You can select the **Trashcan** icon to stop an instance.

.. thumbnail:: ../_images/setup/resource/edit_instance.png
   :title: Edit the instance list by removing or increasing the lifespan of any of them.
   :group: setup_resource

If the process you launched is a long computation (e.g. the **BFAST application** or any **Change detection algorithm**) and you want to close the SEPAL window, you can run the process in the background.

Select **Edit** to open the **Instance** pop-up window, where the slider bar displays the amount of time remaining before your instance will be shut down. Increase this value for the estimated duration of your process and you can then safely close the SEPAL browser tab.

.. attention::

    If you increase the lifespan of your instance, it will continue to consume your quota. Check regularly that your process is running effectively to avoid losing resources.

.. thumbnail:: ../_images/setup/resource/change_duration.png
   :title: Increase the lifespan of a specific instance.
   :group: setup_resource

Request resources
-----------------

From the **Resource manager**, select **Request additional resources**.

In order for your request to be considered, you must:

- Change the quota to values that meet your needs (e.g. more storage and fewer instances). The values entered are suggestions that the administrator will be able to change, if needed. (1)
- Provide an extensive explanation for why you need these resources, as well as the project name, the type of analysis and the area of interest (AOI). (2)

.. thumbnail:: ../_images/setup/resource/request.png
   :title: The **Resource management** request form.
   :group: setup_resource

Once validated, the request is sent to the SEPAL team, who will take measures in the coming days to update your profile, which may include contacting you directly if they need any extra details.

.. thumbnail:: ../_images/setup/resource/notification.png
   :title: The **Resource management** notification communicating that your resource request is being processed.
   :group: setup_resource

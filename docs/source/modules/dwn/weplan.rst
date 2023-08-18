WePlan - Forests
================

Forest Restoration Planning Tool

Overview 
--------

WePlan - Forests is a decision support platform for tropical and subtropical forest ecosystem restoration planning that aims to optimise the benefits arising from forest restoration. A initiative of the International Institute for Sustainability Australia in partnership with the International Institute for Sustainability Rio and the Convention on Biological Diversity (CBD), with the support of Korea Forest Service via the Forest Ecosystem Restoration Initiative (FERI), the project provides quantitative, spatial, evidence-based planning support to developing countries party to the CBD in order to facilitate the realisation of forest restoration pledges and targets.

WePlan - Forests is a spatially explicit, forest restoration planning tool that uses linear programming to evaluate a range of alternative scenarios for restoration, reporting the benefits, costs and spatial distribution of national restoration priorities for each one. The current version (2.0) considers two objectives: (i) climate change mitigation benefit, estimated as the change in carbon sequestration that would arise from forest restoration, and (ii) biodiversity conservation benefit, estimated as the average reduction in local (national) extinction risk among all forest-associated species. The analysis also considers as constraints the opportunity and implementation costs of forest restoration, accounting for the potential for natural regeneration to reduce implementation costs. Analyses occur at a 1 km^2 resolution on a national basis, for countries containing tropical and subtropical forests within +/- 25 degrees latitude. Scenarios are offered in five levels of restoration targets, ranging from 10 to 50% of the areas available for restoration. All results for WePĺan-Forests and more information about the project, input data and methodology can be found on the `weplan forest platform website <http://weplan-forests.org>`.

The platform in SEPAL consists of a user-friendly SEPAL-based interface to retreive and manipulate the Geospatial data resulting from the WePlan - Forests optimisation for each pre-computed scenario.


Usage
-----

.. warning::

    This application is a prototype, data are provided for Uganda only.

Output
------

The output will be found in the user SEPAL files under :code:`module_results/weplan/<iso_code>` with :code:`iso_code` being the `ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__ code of the downloaded country (e.g. "UGA" for Uganda).

Every file is using the :code:`.tif` format with one single band expressing the variable described. and will display the version of the weplan-forest computation, here "v002", called :code:`<version>` from now on.

Planning solutions were developed for five area targets, representing 10, 20, 30, 40, and 50% of the area available for forest restoration in the country.

The application will retreive 4 types of analysis from the weplan forest project: 

-   :code:`available_<version>.tif`: the raster of the proportion of each cell deemed available for forest restoration within the seleted country.
-   :code:`scen_mincost_target_<X>_<version>.tif`: the minimum cost scenarios. These rasters are the optimal reference solutions that minimise total costs, ignoring benefits where :code:`<X>` is an integer referring to the target category.
-   :code:`scen_tradeoffs_ce_target_<X>_weight_<Y>_<version>.tif`: cost-effective scenarios. These rasters are the optimal solutions that maximise cost-effectiveness (benefit / cost), that is, provide the maximum benefit at the minimum possible cost, where :code:`X` is an integer referring to the target category and :code:`Y` is an integer referring to the order of relative weights between carbon and biodiversity objectives.
-   :code:`scen_tradeoffs_mb_target_<X>_weight_<Y>_<version>.tif`: max-benefit scenarios. These raster are the optimal solutions that maximise benefit, ignoring costs where :code:`X` is an integer referring to the target category and :code:`Y` is an integer referring to the order of relative weights between carbon and biodiversity objectives.

For more information about the computation methodology and the scenarios, please refer to the `WePlan-Forests website <http://www.weplan-forests.org/flrp/choose.php>`__.


.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/weplan/release/doc/en.rst

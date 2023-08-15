WePlan - Forests
================

*Forest restoration planning tool*

Overview
--------

WePlan - Forests is a decision-support platform for tropical and subtropical forest ecosystem restoration planning that aims to optimize the benefits arising from forest restoration.

It is an initiative of the International Institute for Sustainability Australia, in partnership with the International Institute for Sustainability Rio and the Convention on Biological Diversity (CBD), with the support of the Korea Forest Service via the Forest Ecosystem Restoration Initiative (FERI).

The project provides quantitative, spatial, evidence-based planning support to developing countries that are parties to the CBD in order to facilitate the realization of forest restoration pledges and targets.

WePlan - Forests is a spatially explicit, forest restoration planning tool that uses linear programming to evaluate a range of alternative scenarios for restoration, reporting the benefits, costs and spatial distribution of national restoration priorities for each.

The current version (2.0) considers two objectives:

-    **climate change mitigation benefit** (estimated as the change in carbon sequestration that would arise from forest restoration), and
-    **biodiversity conservation benefit** (estimated as the average reduction in local [national] extinction risk among all forest-associated species).

The analysis also considers (as constraints) the opportunity and implementation costs of forest restoration, accounting for the potential for natural regeneration to reduce implementation costs. 

Analyses occur at a 1 km^2 resolution on a national basis, for countries containing tropical and subtropical forests within +/- 25 degrees latitude. Scenarios are offered in five levels of restoration targets, ranging from 10 percent to 50 percent of the areas available for restoration.

Results for WePĺan - Forests, as well as more information about the project, input data and methodology, can be found on the `platform's website <http://weplan-forests.org>`.

The platform in SEPAL consists of a user-friendly SEPAL-based interface to retreive and manipulate the geospatial data resulting from WePlan - Forests optimisation for each pre-computed scenario.

Usage
-----

.. attention::

    This application is a prototype. Data are provided for Uganda only.

Output
------

The output will be found in your **SEPAL files** under :code:`module_results/weplan/<iso_code>` with :code:`iso_code` being the `ISO 3166-1 alpha-3 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3>`__ code of the downloaded country (e.g. "UGA" for Uganda).

Every file is in :code:`.tif` format with one single band expressing the variable described. It will display the version of the WePlan - Forests computation (here "v002", called :code:`<version>` from now on).

Planning solutions were developed for five area targets, representing 10 percent, 20 percent, 30 percent, 40 percent, and 50 percent of the area available for forest restoration in the country.

The application will retrieve four types of analysis from the WePlan - Forests project:

-   :code:`available_<version>.tif`: The raster of the proportion of each cell deemed available for forest restoration within the selected country.
-   :code:`scen_mincost_target_<X>_<version>.tif`: The minimum cost scenarios; these rasters are the optimal reference solutions that minimize total costs, ignoring benefits where :code:`<X>` is an integer referring to the target category.
-   :code:`scen_tradeoffs_ce_target_<X>_weight_<Y>_<version>.tif`: Cost-effective scenarios; these rasters are the optimal solutions that maximize cost-effectiveness (benefit/cost) (i.e. provide the maximum benefit at the minimum possible cost, where :code:`X` is an integer referring to the target category and :code:`Y` is an integer referring to the order of relative weights between carbon and biodiversity objectives).
-   :code:`scen_tradeoffs_mb_target_<X>_weight_<Y>_<version>.tif`: Max-benefit scenarios; these rasters are the optimal solutions that maximize benefit, ignoring costs where :code:`X` is an integer referring to the target category and :code:`Y` is an integer referring to the order of relative weights between carbon and biodiversity objectives.

For more information about the computation methodology and scenarios, refer to the `WePlan - Forests website <http://www.weplan-forests.org/flrp/choose.php>`__.

.. custom-edit:: https://raw.githubusercontent.com/sepal-contrib/weplan/release/doc/en.rst

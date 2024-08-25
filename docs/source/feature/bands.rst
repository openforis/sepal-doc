Optical Satellite bands, transformations, and indices
=====================================================

When exporting an optical satellite image in SEPAL, you can choose from a variety of bands, transformations, and indices to enhance your analysis and visualization. Understanding the characteristics and applications of different bands can help you optimize your image processing workflow and extract valuable insights from satellite data.

.. thumbnail:: ../_images/feature/bands/optical_bands.png
    :title: SEPAL Optical Bands to export
    :width: 50%
    :align: center


Bands
-----

Satellite imagery is composed of multiple bands, each capturing light in specific wavelengths. These bands are essential for various remote sensing applications, including land cover classification, vegetation monitoring, and environmental assessment. Understanding the characteristics and uses of different bands can help optimize image analysis and interpretation.

**Aerosol**
    - **Description**: Used for detecting aerosols (tiny particles) in the atmosphere, which can be crucial for air quality monitoring and climate studies.
    - **Usage**: Air pollution assessment, wildfire smoke tracking.

**Blue**
    - **Description**: Captures light in the blue wavelength (approximately 450-520 nm).
    - **Usage**: Coastal water mapping, vegetation health monitoring, and identification of shallow water bodies.

**Cirrus**
    - **Description**: A band designed to detect high-altitude cirrus clouds (often around 1.38 μm).
    - **Usage**: Cloud screening in high-altitude regions to improve atmospheric correction.

**Green**
    - **Description**: Captures light in the green wavelength (approximately 520-600 nm).
    - **Usage**: Mapping vegetation, water bodies, and urban areas.

**NIR (Near-Infrared)**
    - **Description**: Captures light in the near-infrared spectrum (approximately 800-900 nm).
    - **Usage**: Differentiating between vegetation and water, and monitoring vegetation health.

**Pan (Panchromatic)**
    - **Description**: Captures data in a single broad wavelength band, offering higher spatial resolution.
    - **Usage**: High-resolution imaging for mapping and urban planning.

**Red**
    - **Description**: Captures light in the red wavelength (approximately 600-700 nm).
    - **Usage**: Vegetation analysis, especially in calculating vegetation indices like NDVI.

**Red Edge**
    - **Description**: Captures light in the red-edge spectrum (around 700-750 nm), sensitive to chlorophyll content in plants.
    - **Usage**: Detailed vegetation health monitoring, particularly for precision agriculture.

**SWIR 1 (Shortwave Infrared 1)**
    - **Description**: Captures light in the shortwave infrared spectrum (approximately 1500-1750 nm).
    - **Usage**: Detecting moisture content in soil and vegetation, mapping burned areas.

**SWIR 2 (Shortwave Infrared 2)**
    - **Description**: Captures light in the shortwave infrared spectrum (approximately 2000-2300 nm).
    - **Usage**: Distinguishing snow from clouds, mapping geological features, and burn scars.

**Thermal**
    - **Description**: Measures thermal radiation emitted by the Earth's surface (usually around 10.4-12.5 µm).
    - **Usage**: Monitoring land surface temperature, heat islands, and volcanic activity.

**Water Vapor**
    - **Description**: Sensitive to atmospheric water vapor absorption, commonly used for weather and climate studies.
    - **Usage**: Studying cloud formation, precipitation, and humidity levels.


Tasseled Cap Transformation
---------------------------

The Tasseled Cap Transformation is a method to transform satellite imagery into three brightness components (Brightness, Greenness, and Wetness) and three color components (Red, Green, and Blue). This transformation is particularly useful for analyzing land cover changes, vegetation health, and urban development over time.

**Brightness**
    - **Description**: Measures the brightness band measures the overall brightness of the image, specifically the soil.
    - **Usage**: this band is often used to identify bare or partially covered soil, man-made features, and natural features like asphalt, concrete, gravel, and rock outcrops.

**Greenness**
    - **Description**: Measures the density and health of vegetation by capitalizing on the chlorophyll absorption in the red band and the high reflectance in the near-infrared band. It enhances the contrast between vegetated areas and non-vegetated areas.
    - **Usage**: Widely used in assessing plant health, monitoring crop conditions, tracking forest cover changes, and managing natural resources.

**Wetness**
    - **Description**: Captures moisture content in both soil and vegetation. This band is sensitive to the moisture continuum from dry to wet surfaces, helping to differentiate moist soils and saturated vegetation from dry areas.
    - **Usage**: Important for identifying wetlands, managing irrigation in agriculture, detecting flood-prone areas, and conducting soil moisture studies.

**Fourth Component**
    - **Description**: Often calibrated to highlight additional properties of vegetation or soil, such as senescence or specific soil types. The exact nature of this band can vary depending on the coefficients and sensor used.
    - **Usage**: Can be used to differentiate between types of vegetation or stages of crop maturity, and to detect stressed vegetation in forestry and agriculture.

**Fifth Component**
    - **Description**: Typically emphasizes land disturbance or variability in land cover types, providing a finer distinction between different types of ground cover and land use.
    - **Usage**: Useful in monitoring land cover changes over time, detecting disturbances like deforestation or urban expansion, and enhancing land cover classification schemes.

**Sixth Component**
    - **Description**: This band often captures more subtle or residual information that the other bands do not emphasize. It can be less directly interpretable and might be seen as highlighting noise or anomalies in the data.
    - **Usage**: Potentially useful for detecting subtle ecological changes, analyzing noise in the data for improved image processing, and refining classifications by providing additional context.


Vegetation Indices
------------------

Vegetation indices are mathematical transformations of satellite data that highlight specific vegetation properties, such as chlorophyll content, leaf area, or vegetation health. These indices are widely used in agriculture, forestry, and environmental monitoring to assess plant growth, detect stress, and monitor land cover changes.

**NDVI (Normalized Difference Vegetation Index)**
    - **Description**: Measures the density and health of vegetation by calculating the difference between the near-infrared (NIR) and red light reflected by vegetation. Healthy vegetation absorbs most of the visible light and reflects a large portion of the NIR.
    - **Usage**: Used to assess vegetation health, monitor drought, and manage agricultural operations.
    - **Formula**: (NIR - Red) / (NIR + Red)

**NDMI (Normalized Difference Moisture Index)**
    - **Description**: Highlights moisture content in vegetation by utilizing the NIR and short-wave infrared (SWIR1) bands. It is sensitive to moisture content in vegetation.
    - **Usage**: Useful in monitoring vegetation hydration and managing irrigation in agricultural contexts.
    - **Formula**: (NIR - SWIR1) / (NIR + SWIR1)

**NDWI (Normalized Difference Water Index)**
    - **Description**: Designed to identify and monitor changes in water content in vegetation, leveraging the green and NIR bands to maximize the reflection differences.
    - **Usage**: Employed in monitoring water stress in crops, detecting water bodies, and managing wetland areas.
    - **Formula**: (Green - NIR) / (Green + NIR)

**MNDWI (Modified Normalized Difference Water Index)**
    - **Description**: Enhances the detection of surface water by using the green and SWIR1 bands, reducing the influence of built-up land that can be confused with water in traditional NDWI.
    - **Usage**: Used to map and monitor surface water bodies, crucial for flood mapping and water resource management.
    - **Formula**: (Green - SWIR1) / (Green + SWIR1)

**NDFI (Normalized Difference Fraction Index)**
    - **Description**: Typically used to distinguish between different types of vegetation and non-vegetation elements, providing a measure of vegetation cover fraction.
    - **Usage**: Utilized in forest management and land cover classification tasks.
    - **Formula**: Index-specific, varies based on application.

**EVI (Enhanced Vegetation Index)**
    - **Description**: Improves the NDVI by optimizing the vegetation signal with improved sensitivity in high biomass regions and reducing background and atmospheric noise.
    - **Usage**: Frequently used in areas where vegetation monitoring requires greater sensitivity to biomass.
    - **Formula**: 2.5 * (NIR - Red) / (NIR + 6 * Red - 7.5 * Blue + 1)

**EVI2 (Enhanced Vegetation Index 2)**
    - **Description**: A refinement of EVI that uses only red and NIR bands, designed for areas where blue band data may not be reliable.
    - **Usage**: Ideal for vegetation monitoring through dense atmosphere or where the blue band is unavailable.
    - **Formula**: 2.5 * (NIR - Red) / (NIR + 2.4 * Red + 1)

**SAVI (Soil-Adjusted Vegetation Index)**
    - **Description**: Adjusts the NDVI for the influence of soil brightness, particularly useful in areas with sparse vegetation where soil is visible.
    - **Usage**: Applied in semi-arid regions to improve the accuracy of vegetation assessments.
    - **Formula**: (1.5 * (NIR - Red) / (NIR + Red + 0.5))

**NBR (Normalized Burn Ratio)**
    - **Description**: Utilizes NIR and SWIR2 bands to assess the severity of burn damage and the delineation of burned areas.
    - **Usage**: Key for assessing post-fire recovery in forested areas and mapping burn severity.
    - **Formula**: (NIR - SWIR2) / (NIR + SWIR2)

**MVI (Mangrove Vegetation Index)**
    - **Description**: Specifically designed to enhance the detection and monitoring of mangrove forests by using NIR and green bands.
    - **Usage**: Used in coastal management and conservation of mangrove ecosystems.
    - **Formula**: 0.1 * (NIR - Green) / abs(SWIR1 - Green)

**UI (Urban Index)**
    - **Description**: Highlights urban areas by exploiting the differences in reflection between SWIR2 and NIR bands.
    - **Usage**: Useful for urban mapping and monitoring changes in urban land use.
    - **Formula**: (SWIR2 - NIR) / (SWIR2 + NIR)

**NDBI (Normalized Difference Built-up Index)**
    - **Description**: Differentiates urban and built-up areas from natural land cover by using NIR and SWIR1 bands.
    - **Usage**: Employed in urban planning and studying urban heat islands.
    - **Formula**: (SWIR1 - NIR) / (SWIR1 + NIR)

**IBI (Index-based Built-up Index)**
    - **Description**: Combines NDBI with SAVI and MNDWI to provide a more comprehensive measure of built-up areas.
    - **Usage**: Useful in detailed urban analysis and land use classification.
    - **Formula**: (NDBI - (SAVI + MNDWI) / 2) / (NDBI + (SAVI + MNDWI) / 2)

**NBI (New Built-up Index)**
    - **Description**: Employs red, NIR, and SWIR1 bands to enhance the detection of built-up areas.
    - **Usage**: Applied in urban growth monitoring and land use planning.
    - **Formula**: Red * SWIR1 / NIR

**EBBI (Enhanced Built-Up and Bareness Index)**
    - **Description**: Focuses on urban areas and bare land by incorporating thermal and SWIR1 bands to detect built-up regions.
    - **Usage**: Crucial for urban mapping and identifying heat-stressed areas in cities.
    - **Formula**: (SWIR1 - NIR) / (10 * sqrt(SWIR1 + Thermal))

**BUI (Built-Up Index)**
    - **Description**: Combines multiple SWIR bands to enhance the detection and differentiation of built-up areas.
    - **Usage**: Employed in urban and regional planning to delineate built-up from natural areas.
    - **Formula**: (Red - SWIR1) / (Red + SWIR1) + (SWIR2 - SWIR1) / (SWIR2 + SWIR1)

**KNDVI (Kernel Normalized Difference Vegetation Index)**
    - **Description**: Applies a kernel function to traditional NDVI to improve sensitivity and accuracy in vegetation monitoring.
    - **Usage**: Used in precision agriculture and detailed vegetation studies where standard NDVI is not sufficient.
    - **Formula**: Kernel-function applied to NDVI, specific implementation details vary.

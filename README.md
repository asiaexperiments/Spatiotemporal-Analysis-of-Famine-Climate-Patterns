# Spatiotemporal-Analysis-of-Famine-Climate-Patterns
## Project Overview
### This project explores the relationship between famine occurrences and climate patterns in East Africa using spatiotemporal analysis and geospatial techniques. By mapping historical famine hotspots and analyzing climate trends (rainfall, temperature anomalies), we aim to identify key patterns that can aid food security planning and humanitarian interventions.

#### Research Questions
1.) Where are famine hotspots, and how have they shifted over time?
2.) How do rainfall and temperature trends vary across famine-affected regions?
3.)  Can we identify clusters of famine-prone areas based on climate anomalies?

####  Objectives
1.) Map famine occurrences over time using geospatial tools.
2.) Analyze climate trends in regions prone to famine.
3.) Identify spatial clusters where famine risk is consistently high.
4.) Provide visual insights through heatmaps and time-series geospatial analyses.

### Data Sources
This project integrates multiple datasets related to famine occurrences and climate patterns:
##### Climate Data (temperature anomalies, rainfall trends, drought indices) from:
- NOAA Climate Data
-NASA Earth Observation
-FAO Climate & Agriculture Data
-Dryad Climate Dataset
##### Famine Occurrence Data from:
-FEWS NET
-FAO Food Security Indicators
-Humanitarian Data Exchange (HDX)
##### Geospatial Data (country boundaries, admin regions) from:
-Natural Earth
-OpenStreetMap

### Tools & Technologies
This project leverages Python and GIS tools for data processing, mapping, and analysis:

##### Programming & Data Processing:
- pandas, numpy, geopandas (for data handling)
- matplotlib, seaborn, folium (for visualization)
##### Geospatial Analysis:
- GeoPandas, Shapely, rasterio (for GIS operations)
- QGIS, Google Earth Engine, ArcGIS (for spatial mapping)
##### Clustering & Statistical Methods:
- Moran’s I for spatial autocorrelation
- DBSCAN / K-Means for famine-prone area clustering


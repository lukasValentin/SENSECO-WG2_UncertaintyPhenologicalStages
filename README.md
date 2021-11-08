# About

This repositories contains **scripts and data** to create scenarios of **Sentinel-2 (S2) Normalized Difference Vegetation Index (NDVI) time series** data to account for **radiometric uncertainty**. The **objective**
if this small exercise is to give a first rough estimate of the **impact of radiometric uncertainty on the timing of key phenological stages** such as start (SOS), peak (POS), and end of season (EOS).

The project is the **result of a summer school student project** jointly accomplished by Paulo Bernardina, Zaib un Nisa, Stefanie Steinhauser and Lukas Graf at the **[SENSECO](https://www.senseco.eu/) Eo-Sense 2.0 summer school in Plovidiv, Bulgaria** in September 2021.
It has been carried out within the scope of [SENSECO Working Group 2](https://www.senseco.eu/working-groups/wg2-temporal-gap/) ("Closing the temporal gap: from daily observations to seasonal trends") and has also received valuable inputs from
[SENSECO Working Group 4](https://www.senseco.eu/working-groups/wg4-data-quality/) ("Establishing data quality through traceability and uncertainty").

The research was supported by the Action CA17134 SENSECO (Optical synergies for spatiotemporal sensing of scalable ecophysiological traits) funded by COST (European Cooperation
in Science and Technology, www.cost.eu).

# Workflow

## S2 NDVI Data Acquisition

S2 NDVI data was acquired for a whole growing period (August 2017 to August 2018) for an agricultural field parcel in northern Bulgaria, where winter rapeseed (*Brassica Napus L.*) was grown.
To obtain the data a Jupyter Notebook running on [Google Colab](https://colab.research.google.com/drive/1Bud03PGWlVyBZoqvdJW_4iW1lJcDGIhC?usp=sharing) (requires a Google account) can be used that was provided
by Matias Salinero Delgado from the University of Valencia - many thanks for sharing!

## Scenario and Time Series Generation

For each NDVI image, we discarded the lower and upper 5% percentile and averaged the remaining values. We then assumed an uncertainty of 2% in the NDVI values and draw samples from a normal distribution
$`\mathcal{N}(0,\sigma)`$, where $`\sigma`$ denotes the standard deviation. In total, 10000 samples were generated this way to reflect the potential impact of radiometric uncertainty on NDVI values.
To reproduce this step, the **[R-script](./scripts/monte_carlo_simulations.R) written by Paulo Bernardino** can be used.

The 100000 NDVI time series generated were put into [DATimeS](https://doi.org/10.1016/j.envsoft.2020.104666) which is a stand-alone toolbox that can be acquired via the
[ARTMO](https://artmotoolbox.com/plugins-standalone/91-plugins-standalone/34-datimes.html) toolbox. DATimeS is a stand-alone image processing GUI toolbox that enables to perform different
advanced time series tasks for:

(1) generating spatially continuous maps from discontinuous data using conventional fitting and smoothing functions and advanced machine learning regression algorithms, and
(2) quantifying of phenological indicators (e.g., SOS, EOS, and POS) throughout multiple seasons.

Using DATimeS we interpolated and smoothed the data to extract SOS, POS, EOS, and the length of the growing season using a 30% threshold of the seasonal amplitude.

Finally, we analyzed the spread among the 10000 time series realizations in terms of these phenological stages and reported the standard uncertainty as measure of the standard uncertainty in days alongside
the min-max spread among the realizations. For that step a **[Python script](./scripts/phenology_simulations_analysis.py)** was used.

# Project Structure

In **`scripts`** you find the R script for generating the Monte Carlo simulations and the Python script used to analyse the outcomes of DATimeS.

In **`data`** you find a series of GeoTiff files with the extracted NDVI values for the field studied. The images can be reproduced (or generated for another region) using teh Jupyter notebook by [Matias Salinero Delgado](https://colab.research.google.com/drive/1Bud03PGWlVyBZoqvdJW_4iW1lJcDGIhC?usp=sharing).

# Citation



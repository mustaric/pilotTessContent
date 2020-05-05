#Learn Light Curve Data Analysis
In this set of tutorials we aim to show you how to select targets, retrieve data and manipulate that data to perform research tasks commonly done with light curve data. 


### Selecting Targets from the TESS Input Catalog
There are several ways to select the targets you want to study. You might already have a list of Right Ascension and Declination pairs, or star names from other catalogs. Frequnetly, the easiest way to ensure you get TESS or Kepler data back that you want is to cross-match that list to the TESS Input Catalog or the Kepler Input Catalog. These catalogs give ID numbers to each star and these numbers are used in the data files created by the mission.  At this point the TESS input catalog includes the Kepler Input Catalog IDs, as well as those from the K2 EPIC, Gaia and 2MASS. For more information on the TESS Input Catalog see this [overview](https://heasarc.gsfc.nasa.gov/docs/tess/tess-input-catalog-version-8-tic-8-is-now-available-at-mast.html) and the [release notes](https://outerspace.stsci.edu/display/TESS/TIC+and+CTL+Data+Release+Notes+Home+Page).

The TESS Input catalog is available through various services. For simple queries use the Python package astroquery. For more complicated queries, Table Access Protocal (TAP) access or [CASJobs](http://mastweb.stsci.edu/mcasjobs/) may be more appropriate. These last two allow you to do more SQL-like database queries on the table.

- Learn how to access the TESS Input Catalog with astroquery | [TIC Search](../notebooks/MAST/TESS/beginner_tic_search_hd209458/beginnner_tic_search_hd209458.ipynb)
- Accessing the TIC using TAP and the Virtual Observatory's PyVO package | []()
- Searching by Footprint using GSSC

### Intro to TESS data products
These tutorials are designed to show you the content of the TESS and Kepler data products. These tutorials primarily rely on astroquery to retrieve the data and astropy to open the FITS files. In general these missions provide pixel level data contained in target pixel files, photometric time series contained in light curve files and full images of the sky contained in Full Frame Images (FFI). Kepler and TESS also provide data related to the exoplanet transit search called data validation files (DV is the name of the software module that validates an exoplanet found by the transit search).  

For TESS the Full Frame Images are also a time series, so working with the data can be tricky. MAST has provided a tool called TESScut which returns the pixels around a requested star in a target pixel file format. Be sure to use the version of TESScut that accesses the data on the cloud if working in the JupyterHub environment, especially if you plan to do a lot of cutouts, it will be faster. 

- Locate and downlad a light curve using astroquery. | [TESS]() | [Kepler]()
- Introduction to light curve files |  [TESS](../notebooks/MAST/TESS/beginner_how_to_use_lc/beginner_how_to_use_lc.ipynb) | [Kepler](./notebooks/MAST/Kepler/Kepler_Lightcurve/kepler_lightcurve.ipynb)
- Overview of the Planet Search Data Validation light curve files | [Astroquery Search](./notebooks/blob/master/notebooks/MAST/TESS/beginner_astroquery_dv/beginner_astroquery_dv.ipynb) | [Overview of Contents](./notebooks/MAST/TESS/beginner_how_to_use_dvt/beginner_how_to_use_dvt.ipynb)
- Intro to TESS Full Frame Images (FFI) | [TESS](./notebooks/MAST/TESS/beginner_how_to_use_ffi/beginner_how_to_use_ffi.ipynb)
- Cutting out the FFIs with TESScut | [MAST-hosted TESScut](./notebooks/MAST/TESS/interm_tesscut_astroquery/interm_tesscut_astroquery.ipynb) | [AWS-hosted TESScut]()

### Manipulating Light Curves with Community Software 
A couple of community software packages are available that provide easy ways to retrieve and manipulate time series data. While these are extremely convenient, it can be useful to first understand the basic data products of TESS, as shown above, and by reading the mission documentation. These tools provide wonderful visualizations and are well worth your time to learn.

- Lightkurve: An introduction to the lightcurve objects
- Lightkurve: An introduction to target pixel objects 
- Lighrkurve: How to stitch together data
- Lightkurve: Common detrending techniques
- Lightkurve: Co-trending with basis vectors
- Eleanor: Making FFI light curves 
- Eleanor: Pixel-Level Inspection of your data

### Science Examples
These tutorials are specific to a particular science case and show how to pull together some of the knowledge above.  Several rely on community provided software packages.

- K2flix: Making a movie of your pixels
- [Stellar Flares and Variable stars.](./notebooks/MAST/TESS/interm_tasc_lc/interm_tasc_lc.ipynb) by Clara Brasseur
- Pyriod: Find the pulsation modes of a variable stars
- exoplanet: Fit a transiting exoplanet
- astropy BLS: A planet search of the TESS FFI data
- Ruling out common systematic noise sources. [TESS]() | [Kepler]()
- Kepler planet search and occurrence rates
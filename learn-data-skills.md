#Learn Light Curve Data Analysis
In this set of tutorials we aim to show you how to select targets, retrieve data and manipulate that data to perform research tasks commonly done with light curve data. 


### Selecting Targets from the TESS Input Catalog
- Learn how to access the TESS Input Catalog with astroquery |[TIC Search](../notebooks/MAST/TESS/beginner_tic_search_hd209458/beginnner_tic_search_hd209458.ipynb)
- PyVO TAP access to astroquery
- CasJobs for sql access to large tables, an introduction

### Intro to TESS data products
These tutorials are intended to show you the content of various data products and the tutorials primarily rely on astroquery and astropy to retrieve and open the data.

- Using astroquery to find light curve files for your target.
- Introduction to light curve and target pixel files |  [TESS](../notebooks/MAST/TESS/beginner_how_to_use_lc/beginner_how_to_use_lc.ipynb) | [Kepler]()
- Planet Search Data Validation light curve files
- Intro to TESS Full Frame Images (FFI)
- Cutting out the FFIs with TESScut

### Manipulating Light Curves with Community Software 
A couple of community software packages are available that provide easy ways to retrieve and manipulate data. While these are extremely convenient, it can be useful to first understand the basic data products of TESS, as shown above, and by reading the mission documentation.

- Lightcurve: An introduction to the lightcurve and target pixel objects 
- Lighrcurve: How to stitch together data
- Lightcurve: Common detrending techniques
- Lightcurve: Co-trending with basis vectors
- Eleanor: Making FFI light curves 
- Eleanor: Pixel-Level Inspection of your data

### Science Examples
These tutorials are more specific to a science case. Some rely on community provided software packages.

- K2flix: Making a movie of your pixels
- Pyriod: Find the pulsation modes of a variable stars
- exoplanet: Fit a transiting exoplanet
- astropy BLS: A planet search of the TESS FFI data
- Ruling out common systematic noise sources. [TESS]() | [Kepler]()
- Kepler planet search and occurrence rates
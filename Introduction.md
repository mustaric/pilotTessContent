# Welcome to  the TESS/Kepler/K2 Science Platform
## Hosted by STScI and the Mikulski Archive for Space Telescope

This JupyterHub instance running on AWS is intended to allow you to work with MAST's time series data without having to download it. This enables you to learn how to use NASA's photometric missions and provides a place that will allow you to work with large amounts of data hosted in the the AWS public buckets. 

This area assumes you are somewhat familiar with NASA's high cadence photometric missions, but not necessarily with exactly how the data is formatted or how to best use it. If you are looking for an introduction to TESS, Kepler or K2, we recommend some of these documents. 

- TESS Archive Manual
- TESS Mission Page
- Kepler Archive Manual
- K2 Mission

----
## Latest Updates -- What's new?
 - March 30, 2020 -- Added this document
 - March 29, 2020 -- Added nbgitpuller.

---

## A few Starting Points

### Intro to TESS data 
- TESS Input Catalog with astroquery
- Intro to target pixel files
- Intro to light curve files
- Intro to Full Frame Images (FFI) and rapid cutouts
- Using Astroquery to find data
- An introduction to manipulating TESS data light curves with Lightkurve.
- Using eleanor to make an FFI light curve
- How to detrend or co-trend a ligth curve

### Inspecting your data
- Pixel-level inspection
- Make a movie of your data
- Overlaying DSS Images

### Quick data visualizations
- Compare TIC sources with a TESS FFI Image
- Quick look light curves
- Explore mission data

----
### Cloud Computing
- Basics of AWS for Science: credentials, buckets, boto3
- Speeding up code with Dask
- 
    An Introduction to the AWS cloud, getting credentials and which MAST data sets that are available in the cloud.
    Writing and retrieving data from S3 Buckets, for those who need to create a lot of data. – Working with the public data sets.
    Adding more computational power with Dask.
    Sharing code and environments with your collaborators.
    Spinning up your own TESS JupyterHub.
    How to transfer files onto the platform: ssh, scp

### TESS Platform Info
- FAQ: How do I share data?  How do I pull down code? Collaboration?
- Overview of what's behind this platform.


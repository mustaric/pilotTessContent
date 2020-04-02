# Welcome to  the proto-TIKE 
## Hosted by STScI and the Mikulski Archive for Space Telescope

This JupyterHub instance running on AWS is intended to allow you to learn new tools, collaborate with your colleagues and ultimately perform your research on TESS and Kepler data. This enables you to learn how to use NASA's photometric missions and provides a place that will allow you to work with large amounts of data hosted in the the AWS public buckets. If you are new to JupyterHub, take this [quick tour](./Jupytertour) to familarize yourself with the platform and its capabilities.

This platform is pre-loaded with python software packages and Jupyter notebook tutorials that teach how to do research with the TESS and Kepler Data (see the directory `notebooks/` on the left). We use git to pull new and updated notebooks into this instance, so if you decide to alter these notebooks in a way you would like to keep, you should first make a copy for yourself. 

If you would like to contribute your notebook back to the repo, please do a pull request against the STScI notebooks repo. If something is missing from the platform that you need, please email the help desk, archive@stsci.edu.

----

## A Few Starting Points

**Learn Data Skills** If you are new to TESS data products and are trying to learn the best way to work with TESS catalogs, retrieve light curves, and manipulate time series data, start with [TESS Data Skills Tutorials](./leearn-data-skill.md).

**Plethora of FFI Cutouts**  If you are planning on working with the FFI data at scale and want to learn how the cloud can provide easy and rapid access to this data set, start with [TESScut in the Cloud](./tesscut-in-the-cloud.md).

**Data Visualizations** If you are more interested browsing the TESS and Kepler data holdings or quickly viewing the quality of the data that is available, start with [Quick Visualizations](./quick-visualizations.md).

**Cloud Computing** If you would like to learn more about Amazon Web Services and how you can fully utilize this cloud computing environment with tools like Dask, start with [Cloud Computing for TESS](./cloud-computing.md).


---


## More Information
The tutorials available here assume you are somewhat familiar with Astronomy, Python and NASA's light curve missions (TESS, Kepler or K2). If not, here are a few starting points.

- [TESS Archive Documentation](https://outerspace.stsci.edu/display/TESS)
- [TESS Mission Page](https://tess.mit.edu)
- [Kepler Documentation](https://archive.stsci.edu/missions-and-data/kepler/documents)
- [K2 Documentation](https://archive.stsci.edu/missions-and-data/k2/documents)

----

**TESS Platform News and Updates:**
The following are some of the most recent and important updates. See [this file](news.md) for a full list of news items. 
 
- 2020-04-30. Platform is made live. Welcome!
- 2020-04-28. New Software: exoplanet added.
- 2020-04-25. TESScut is now running using the cloud hosted data. 

----

----

---
Author: Susan E. Mullally, STScI

Last Updated: 2020-03-31

### Data and Meta-Data Visualizations
- Compare TIC sources with a TESS target pixel file (see tpfplotter)
- Quick look light curves and periodograms
- Combine TIC and archive availability
- Overlaying DSS and PanStarrs Images on TESS FFIs

### Science Examples
- K2flix: Making a movie of your pixels
- Pyriod: Find the pulsation modes of a variable stars
- exoplanet: Fit a transiting exoplanet
- astropy BLS: A planet search of the TESS FFI data
- Ruling out common systematic noise sources. [TESS]() | [Kepler]()
- Kepler planet search and occurrence rates

----
### Cloud Computing
- Intro to AWS for Scientists: credentials and costs
- Intro to AWS: S3 buckets and boto3
- Dask: Speeding up code with many processors
- ???

### Platform Information
- FAQ: How do I share data?  What resources does this provide? Installing software.
- Overview of how this platform was built.

---


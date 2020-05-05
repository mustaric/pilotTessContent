
# TESS FFIs and light curves in the cloud
If you are planning on accessing a lot of the TESS or Kepler data, it is worth paying attention to where the data is coming from.  Both the TESS and Kepler data are available through Amazon's public S3 buckets.  

- Abundant and speedy cutouts of TESS FFIs using TESScut 
- Accessing AWS public S3 buckets for TESS and Kepler.
- Using Community software in the cloud: Lightkurve and eleanor.


# Cloud Computing
Working on AWS is not exactly the same as working on your laptop. It provides access to high power machines and an almost local archive of mission data. However, it involves learning data handling using the S3 buckets and boto3.  What follows are tutorials and links to help you get started with using cloud-hosted data and computes.

- Intro to AWS: credentials and costs
- Intro to AWS: S3 buckets and boto3
- [Accessing cloud-hosted data with astroquery](./code/cloud_astroquery.ipynb)
- Dask: Speeding up code with many processors
- Optimizing your code in the cloud
- Spinning up your own EC2 instance of the proto-TIKE


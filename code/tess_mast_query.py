import numpy as np
from astroquery.mast import Catalogs
from astroquery.mast import Observations
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord
from astropy.wcs import WCS
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.table import QTable

import re

def get_tic_info(star_name, radius_deg=.10, maglimit = 14.5, cols=['ID', 'Tmag', 'Jmag', 'Teff','logg','ra', 'dec','TWOMASS','dstArcSec']):
        
    catalogData = Catalogs.query_object(star_name, radius = radius_deg, catalog = "TIC")
    want = catalogData['Tmag'] <= maglimit
    #I always want the first two regardless of magnitude, it returns sorted by angular distance
    want[0:2] = [True, True]
    
    return(catalogData[want][cols])

# Define a function to simplify the plotting command that we do repeatedly.
def plot_cutout(image):
    """
    Plot image and add grid lines.
    """
    plt.imshow(image, origin = 'lower', cmap = plt.cm.YlGnBu_r, 
           vmax = np.percentile(image, 92),
           vmin = np.percentile(image, 5))

    plt.grid(axis = 'both',color = 'white', ls = 'solid')



def overplot_ticffi(targetlist, cutout_deg = .1,nearest=10):
    """
    Plot tic positions on top of an ffi
    sector =0 means use the first available, otherwise use the specified sector.
    targetlist is a astropy table containing ID, ra, dec, Tmag
    The cutout will be performed around the first ra/dec
    """
    
    ra = targetlist[0]['ra']
    dec = targetlist[0]['dec']

    coord = SkyCoord(ra, dec, unit = "deg")
    
    npixels = 2*np.ceil(cutout_deg*3600/21) + 4 #This assumes 21arcsecond pixels)
    
    if npixels > 60:
        npixels = 60
        print("Warning: cutout size set to 80 pixels.")
    if npixels < 10:
        npixels = 10
    
    try:
        hdulist = Tesscut.get_cutouts(coord, size = npixels)
    except:
        print["Cutout not available"]
        return
    
    hdu = hdulist[0]
    firstImage = hdu[1].data['FLUX'][0]

    wcs = WCS(hdu[2].header)

    fig = plt.figure(figsize = (6, 6))
    fig.add_subplot(111, projection = wcs)
    plot_cutout(firstImage)

    plt.xlabel('RA', fontsize = 12)
    plt.ylabel('Dec', fontsize = 12)


    starloc = wcs.all_world2pix([[ra,dec]],0)  #Second is origin
    plt.scatter(starloc[0,0], starloc[0,1],s = 45,color = 'red')

    # Make it a list of Ra, Dec pairs of the bright ones. This is now a list of nearby bright stars.
    nearby_stars = list( map( lambda x,y:[x,y], targetlist['ra'], targetlist['dec'] ) )
    
    # Plot nearby stars as well, which we created using our Catalog call above.
    nearby_loc = wcs.all_world2pix(nearby_stars[1:nearest],0)
    plt.scatter(nearby_loc[1:nearest, 0], nearby_loc[1:nearest, 1], 
                s = 25, color = 'orange')
    
    for i,v in enumerate(nearby_loc[:nearest]):
        plt.annotate(str(i), (nearby_loc[i][0], nearby_loc[i][1]),
                     textcoords="offset points", xytext=(2,2), ha='left',
                    color = 'red', fontsize=15)
    plt.title("TIC "+ str(targetlist[0]['ID']))
    
    return firstImage, wcs

def get_twomin_obs(ticlist):
    """
    Given a list of ticids, return a table of all the data that is available on that target.
    The table will be well formated to just be one one describing 
    the available sectors per target.
    
    Input: list of ticids, int
    Return: full table (astropy table of tic, obsid, filenames, camera, ccd)
            for all relevant two minute data files.
            summary table (one line per ticid), list of sectors, list of camera and ccd
    """
    
    sectors=[]
    gis=[]
    obsid=[]
    tmin=[]
    tmax=[]
    exptime=[]
    target=[]
    
    dv_sectors=[]
    dv_obsid=[]
    dv_tmin=[]
    dv_tmax=[]
    dv_target=[]
    dv_exptime=[]
    
    for tic in ticlist:
        observations = Observations.query_criteria(obs_collection = "TESS",
                                             dataproduct_type = ["timeseries"],
                                             target_name = tic)
        if len(observations) > 0:
            observations.sort(keys=['sequence_number', 'target_name'])
            
            for obs in observations:
                #Match for multi-sector observations
                match = re.search("s\d\d\d\d-s\d\d\d\d",obs['obs_id'])
                
                if match == None:
                
                    if int(obs['target_name']) == int(tic):
                        obsid.append(obs['obs_id'])
                        gis.append(obs['proposal_id'])
                        sectors.append(obs['sequence_number'])
                        tmin.append(obs['t_min'])
                        tmax.append(obs['t_max'])
                        exptime.append(int(obs['t_exptime']/60.0))
                        target.append(obs['target_name'])
                    
                else:
                    dv_sectors.append(match.group(0))
                    dv_obsid.append(obs['obs_id'])
                    dv_tmin.append(obs['t_min'])
                    dv_tmax.append(obs['t_max'])
                    dv_target.append(obs['target_name'])
                    dv_exptime.append(int(obs['t_exptime']/60.0))
    
    ts_table = QTable([target, sectors, gis, obsid, exptime, tmin,tmax],
                 names=('target_tic', 'sectors', 'GI_nums', 'obs_id', 'Exp_time_min','t_min','t_max'),
                 meta={'name':'observation table'})
    dv_table = QTable([dv_target, dv_sectors, dv_obsid, dv_exptime, dv_tmin, dv_tmax],
                 names=('target_tic', 'sector_range','obs_id', 'Exp_time_min','t_min','t_max'),
                 meta={'name':'Multi-Sector Planet Search'})
    
    return ts_table, dv_table

def run_tic_info(ticid, maglimit):

    size = .11
    nearest = 15
    cols = ['ID', 'Tmag', 'Jmag', 'Teff','logg','ra', 'dec','dstArcSec']
    
    ticinfo = get_tic_info(ticid, radius_deg = size, cols=cols)
    ticinfo.show_in_notebook(display_length=nearest)
    
    image, wcs = overplot_ticffi(ticinfo, cutout_deg = size, nearest=nearest)
    
    ticlist = ticinfo['ID']
    obs_table, dv_table = get_twomin_obs(ticlist[0:3])
    obs_table.show_in_notebook()
    
    return(ticinfo)
    

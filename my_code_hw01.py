#-- my_code_hw01.py
#-- hw01 GEO1015.2022
#-- Sitong Li
#-- [5683688]

import random



def nn_xy(dt, kd, all_z, x, y):
    """
    !!! TO BE COMPLETED !!!
     
    Function that interpolates with nearest neighbour method.
     
    Input:
        dt:     the DT of the input points (a startinpy object)
        kd:     the kd-tree of the input points 
        all_z:  an array with all the z values, same order as kd.data
        x:      x-coordinate of the interpolation location
        y:      y-coordinate of the interpolation location
    Output:
        z: the estimation of the height value, 
           (raise Exception if outside convex hull)
    """
    #-- kd-tree docs: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree
    #-- you are *not* allowed to use the function for the nn interpolation that I wrote for startinpy
    #-- you need to write your own code for this step
    z = random.uniform(0, 100)
    raise Exception("Outside convex hull")
    return z


def idw_xy(dt, kd, all_z, x, y, power, radius):
    """
    !!! TO BE COMPLETED !!!
     
    Function that interpolates with IDW
     
    Input:
        dt:     the DT of the input points (a startinpy object)
        kd:     the kd-tree of the input points 
        all_z:  an array with all the z values, same order as kd.data
        x:      x-coordinate of the interpolation location
        y:      y-coordinate of the interpolation location
        power:  power to use for IDW
        radius: search radius
¨    Output:
        z: the estimation of the height value, 
           (raise Exception if (1) outside convex hull or (2) no point in search radius
    """
    #-- kd-tree docs: https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree
    z = random.uniform(0, 100)
    raise Exception("Outside convex hull")
    raise Exception("No point in search radius")
    return z


def tin_xy(dt, kd, all_z, x, y):
    """
    !!! TO BE COMPLETED !!!
     
    Function that interpolates linearly in a TIN.
     
    Input:
        dt:     the DT of the input points (a startinpy object)
        kd:     the kd-tree of the input points 
        all_z:  an array with all the z values, same order as kd.data
        x:      x-coordinate of the interpolation location
        y:      y-coordinate of the interpolation location
    Output:
        z: the estimation of the height value, 
           (raise Exception if outside convex hull)
    """
    #-- startinpy docs: https://startinpy.rtfd.io/
    #-- you are *not* allowed to use the function for the TIN interpolation that I wrote for startinpy
    #-- you need to write your own code for this step
    z = random.uniform(0, 100)
    raise Exception("Outside convex hull")
    return z


def nni_xy(dt, kd, all_z, x, y):
    """
    !!! TO BE COMPLETED !!!
     
    Function that interpolates with natural neighbour interpolation method (nni).
     
    Input:
        dt:     the DT of the input points (a startinpy object)
        kd:     the kd-tree of the input points 
        all_z:  an array with all the z values, same order as kd.data
        x:      x-coordinate of the interpolation location
        y:      y-coordinate of the interpolation location
    Output:
        z: the estimation of the height value, 
           (raise Exception if outside convex hull)
    """
    #-- startinpy docs: https://startinpy.rtfd.io/
    #-- you are *not* allowed to use the function for the nni interpolation that I wrote for startinpy
    #-- you need to write your own code for this step
    z = random.uniform(0, 100)
    raise Exception("Outside convex hull")
    return z
    



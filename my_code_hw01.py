#-- my_code_hw01.py
#-- hw01 GEO1015.2022
#-- Sitong Li
#-- [5683688]

import random
import math


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
    n=len(dt.points)
    dis=[]
    count=0
    cp = dt.closest_point(x, y)
    pt=dt.get_point(cp)
    z1=pt[2]
    z=dt.points[cp][2]
    assert z1==z
    # for i in range(1,n-1,1):
    #     x1=dt.points[i][0]
    #     y1=dt.points[i][1]
    #     dis[i]=math.sqrt((x1-x)*(x1-x)+(y1-y)*(y1-y))
    # min=dis[0]
    # for i in range(n-1):
    #     if min>=dis[i]:
    #         min=dis[i]
    #         count=i
    # z=dt.points[count][2]
    #print(x,y,dt.points[count][0],dt.points[count][1],dt.points[count][2])
    #z = random.uniform(0, 100)
    #if cp not in dt.convex_hull():
    if not dt.is_inside_convex_hull(dt.points[cp][0], dt.points[cp][1]):
        raise Exception("Outside convex hull")
    #raise Exception("Outside convex hull")
    return z

def dis(pt,x,y):
    return math.sqrt((pt[0]-x)**2+(pt[1]-y)**2)
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
    kd



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
    tri=dt.locate(x, y)
    p1=dt.get_point(tri[0])
    p2=dt.get_point(tri[1])
    p3=dt.get_point(tri[2])
    w1 = 0.5 * (p1[0] * p2[1] - p2[0] * p1[1] + p2[0] * y - x * p2[1] + x * p1[1] - p1[0] * y)
    w2 = 0.5 * ((x * p2[1] - p2[0] * y) + (p2[0] * p3[1] - p3[0] * p2[1]) + (p3[0]*y - p3[1] * x))
    w3 = 0.5 * ((p1[0] * y - x * p1[1]) + (p3[1] * x - y * p3[0]) + (p3[0] * p1[1] - p1[0] * p3[1]))
    z=(w2*p1[2]+w3*p2[2]+w1*p3[2])/(w1+w2+w3)
   # z = random.uniform(0, 100)
    if not dt.is_inside_convex_hull(x, y):
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
    



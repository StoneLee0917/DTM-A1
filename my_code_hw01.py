#-- my_code_hw01.py
#-- hw01 GEO1015.2022
#-- Sitong Li
#-- [5683688]

import random
import math
from typing import Any
import startinpy
import numpy as np
import scipy.spatial
from numpy import array
import json
import csv
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
    # n=len(dt.points)
    # dis=[]
    # count=0
    # cp = dt.closest_point(x, y)
    # pt=dt.get_point(cp)
    # z1=pt[2]
    # z=dt.points[cp][2]
    # assert z1==z
    # if not dt.is_inside_convex_hull(dt.points[cp][0], dt.points[cp][1]):
    #     raise Exception("Outside convex hull")
    # #raise Exception("Outside convex hull")
    pt=np.array([x,y])
    ptindex=kd.query(pt)  #(1,2) 1 is the distance and 2 is the index of the nearest point
    ptnz=kd.data[ptindex[1]]
    pt=dt.points[dt.closest_point(ptnz[0],ptnz[1])]
    z=pt[2]
    return z
    # for i in dt.points:
    #     if i[0]==ptnz[0] and i[1]==ptnz[1]:
    #         z=i[2]
    #         # print(z)
    #         return z

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
    if dt.is_inside_convex_hull(x, y) ==False:
        raise Exception("Outside convex hull")
    z = 0
   #(A1,A2)
    w=[]
    wsum=0
    #find the points within searching area
    ptindex=kd.query_ball_point([x,y],radius)
    if len(ptindex)==0:
        raise Exception("No point in search radius")

    for i in ptindex:
        pt_temp=kd.data[i]
        #get the height value of found points
        vi=dt.closest_point(pt_temp[0], pt_temp[1])

        j = dt.points[vi]
        pt=[j[0],j[1],j[2]]
        #pt=[0,0,0]
        weight=math.sqrt((pt[0]-x)**2+(pt[1]-y)**2)
        #weight = 1
        weight=weight**(-power)
        w.append(weight)
        z+=j[2]*weight

    for i in w:
        wsum+=i
    z=z/wsum

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
    z: float | Any = (w2*p1[2]+w3*p2[2]+w1*p3[2])/(w1+w2+w3)
   # z = random.uniform(0, 100)
    if not dt.is_inside_convex_hull(x, y):
        raise Exception("Outside convex hull")
    return z

def get_line(pt1,pt2):
    return((pt2[1]-pt1[1])/(pt2[0]-pt1[0]),(-(pt2[1]-pt1[1])*pt2[0]+(pt2[0]-pt1[0])*pt2[1])/(pt2[0]-pt1[0]))
# (-(pt2[1]-pt1[1])*pt2[0]+(pt2[0]-pt1[0])*pt2[1])/(pt2[0]-pt1[0])
def get_inpoint(kl1,kl2):
    return((kl2[1]-kl1[1])/(kl1[0]-kl2[0]),kl1[0]*(kl2[1]-kl1[1])/(kl1[0]-kl2[0])+kl1[1])
def get_perpenline(x1,y1,x2,y2):
    return( -(x2-x1)/(y2-y1),0.5*((y2-y1)**2+(x2-x1)**2)/(y2-y1))
def poly_area(pts):
    num=len(pts)


    pass
def CCircle(pt1,pt2,pt3):
    center=get_inpoint(get_perpenline(pt1[0],pt1[1],pt2[0],pt2[1]),get_perpenline(pt2[0],pt2[1],pt3[0],pt3[1]))
    return center
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
    x=100
    y=100
    pts=[x,y,0]
    # if dt.is_in_convex_hull(x,y) is False:
    #     raise Exception("Outside convex hull")
    # dt.write_geojson('try.json')

    # 找林解三角形的临界三角形，得到点生成新的dt，在上面做？用write检查，点序号没法保证
    tri_ind=dt.locate(x,y) #e.g. [12,34,45]
    a=tri_ind[0]
    b=tri_ind[1]
    c=tri_ind[2]
    tr_ar=[]
    for pt_ind in tri_ind:
        tr_temp=dt.incident_triangles_to_vertex(pt_ind)
        for i in tr_temp:
            for j in i:
                tr_ar.append(j)
                # if dt.is_triangle(np.array([i,a,b])) or dt.is_triangle([i,b,c]) or dt.is_triangle([i,a,c]):
                #     tr_ar.append(j)
    # is_triangle(t) --t an array of 3 vertex indices

    adj_ptind=[]
    for i in tr_ar:
        if i not in adj_ptind:
            adj_ptind.append(i)
    pts_nni=[]
    for i in adj_ptind:
        pts_nni.append(dt.get_point(i))
    pts_nni.append(dt.get_point(a))
    pts_nni.append(dt.get_point(b))
    pts_nni.append(dt.get_point(c))
    dt_nni = startinpy.DT()
    dt_nni.insert(pts_nni)
    dt_nni.write_geojson('try.json')

    dt_nni2=startinpy.DT()
    dt_nni.insert(pts_nni)
    # vip=dt_nni2.insert_one_pt(x,y,0)
    dt_nni2.write_geojson('try2.json')
    # dt.insert_one_pt(x,y,0)
    # dt.write_geojson('try3.json')
    array_vi=dt_nni2.adjacent_vertices_to_vertex(vip)
    # vip=dt.insert_one_pt(x,y,0)
    # array_vi=dt.adjacent_vertices_to_vertex(vip)
    # list_tri=dt.incident_triangles_to_vertex(vp)
    print(array_vi)

    return z




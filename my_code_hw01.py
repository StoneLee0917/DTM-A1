#-- my_code_hw01.py
#-- hw01 GEO1015.2022
#-- Sitong Li
#-- [5683688]

import random
import math
from typing import Any
import startinpy
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import scipy.spatial
from numpy import array
import json
import csv
def nn_xy(dt, kd, all_z, x, y):
    if dt.is_inside_convex_hull(x, y) is False:
        raise Exception("Outside convex hull")
    pt=np.array([x,y])
    ptindex=kd.query(pt)  #(1,2) 1 is the distance and 2 is the index of the nearest point
    ptnz=kd.data[ptindex[1]]
    pt=dt.points[dt.closest_point(ptnz[0],ptnz[1])]
    z=pt[2]
    return z

def dis(pt,x,y):
    return math.sqrt((pt[0]-x)**2+(pt[1]-y)**2)


def idw_xy(dt, kd, all_z, x, y, power, radius):
    if dt.is_inside_convex_hull(x, y) is False:
        raise Exception("Outside convex hull")
    z = 0

    #find the points within searching area
    ptindex=kd.query_ball_point([x,y],radius)
    if len(ptindex)==0:
        raise Exception("No point in search radius")
    w1=[]
    list_z=[]

    #get the height value of found points
    for i in ptindex:
        pt_temp=kd.data[i]
        x_temp=pt_temp[0]
        y_temp=pt_temp[1]
        # vi=dt.closest_point(x_temp, y_temp)
        # j = dt.get_point(vi)
        j = dt.get_point(i+1)
        weight=math.sqrt((x_temp-x)**2+(y_temp-y)**2)
        weight=weight**(-power)
        w1.append(weight)
        list_z.append(j[2])
    weight_arr=np.array(w1)
    sum=np.sum(weight_arr)
    weight_arr2=weight_arr/sum
    array_z=np.array(list_z)
    list_z=np.multiply(weight_arr2,array_z)
    z=np.sum(list_z)

    return z


def tin_xy(dt, kd, all_z, x, y):
    tri=dt.locate(x, y)
    p1=dt.get_point(tri[0])
    p2=dt.get_point(tri[1])
    p3=dt.get_point(tri[2])
    w1 = 0.5 * (p1[0] * p2[1] - p2[0] * p1[1] + p2[0] * y - x * p2[1] + x * p1[1] - p1[0] * y)
    w2 = 0.5 * ((x * p2[1] - p2[0] * y) + (p2[0] * p3[1] - p3[0] * p2[1]) + (p3[0]*y - p3[1] * x))
    w3 = 0.5 * ((p1[0] * y - x * p1[1]) + (p3[1] * x - y * p3[0]) + (p3[0] * p1[1] - p1[0] * p3[1]))
    z: float | Any = (w2*p1[2]+w3*p2[2]+w1*p3[2])/(w1+w2+w3)
    if not dt.is_inside_convex_hull(x, y):
        raise Exception("Outside convex hull")
    return z


def convex_polyarea(ps):
    # 基于向量叉乘计算多边形面积
    area = 0
    if (len(ps) < 3):
        return 0

    for i in range(len(ps)):
        if i!=len(ps)-1:
            triArea = (ps[i][0] * ps[i+1][1] - ps[i+1][0] * ps[i][1]) / 2
        else:
            triArea = (ps[i][0] * ps[0][1] - ps[0][0] * ps[i][1]) / 2
            # print(triArea)
        area += triArea
    # j=len(ps)-1
    # fn = (points[j][0] * points[0][1] - points[0][0] * points[j][1]) / 2
    # print(fn)
    return area

def ccir2(p1,p2,p3):
    A1=2*(p2[0]-p1[0])
    B1=2*(p2[1]-p1[1])
    C1=p2[0]**2+p2[1]**2-p1[0]**2-p1[1]**2
    A2=2*(p3[0]-p2[0])
    B2 = 2 * (p3[1] - p2[1])
    C2 = p3[0] ** 2 + p3[1] ** 2 - p2[0] ** 2 - p2[1] ** 2
    x=((C1*B2)-(C2*B1))/((A1*B2)-(A2*B1))
    y=((A1*C2)-(A2*C1))/((A1*B2)-(A2*B1))
    pt=[x,y]
    return pt

def get_vdarea(ad_vip,dt):
    a2 = []
    for pt in ad_vip:
        if pt == 0:
            a2.append(0)
            break
        tri_list = dt.incident_triangles_to_vertex(pt)
        cen = []
        # get the vertices of vd around pt using circumcircle center
        for i in tri_list:
            p1=dt.get_point(i[0])
            p2 = dt.get_point(i[1])
            p3 = dt.get_point(i[2])
            cen_p=ccir2(p1,p2,p3)
            cen.append(cen_p)
        area=convex_polyarea(cen)
        a2.append(area)
    return a2

def get_z(dt,ad_vip,a1,a2):
    # get weights
    weight = np.array(a1) - np.array(a2)
    sum = np.sum(weight)
    weight2 = weight / sum
    list_z = []

    # get zs
    for i in ad_vip:
        z_temp = dt.points[i][2]
        list_z.append(z_temp)
    array_z = np.array(list_z)

    list_z = np.multiply(weight2, array_z)
    z = np.sum(list_z)
    return z

def nni_xy(dt,kd,all_z,x,y):
    z=0
    if dt.is_inside_convex_hull(x, y) is False:
        raise Exception("Outside convex hull")
    vip=dt.insert_one_pt(x,y,z)
    ad_vip=dt.adjacent_vertices_to_vertex(vip)
    a2=get_vdarea(ad_vip,dt)
    a1=[]
    dt.remove(vip)
    a1=get_vdarea(ad_vip,dt)
    z=get_z(dt,ad_vip,a1,a2)
    return z

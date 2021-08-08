import numpy as np
import pandas as pd
import os

crossection = 0

def crosssec(crossxfile): # read crossx.html and spit out cross section
    crossfile = open(crossxfile)
    for line in crossfile:
        arrayLine = line.split()
        if "<td rowspan=1><center><a href=\"./HTML/run_01/results.html\">" in line:
            crosssection = arrayLine[3]
    return crosssection

def lamval(lhefile): # read lhe file and spit out lambda value
    lheFile = open(lhefile)
    for line in lheFile:
        arrayLine = line.split()
        if "gdr1x1" in line:
            lambdaval = arrayLine[2]
    return lambdaval
    
def mval(lhefile): # read lhe file and spit out mass value
    lheFile = open(lhefile)
    for line in lheFile:
        arrayLine = line.split()
        if "mh2" in line:
            mass = arrayLine[1]
    return mass

def hxcounter(lhefile): # read lhe file and count the number of heavy Higgs occurences that take place
    lheFile = open(lhefile)
    hxnum = 0
    for line in lheFile:
        if "35  2    1    2" in line:
            hxnum += 1
    return hxnum
    
def pointmaker(mass, lam, cosbma, crosssec): # make a data point using data and append to list of data
    tuple_point = tuple([mass, lam, cosbma, crosssec])
    return tuple_point

def pointnocos(mass, lam, crosssec): # make a data point without the cosbma value
    tuple_point = tuple([mass, lam, crosssec])
    return tuple_point

def pointmakerwithX(mass, lam, cosbma, crosssec, hxnum): # make a data point using data and append to list of data
    tuple_point = tuple([mass, lam, cosbma, crosssec, hxnum])
    return tuple_point

def datamaker(fignum, plotnum, llist, clist, mlist): # put in figure and plot number and this function generates points from the data
    filepath = '/storage/af/user/jmina/Plots/Daniel_Plots/Fig' + str(fignum) + '/Plot' + str(plotnum) + '_Data/Plot' + str(plotnum) + '_Data/'
    datalist1 = []
    for l in llist:
        for c in clist:
            for m in mlist:
                cross = crosssec(filepath + 'm' + str(m) + '_c' + str(c) + '_m' + str(m) + '/crossx.html')
                lam = lamval(filepath + str(l) + '_c' + str(c) + '_m' + str(m) + '/Events/run_01/unweighted_events.lhe')
                mass = mval(filepath + str(l) + '_c' + str(c) + '_m' + str(m) + '/Events/run_01/unweighted_events.lhe')
                cosbma = c
                datalist1.append(pointmaker(mass, lam, cosbma, cross))
    return datalist1

def datamakernoite(fignum, plotnum, date, kind=''): # generates dataframe based on figure number, plot number, date, and kind ('Q' or 'G')
    if kind == '':
        filepath = '/storage/af/user/jmina/Plots/Daniel_Plots/Fig' + str(fignum) + '/Plot' + str(plotnum) + '_Data_' + str(date) + '/Plot' + str(plotnum) + '_Data' + str(kind) + '/'
    else:    
        filepath = '/storage/af/user/jmina/Plots/Daniel_Plots/Fig' + str(fignum) + '/Plot' + str(plotnum) + '_Data_' + str(date) + '/Plot' + str(plotnum) + '_Data_' + str(kind) + '/'
    datalist1 = []
    for dir in os.listdir(filepath):
        cross = crosssec(filepath + dir + '/crossx.html')
        lam = lamval(filepath + dir + '/Events/run_01/unweighted_events.lhe')
        mass = mval(filepath + dir + '/Events/run_01/unweighted_events.lhe')
        datalist1.append(pointnocos(mass, lam, cross))
        df = pd.DataFrame(datalist1, columns = ['Mass', 'Lambda', 'Cross Section'])
        df['Mass'] = pd.to_numeric(df['Mass'])
        df['Lambda'] = pd.to_numeric(df['Lambda'])
        df['Cross Section'] = pd.to_numeric(df['Cross Section'])
    return df

def datamakerwithX(fignum, plotnum, llist, clist, mlist): # put in figure and plot number and this function generates points from the data
    filepath = '/storage/af/user/jmina/Plots/Daniel_Plots/Fig' + str(fignum) + '/Plot' + str(plotnum) + '/l'
    datalist1 = []
    for l in llist:
        for c in clist:
            for m in mlist:
                cross = crosssec(filepath + str(l) + '_c' + str(c) + '_m' + str(m) + '/crossx.html')
                lam = l#amval(filepath + str(l) + '_c' + str(c) + '_m' + str(m) + '/Events/run_01/unweighted_events.lhe')
                mass = m#val(filepath + str(l) + '_c' + str(c) + '_m' + str(m) + '/Events/run_01/unweighted_events.lhe')
                cosbma = c
                hxnum = hxcounter(filepath + str(l) + '_c' + str(c) + '_m' + str(m) + '/Events/run_01/unweighted_events.lhe')
                datalist1.append(pointmaker(mass, lam, cosbma, cross, hxnum))
    return datalist1

def two_d_arraymaker_row1(dataframe): # generate the first row of mass values to form a 2-D array for plotting
    tdframe = [[" "]]
    for mass in dataframe['Mass']:
        if float(mass) not in tdframe[0]:
            tdframe[0].append(float(mass))
    tdframe[0][1:] = sorted(tdframe[0][1:])
    return tdframe

def two_d_arraymaker_row2(dataframe): # generates the second row of cross sections according to the simulations run
    tdframe = two_d_arraymaker_row1(dataframe)
    rowlist = []
    rowlist.append(dataframe['Lambda'][0])
    for i in range(len(dataframe)):
        rowlist.append(dataframe.sort_values(by=['Mass'], ascending=True).reset_index()['Cross Section'][i])
    tdframe.append(rowlist)
    return tdframe

def two_d_arraymaker_row3(dataframe): # extrapolates cross section values according to a quadratic relationship with lambda
    tdframe = two_d_arraymaker_row2(dataframe)
    rowlist = []
    for lam in np.linspace(0.002, 0.025, 100):
        rowlist.append(lam)
        for i in range(len(tdframe[0]) - 1):
            rowlist.append((lam / 0.002) ** 2 * tdframe[1][i+1])
        tdframe.append(rowlist)
        rowlist = []
    return tdframe
        
def two_d_arraymaker(fignum, plotnum, date, kind=''): # produces plotting array based on figure number, plot number, date, and kind ('Q' or 'G')
    df = datamakernoite(fignum, plotnum, date, kind)
    return pd.DataFrame(two_d_arraymaker_row3(df))
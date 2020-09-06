'''
Created on Jul 9, 2014

@author: roj-idl71
'''
import os
import datetime
import numpy

from schainpy.model.graphics.jroplot_base import Plot, plt


class ScopePlot(Plot):

    '''
       Plot for Scope
    '''

    CODE = 'scope'
    plot_type = 'scatter'

    def setup(self):

        self.xaxis = 'Range (Km)'
        self.ncols = 1
        self.nrows = 1
        self.nplots = 1
        self.ylabel = 'Intensity [dB]'
        self.titles = ['Scope']
        self.colorbar = False
        self.width = 6
        self.height = 4

    def plot_iq(self, x, y, channelIndexList, thisDatetime, wintitle):

        yreal = y[channelIndexList,:].real
        yimag = y[channelIndexList,:].imag
        title = wintitle + " Scope: %s" %(thisDatetime.strftime("%d-%b-%Y"))
        self.xlabel = "Range (Km)"
        self.ylabel = "Intensity - IQ"

        self.y = yreal
        self.x = x
        self.xmin = min(x)
        self.xmax = max(x)


        self.titles[0] = title

        for i,ax in enumerate(self.axes):
            title = "Channel %d" %(i)
            if ax.firsttime:
                ax.plt_r = ax.plot(x, yreal[i,:], color='b')[0]
                ax.plt_i = ax.plot(x, yimag[i,:], color='r')[0]
            else:
                ax.plt_r.set_data(x, yreal[i,:])
                ax.plt_i.set_data(x, yimag[i,:])

    def plot_power(self, x, y, channelIndexList, thisDatetime, wintitle):
        y = y[channelIndexList,:] * numpy.conjugate(y[channelIndexList,:])
        yreal = y.real
        yreal = 10*numpy.log10(yreal)
        self.y = yreal
        title = wintitle + " Scope: %s" %(thisDatetime.strftime("%d-%b-%Y"))
        self.xlabel = "Range (Km)"
        self.ylabel = "Intensity"
        self.xmin = min(x)
        self.xmax = max(x)


        self.titles[0] = title

        for i,ax in enumerate(self.axes):
            title = "Channel %d" %(i)

            ychannel = yreal[i,:]

            if ax.firsttime:
                ax.plt_r = ax.plot(x, ychannel)[0]
            else:
                #pass
                ax.plt_r.set_data(x, ychannel)

    def plot_weatherpower(self, x, y, channelIndexList, thisDatetime, wintitle):


        y      = y[channelIndexList,:]
        yreal  = y.real
        yreal  = 10*numpy.log10(yreal)
        self.y = yreal
        title  = wintitle + " Scope: %s" %(thisDatetime.strftime("%d-%b-%Y %H:%M:%S"))
        self.xlabel = "Range (Km)"
        self.ylabel = "Intensity"
        self.xmin   = min(x)
        self.xmax   = max(x)

        self.titles[0] =title
        for i,ax in enumerate(self.axes):
            title    = "Channel %d" %(i)

            ychannel = yreal[i,:]

            if ax.firsttime:
                ax.plt_r = ax.plot(x, ychannel)[0]
            else:
                #pass
                ax.plt_r.set_data(x, ychannel)

    def plot_weathervelocity(self, x, y, channelIndexList, thisDatetime, wintitle):

        x = x[channelIndexList,:]
        yreal  = y
        self.y = yreal
        title = wintitle + " Scope: %s" %(thisDatetime.strftime("%d-%b-%Y %H:%M:%S"))
        self.xlabel = "Velocity (m/s)"
        self.ylabel = "Range (Km)"
        self.xmin   = numpy.min(x)
        self.xmax   = numpy.max(x)
        self.titles[0] =title
        for i,ax in enumerate(self.axes):
            title    = "Channel %d" %(i)
            xchannel    = x[i,:]
            if ax.firsttime:
                ax.plt_r = ax.plot(xchannel, yreal)[0]
            else:
                #pass
                ax.plt_r.set_data(xchannel, yreal)

    def plot_weatherspecwidth(self, x, y, channelIndexList, thisDatetime, wintitle):

        x = x[channelIndexList,:]
        yreal  = y
        self.y = yreal
        title = wintitle + " Scope: %s" %(thisDatetime.strftime("%d-%b-%Y %H:%M:%S"))
        self.xlabel = "width "
        self.ylabel = "Range (Km)"
        self.xmin   = numpy.min(x)
        self.xmax   = numpy.max(x)
        self.titles[0] =title
        for i,ax in enumerate(self.axes):
            title    = "Channel %d" %(i)
            xchannel    = x[i,:]
            if ax.firsttime:
                ax.plt_r = ax.plot(xchannel, yreal)[0]
            else:
                #pass
                ax.plt_r.set_data(xchannel, yreal)

    def plot(self):
        if self.channels:
            channels = self.channels
        else:
            channels = self.data.channels

        thisDatetime = datetime.datetime.utcfromtimestamp(self.data.times[-1])
        if self.CODE == "pp_power":
            scope = self.data['pp_power']
        elif self.CODE == "pp_signal":
            scope = self.data["pp_signal"]
        elif self.CODE == "pp_velocity":
            scope = self.data["pp_velocity"]
        elif self.CODE == "pp_specwidth":
            scope = self.data["pp_specwidth"]
        else:
            scope =self.data["scope"]

        if self.data.flagDataAsBlock:

            for i in range(self.data.nProfiles):

                wintitle1 = " [Profile = %d] " %i
                if self.CODE =="scope":
                    if self.type == "power":
                        self.plot_power(self.data.heights,
                                        scope[:,i,:],
                                        channels,
                                        thisDatetime,
                                        wintitle1
                                        )

                    if self.type == "iq":
                        self.plot_iq(self.data.heights,
                                     scope[:,i,:],
                                     channels,
                                     thisDatetime,
                                     wintitle1
                                    )
                if self.CODE=="pp_power":
                    self.plot_weatherpower(self.data.heights,
                               scope[:,i,:],
                               channels,
                               thisDatetime,
                               wintitle
                               )
                if self.CODE=="pp_signal":
                    self.plot_weatherpower(self.data.heights,
                               scope[:,i,:],
                               channels,
                               thisDatetime,
                               wintitle
                               )
                if self.CODE=="pp_velocity":
                    self.plot_weathervelocity(scope[:,i,:],
                               self.data.heights,
                               channels,
                               thisDatetime,
                               wintitle
                               )
                if self.CODE=="pp_spcwidth":
                    self.plot_weatherspecwidth(scope[:,i,:],
                               self.data.heights,
                               channels,
                               thisDatetime,
                               wintitle
                               )
        else:
            wintitle = " [Profile = %d] " %self.data.profileIndex
            if self.CODE== "scope":
                if self.type == "power":
                     self.plot_power(self.data.heights,
                                scope,
                                channels,
                                thisDatetime,
                                wintitle
                                )

                if self.type == "iq":
                    self.plot_iq(self.data.heights,
                                scope,
                                channels,
                                thisDatetime,
                                wintitle
                                )
            if self.CODE=="pp_power":
                self.plot_weatherpower(self.data.heights,
                                    scope,
                                    channels,
                                    thisDatetime,
                                    wintitle
                                       )
            if self.CODE=="pp_signal":
                self.plot_weatherpower(self.data.heights,
                                    scope,
                                    channels,
                                    thisDatetime,
                                    wintitle
                                       )
            if self.CODE=="pp_velocity":
                self.plot_weathervelocity(scope,
                                       self.data.heights,
                                       channels,
                                       thisDatetime,
                                       wintitle
                                       )
            if self.CODE=="pp_specwidth":
                self.plot_weatherspecwidth(scope,
                                       self.data.heights,
                                       channels,
                                       thisDatetime,
                                       wintitle
                                       )



class PulsepairPowerPlot(ScopePlot):
    '''
    Plot for  P= S+N
    '''

    CODE = 'pp_power'
    plot_type = 'scatter'
    buffering = False

class PulsepairVelocityPlot(ScopePlot):
    '''
    Plot for VELOCITY
    '''
    CODE = 'pp_velocity'
    plot_type = 'scatter'
    buffering = False

class PulsepairSpecwidthPlot(ScopePlot):
    '''
    Plot for WIDTH
    '''
    CODE = 'pp_specwidth'
    plot_type = 'scatter'
    buffering = False

class PulsepairSignalPlot(ScopePlot):
    '''
    Plot for S
    '''

    CODE = 'pp_signal'
    plot_type = 'scatter'
    buffering = False

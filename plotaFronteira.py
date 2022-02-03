from tkinter.ttk import Notebook
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib Notebook
import oapackage


def PlotaFronteira(data):
    """ datapoints=np.random.rand(2, 50)
    for ii in range(0, datapoints.shape[1]):
        
        w=datapoints[:,ii]
        fac=.6+.4*np.linalg.norm(w)
        datapoints[:,ii]=(1/fac)*w

    h=plt.plot(datapoints[0,:], datapoints[1,:], '.b', markersize=16, label='Non Pareto-optimal')
    _=plt.title('The input data', fontsize=15)
    plt.xlabel('Objective 1', fontsize=16)
    plt.ylabel('Objective 2', fontsize=16)
 """

 
    #Array de X e Y
    datapoints=np.random.rand(2, 50)
    
    print(datapoints," datapoints")
    print(data, " data")
    pareto=oapackage.ParetoDoubleLong()

    for ii in range(0, datapoints.shape[1]):
        w=oapackage.doubleVector( (datapoints[0,ii], datapoints[1,ii]))
        pareto.addvalue(w, ii)

    pareto.show(verbose=1)

    lst=pareto.allindices() # the indices of the Pareto optimal designs

    optimal_datapoints=datapoints[:,lst]

    h=plt.plot(datapoints[0,:], datapoints[1,:], '.b', markersize=16, label='Non Pareto-optimal')
    hp=plt.plot(optimal_datapoints[0,:], optimal_datapoints[1,:], '.r', markersize=16, label='Pareto optimal')
    plt.xlabel('Objective 1', fontsize=16)
    plt.ylabel('Objective 2', fontsize=16)
    plt.xticks([])
    plt.yticks([])
    _=plt.legend(loc=3, numpoints=1)
    plt.show()


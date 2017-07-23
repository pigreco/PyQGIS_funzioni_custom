"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def area_ha( feature, parent):
    """ Questa funzione ritorna il valore dell'area della geometria in ettari"""
    geom_area_ha = feature.geometry().area()/10000
    return geom_area_ha

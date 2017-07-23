"""
Define new functions using @qgsfunction. feature and parent must always be the
last args. Use args=-1 to pass a list of values as arguments
"""

from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def perimetro_km( feature, parent):
    """ Questa funzione ritorna il valore del perimetro della geometria in km"""
    geom_perimetro_km = feature.geometry().length()/1000
    return geom_perimetro_km

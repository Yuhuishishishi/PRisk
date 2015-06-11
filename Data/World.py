__author__ = 'Yuhui'
import Data.Continent as Continent
import Data.Territory as Territory

class World:
    # initialize continents
    _names = ["North America", "South America", "Europe", "Africa", "Asia", "Australia"]
    _weight = [5, 2, 5, 3, 7, 2]
    na = Continent(_names[0], _weight[0])
    sa = Continent(_names[1], _weight[1])
    eu = Continent(_names[2], _weight[2])
    afc = Continent(_names[3], _weight[3])
    asia = Continent(_names[4], _weight[4])
    aus = Continent(_names[5], _weight[5])

    # initialize territories
    # North America
    _names = ["Alaska", "Alberta", "Central America", "Eastern USA",
             "Greenland", "Northwest Territory", "Ontario", "Quebec", "Western USA"]
    na_t = {}
    for _idx, _name in enumerate(_names):
        _terr = Territory(_idx, _name, na, [])
        na_t[_idx] = _terr

    # South America
    _names = ["Argentina", "Brazil", "Peru", "Venezuela"]
    sa_t = {}
    for _idx, _name in enumerate(_names):
        _terr = Territory(_idx, _name, sa, [])
        sa_t[_idx] = _terr

    # Europe
    _names = ["GB", "Iceland", "Northen Europe", "Scandinavia", "Southern Europe",
             "Ukraine", "Western Europe"]
    eu_t = {}
    for _idx, _name in enumerate(_names):
        _terr = Territory(_idx, _name, eu, [])
        eu_t[_idx] = _terr

    # Africa
    _names = ["Congo", "East Africa", "Egypt", "Madagascar", "North Africa", "South Africa"]
    afc_t = {}
    for _idx, _name in enumerate(_names):
        _terr = Territory(_idx, _name, afc, [])
        afc_t[_idx] = _terr

    # Australia

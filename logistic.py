# -*- coding: UTF-8 -*-
import pyhop

__author__ = 'Bartosz'


# DEFINICJE OPERATORÓW
def pack_truck(state, package, truck):
    if state.loc[package] == state.loc[truck] and truck not in state.loc.values():
        state.loc[package] = truck
        state.cost += 1
        return state
    return False


def unpack_truck(state, package, truck):
    if state.loc[package] == truck:
        state.loc[package] = state.loc[truck]
        state.cost += 1
        return state
    return False


def pack_plane(state, package, plane):
    if state.loc[plane] == state.loc[package] and plane not in state.loc.values():
        state.loc[package] = plane
        state.cost += 3
        return state
    return False


def unpack_plane(state, package, plane):
    if state.loc[package] == plane:
        state.loc[package] = state.loc[plane]
        state.cost += 3
        return state
    return False


def travel_truck(state, truck, x, y):
    if state.places[x] == state.places[y] and state.loc[truck] == x:
        state.loc[truck] = y
        state.cost += 10
        return state
    return False


def travel_plane(state, plane, x, y):
    if state.places[x] != state.places[y] and state.loc[plane] == x:
        state.loc[plane] = y
        state.cost += 100
        return state
    return False


# DEFINICJE METOD
def transport_by_truck(state, package, x, y):
    # jeśli punkty w różnych miastach to mamy błąd
    if state.places[x] != state.places[y]:
        return False
    # sprawdzamy czy jest juz jakaś ciężarówka w x
    for truck in state.trucks:
        if state.loc[truck] == x:
            return [('pack_truck', package, truck), ('travel_truck', truck, x, y), ('unpack_truck', package, truck)]
    # jeśli nie, bierzemy dowolną z miasta w którym znajduje się x
    for truck in state.trucks:
        if state.trucks[truck] == state.places[x]:
            loc = state.loc[truck]
            return [('travel_truck', truck, loc, x), ('pack_truck', package, truck), ('travel_truck', truck, x, y),
                    ('unpack_truck', package, truck)]


def transport_by_plane(state, package, x, y):
    # jeśli punkty w tych samych miastach to mamy błąd
    if state.places[x] == state.places[y] or x not in state.airports.values() or y not in state.airports.values():
        return False
    # sprawdzamy czy jest juz jakiś samolot w x
    for plane in state.planes:
        if state.loc[plane] == x:
            return [('pack_plane', package, plane), ('travel_plane', plane, x, y), ('unpack_plane', package, plane)]
    # jeśli nie, bierzemy dowolny
    plane = state.planes.keys[0]
    loc = state.loc[plane]
    return [('travel_plane', plane, loc, x), ('pack_plane', package, plane), ('travel_plane', plane, x, y),
            ('unpack_plane', package, plane)]


def transport(state, package, x, y):
    if state.places[x] != state.places[y] and (x not in state.airports.values() or y not in state.airports.value()):
        result = [('transport_by_plane', package, x, y)]
        if x in state.airports.values():
            result.insert(0, ('transport_by_truck', package, x, y))
        if x in state.airports.values():
            result.append(('transport_by_truck', package, x, y))
        return result
    return False


# GŁÓWNY PROGRAM
if __name__ == '__main__':
    # stworzenie stanu
    state1 = pyhop.State('state1')
    state1.airports = {'Krakow': 'loc1', 'Kielce': 'loc2', 'Warszawa': 'loc6'}
    state1.loc = {'plane2': 'loc2', 'plane1': 'loc1', 'truck4': 'loc1', 'truck3': 'loc2', 'truck2': 'loc1',
                  'truck1': 'loc1', 'package1': 'loc1', 'package2': 'loc4'}
    state1.places = {'loc1': 'Krakow', 'loc2': 'Kielce', 'loc3': 'Krakow', 'loc4': 'Kielce', 'loc5': 'Warszawa',
                     'loc6': 'Krakow'}
    state1.trucks = {'truck1': 'Krakow', 'truck2': 'Krakow', 'truck3': 'Kielce', 'truck4': 'Krakow'}
    state1.planes = {'plane1': 'Krakow', 'plane2': 'Kielce'}
    state1.cost = 0

    # deklaracja operatorów
    pyhop.declare_operators(pack_plane, pack_truck, unpack_plane, unpack_truck, travel_plane, travel_truck)

    # deklaracja metod
    pyhop.declare_methods('transport', transport_by_truck, transport_by_plane, transport)

    pyhop.print_methods()
    pyhop.print_operators()

    # uruchomienie solvera
    pyhop.pyhop(state1, [('transport', 'package1', 'loc1', 'loc6'), ('transport', 'package2', 'loc4', 'loc2')],
                verbose=1)

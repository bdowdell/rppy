#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    rppy - a geophysical library for Python
#    Copyright (C) 2015  Sean M. Contenti
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from rppy import rppy
import numpy as np


def test_batzle_wang_brine():
    err = 0.0001

    # Test low-pressure, low-temperature brine properties
    T = 25
    P = 5
    S = 30000
    expected_rho = 1.0186679
    expected_Vp = 1535.572

    gas = rppy.batzle_wang(P, T, 'brine', S=S)

    assert np.abs(gas['rho'] - expected_rho) < err
    assert np.abs(gas['Vp'] - expected_Vp) < err


def test_batzle_wang_oil():
    err = 0.0001

    # Test low-pressure, low-temperature oil properties
    T = 25
    P = 5
    G = 0.6
    api = 21
    Rg = 7
    expected_rho = 0.9211315
    expected_Vp = 1469.1498

    gas = rppy.batzle_wang(P, T, 'oil', G=G, api=api, Rg=Rg)

    assert np.abs(gas['rho'] - expected_rho) < err
    assert np.abs(gas['Vp'] - expected_Vp) < err


def test_batzle_wang_gas():
    err = 0.0001

    # Test low pressure, low temperature gas properties
    T = 15
    P = 3
    G = 0.6
    expected_rho = 0.02332698
    expected_K = 4.264937

    gas = rppy.batzle_wang(P, T, 'gas', G=G)

    assert np.abs(gas['rho'] - expected_rho) < err
    assert np.abs(gas['K'] - expected_K) < err

    # Test high-pressure, high-temperature gas properties
    T = 180
    P = 13
    G = 0.6
    expected_rho = 0.060788613
    expected_K = 25.39253

    gas = rppy.batzle_wang(P, T, 'gas', G=G)

    assert np.abs(gas['rho'] - expected_rho) < err
    assert np.abs(gas['K'] - expected_K) < err


def test_snell():
    err = 0.01
    vp1 = 2500
    vs1 = 1725
    vp2 = 3800
    vs2 = 1900
    theta1 = 30

    theta2E = 49.46
    thetas1E = 20.18
    thetas2E = 22.33

    theta2, thetas1, thetas2, p = rppy.snell(vp1, vp2, vs1, vs2, np.radians(theta1))

    assert np.abs(np.rad2deg(theta2) - theta2E) < err
    assert np.abs(np.rad2deg(thetas1) - thetas1E) < err
    assert np.abs(np.rad2deg(thetas2) - thetas2E) < err


def test_youngs():
    err = 0.01
    E = 70
    v = 0.3
    u = 26.92
    K = 58.33
    L = 40.38
    expected = E

    assert np.abs(rppy.youngs(v=v, u=u) - expected) < err
    assert np.abs(rppy.youngs(v=v, K=K) - expected) < err
    assert np.abs(rppy.youngs(v=v, L=L) - expected) < err
    assert np.abs(rppy.youngs(u=u, K=K) - expected) < err
    assert np.abs(rppy.youngs(u=u, L=L) - expected) < err
    assert np.abs(rppy.youngs(K=K, L=L) - expected) < err


def test_poissons():
    err = 0.01
    E = 70
    v = 0.3
    u = 26.92
    K = 58.33
    L = 40.38
    expected = v

    assert np.abs(rppy.poissons(E=E, u=u) - expected) < err
    assert np.abs(rppy.poissons(E=E, K=K) - expected) < err
    assert np.abs(rppy.poissons(E=E, L=L) - expected) < err
    assert np.abs(rppy.poissons(u=u, K=K) - expected) < err
    assert np.abs(rppy.poissons(u=u, L=L) - expected) < err
    assert np.abs(rppy.poissons(K=K, L=L) - expected) < err


def test_shear():
    err = 0.01
    E = 70
    v = 0.3
    u = 26.92
    K = 58.33
    L = 40.38
    expected = u

    assert np.abs(rppy.shear(E=E, v=v) - expected) < err
    assert np.abs(rppy.shear(E=E, K=K) - expected) < err
    assert np.abs(rppy.shear(E=E, L=L) - expected) < err
    assert np.abs(rppy.shear(v=v, K=K) - expected) < err
    assert np.abs(rppy.shear(v=v, L=L) - expected) < err
    assert np.abs(rppy.shear(K=K, L=L) - expected) < err


def test_bulk():
    err = 0.01
    E = 70
    v = 0.3
    u = 26.92
    K = 58.33
    L = 40.38
    expected = K

    assert np.abs(rppy.bulk(E=E, v=v) - expected) < err
    assert np.abs(rppy.bulk(E=E, u=u) - expected) < err
    assert np.abs(rppy.bulk(E=E, L=L) - expected) < err
    assert np.abs(rppy.bulk(v=v, u=u) - expected) < err
    assert np.abs(rppy.bulk(v=v, L=L) - expected) < err
    assert np.abs(rppy.bulk(u=u, L=L) - expected) < err


def test_lame():
    err = 0.01
    E = 70
    v = 0.3
    u = 26.92
    K = 58.33
    L = 40.38
    expected = L

    assert np.abs(rppy.lame(E=E, v=v) - expected) < err
    assert np.abs(rppy.lame(E=E, u=u) - expected) < err
    assert np.abs(rppy.lame(E=E, K=K) - expected) < err
    assert np.abs(rppy.lame(v=v, u=u) - expected) < err
    assert np.abs(rppy.lame(v=v, K=K) - expected) < err
    assert np.abs(rppy.lame(u=u, K=K) - expected) < err


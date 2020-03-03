#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Vincent MAGNIN, 2016-2019

'''
Surveillance d'un fichier XMLTV contenant les programmes de la TNT pour les
prochains jours.
'''

# https://pypi.org/project/pipimport/
try:
    import pipimport
    pipimport.install()
except ImportError:
    print("Les éventuels modules manquants peuvent être installés par pipimport (version du 4 août 2015), que vous pouvez installer depuis https://github.com/chaosct/pipimport")

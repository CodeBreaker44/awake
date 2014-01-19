# This file is part of Awake - GB decompiler.
# Copyright (C) 2014  Wojciech Marczenko (devdri) <wojtek.marczenko@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from awake.rom import Rom
from awake.database import Database
from awake.disasm import Z80Disasm

class Project(object):
    def __init__(self, filename):
        self.filename = filename
        self.rom = Rom(self.filename)
        self.database = Database('data/xxx.db')
        self.disasm = Z80Disasm(self)

    def close(self):
        pass
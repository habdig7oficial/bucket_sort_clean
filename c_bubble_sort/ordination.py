 # Copyright ©️ 2024 Mateus Felipe da Silveira Vieira
 
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>5.

from ctypes import *

import pathlib

root = pathlib.Path(__file__).parent.resolve()
bubble_sort = CDLL(f"{root}/methods/bubble_sort/bubble_sort.so").bubble_sort

bubble_sort.argtypes = [POINTER(c_float), c_float]
bubble_sort.restype = POINTER(c_float)

def to_c_array(arr: list[float]):
    return (c_float * len(arr))(*arr)


#teste = [1233, 15, 100]

#p_teste = to_c_array(teste)
#x = bubble_sort(p_teste, c_float(len(teste)))

#for i in range(len(teste)):
#    print(x[i])


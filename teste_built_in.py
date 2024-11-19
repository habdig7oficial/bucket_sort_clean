##   Copyright 2024 Antônio Augusto Maguetta Feitosa, Mateus Felipe da Silveira Vieira

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the Affero GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    Affero GNU General Public License for more details.

#    You should have received a copy of the Affero GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>5.



from bucket_sort import *

lista = [10, 154, 8, 0, 9, 48, 7, 55, 5]
#lista = [0.47, 0.93, 0.82, 0.12, 0.42, 0.03, 0.62, 0.38, 0.77, 0.91, 0.5]

x = bucket_sort_built_in(lista)

print(x)
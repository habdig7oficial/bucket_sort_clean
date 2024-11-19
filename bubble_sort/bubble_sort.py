##   Copyright 2024 Mateus Felipe da Silveira Vieira

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



def bubble_sort(vec, key = None, reverse = False):

    #print(f"\nvec: {vec}")
    if key == None:
        key = vec.copy()
       # print(f"\nkey: {key}")
    #print(key)
    
    for i in range(len(vec) - 1):
        for j in range(len(vec) - 1):
            if (key[j] > key[j + 1] and reverse == False) or (key[j] < key[j + 1] and reverse == True):

                aux = key[j]
                key[j] = key[j + 1]
                key[j + 1] = aux
                
                aux = vec[j]
                vec[j] = vec[j + 1]
                vec[j + 1] = aux
                #print(f"key[j]: {key[j]} - {key[j + 1]} - {vec[j]} - {vec[j + 1]}")
                #print(vec)
    return vec

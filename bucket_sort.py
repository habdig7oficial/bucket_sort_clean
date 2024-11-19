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


def bucket_sort(array: list[float]):
    buckets = [[] for i in range(len(array))]
    print(f"Balde Vazio: {buckets}\n")
    i = 0
    while i < len(array):
        index = int(array[i] * len(array))
        buckets[index].append(array[i])
        print(f"i: {i} -- nº do balde: {index} -- valor inserido: {array[i]}\n{buckets}\n")
        i += 1
    
    return buckets

def bucket_sort_built_in(array: list[float]):
    buckets = bucket_sort(array)
    i = 0
    while i < len(buckets):
        buckets[i].sort()
        i += 1
    flatten = [j for i in buckets for j in i]
    return flatten

from bubble_sort.bubble_sort import bubble_sort as py_bubble


def bucket_sort_bubble(array: list[float]):
    buckets = bucket_sort(array)
    i = 0
    while i < len(buckets):
        buckets[i] = py_bubble(buckets[i])
        i += 1
    flatten = [j for i in buckets for j in i]
    return flatten

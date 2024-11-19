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


# Função que realiza a ordenação
def bucket_sort(array: list[float]):
    # Encontrar o maior valor para normalizar os índices
    maximo = max(array)

    # Criar baldes vazios
    buckets = [[] for _ in range(len(array))]
    print(f"Balde Vazio: {buckets}\n")

    # Inserir os elementos nos baldes correspondentes
    for i in range(len(array)):
        # Normalizar o valor para o intervalo [0, 1] e calcular o índice
        index = int((array[i] / maximo) * (len(array) - 1))
        buckets[index].append(array[i])
        print(f"i: {i} -- nº do balde: {index} -- valor inserido: {array[i]}\n{buckets}\n")

    return buckets

# Método que organiza os baldes e retorna a lista ordenada
def bucket_sort_built_in(array: list[float]):
    # Preenche os baldes
    buckets = bucket_sort(array)

    # Ordena os elementos de cada balde
    for bucket in buckets:
        bucket.sort()

    # Concatena os baldes ordenados
    flatten = [num for bucket in buckets for num in bucket]
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

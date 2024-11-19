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


# Testando o algoritmo
lista = [10, 154, 8, 0, 9, 48, 7, 55, 5]

x = bucket_sort_built_in(lista)

print(f"Lista original: {lista}")
print(f"Lista ordenada: {x}")
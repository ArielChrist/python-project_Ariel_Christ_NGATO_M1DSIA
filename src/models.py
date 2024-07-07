import timeit

# vérifier les donnnées manquantes en parcourant chaque ligne 

def missing_data(data):
    """
    argument: prend comme argument un dictionnaire

    return: renvoie True si une ligne est vide, Flase sinon
    """
    for ligne in data:
        for valeur in ligne.values():
            if valeur == '' or valeur is None:
                return True
    return False


#Algorithme de Trie Rapide
def quicksort(arr, key):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if (key(x) if key else x) < (key(pivot) if key else pivot)]
        middle = [x for x in arr if (key(x) if key else x) == (key(pivot) if key else pivot)]
        right = [x for x in arr if (key(x) if key else x) > (key(pivot) if key else pivot)]
        return quicksort(left, key) + middle + quicksort(right, key)


#Algorithme de trie fusion
def merge_sort(arr, key):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, key)
        merge_sort(R, key)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if (key(L[i]) if key else L[i]) < (key(R[j]) if key else R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

#Algorithme de Trie fusion optimiser
def merge_sort_optimiser(arr, key):
    def merge_optimiser(left, right, left_keys, right_keys):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left_keys[i] < right_keys[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    L = merge_sort_optimiser(arr[:mid], key)
    R = merge_sort_optimiser(arr[mid:], key)

    L_keys = [key(item) for item in L]
    R_keys = [key(item) for item in R]

    return merge_optimiser(L, R, L_keys, R_keys)

#Algorithme de trie par tas
def heapify(arr, n, i, key):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and (key(arr[i]) if key else arr[i]) < (key(arr[left]) if key else arr[left]):
        largest = left

    if right < n and (key(arr[largest]) if key else arr[largest]) < (key(arr[right]) if key else arr[right]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heap_sort(arr, key):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

    return arr

#Algorithme de tri par tas optimiser
def heapify_optimiser(arr, n, i, key):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and key(arr[left]) > key(arr[largest]):
        largest = left

    if right < n and key(arr[right]) > key(arr[largest]):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_optimiser(arr, n, largest, key)

def heap_sort_optimiser(arr, key):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_optimiser(arr, n, i, key)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_optimiser(arr, i, 0, key)

    return arr


def measure_time(sort_func, data, key):
    start_time = timeit.default_timer()
    sort_func(data.copy(), key)  
    end_time = timeit.default_timer()
    return end_time - start_time
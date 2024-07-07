import matplotlib.pyplot as plt
from controller import verify
from models import *

def run():

    #initialisation de la clé de tri sur la premiere colonne de chaque dataset
    key = lambda x: list(x.values())[0]

    datasets = verify()
    quicksort_times = [measure_time(quicksort, data, key) for data in datasets]
    mergesort_optimiser_times = [measure_time(merge_sort_optimiser, data, key) for data in datasets]
    mergesort_times = [measure_time(merge_sort, data, key) for data in datasets]
    heap_sort_times = [measure_time(heap_sort, data, key) for data in datasets]
    heap_sort_optimiser_times = [measure_time(heap_sort_optimiser, data, key) for data in datasets]

    sizes = ['Commercial Aviation', 'Transport', 'Covid_19']
    bar_width = 0.15
    index = range(len(sizes))

    plt.bar(index, quicksort_times, bar_width, label='Tri rapide')
    plt.bar([i + bar_width for i in index], mergesort_times, bar_width, label='Tri fusion')
    plt.bar([i + 2 * bar_width for i in index], heap_sort_times, bar_width, label='Tri par tas')

    plt.xlabel('Dataset')
    plt.ylabel('Temps d"exécution (seconds)')
    plt.title('Comparaison de la performance des Algorithmes de tri')
    plt.xticks([i + 2 * bar_width for i in index], sizes)
    plt.legend()
    plt.show()

    sizes = ['Commercial Aviation', 'Transport', 'Covid_19']
    bar_width = 0.15
    index = range(len(sizes))

    plt.bar(index, quicksort_times, bar_width, label='Tri rapide')
    plt.bar([i + bar_width for i in index], mergesort_times, bar_width, label='Tri fusion')
    plt.bar([i + 2 * bar_width for i in index], mergesort_optimiser_times, bar_width, label='Tri fusion optimiser')
    plt.bar([i + 3 * bar_width for i in index], heap_sort_times, bar_width, label='Tri par tas')
    plt.bar([i + 4 * bar_width for i in index], heap_sort_optimiser_times, bar_width, label='Tri par tas optimiser')

    plt.xlabel('Dataset')
    plt.ylabel('Temps d"exécution (seconds)')
    plt.title('Comparaison de la performance des Algorithmes de tri optimiser')
    plt.xticks([i + 2 * bar_width for i in index], sizes)
    plt.legend()
    plt.show()



run()
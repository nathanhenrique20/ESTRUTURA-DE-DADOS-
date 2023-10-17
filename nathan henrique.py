import requests
import time

def get_lorem_ipsum_text():
    url = "https://www.lipsum.com/generate/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["text"]
    else:
        raise Exception

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        swap(arr, i, min_idx)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

text = get_lorem_ipsum_text()
words = text.split()[:1000]

start_time = time.time()
bubble_sort(words.copy())
bubble_sort_time = time.time() - start_time

start_time = time.time()
selection_sort(words.copy())
selection_sort_time = time.time() - start_time

start_time = time.time()
merge_sort(words.copy())
merge_sort_time = time.time() - start_time

target_words = ["egestas", "Tincidunt"]
binary_search_times = []

for target in target_words:
    start_time = time.time()
    index = binary_search(words, target)
    binary_search_times.append((target, time.time() - start_time))

print(f"Tempo de ordenação por Troca (Bubble Sort): {bubble_sort_time:.6f} segundos")
print(f"Tempo de ordenação por Seleção (Selection Sort): {selection_sort_time:.6f} segundos")
print(f"Tempo de ordenação por Intercalação (Merge Sort): {merge_sort_time:.6f} segundos")

for target, search_time in binary_search_times:
    print(f"Tempo de pesquisa binária para '{target}': {search_time:.6f} segundos")

fastest_sorting = min(bubble_sort_time, selection_sort_time, merge_sort_time)
fastest_sorting_algorithm = "Bubble Sort" if fastest_sorting == bubble_sort_time else \
                            "Selection Sort" if fastest_sorting == selection_sort_time else \
                            "Merge Sort"

print(f"O algoritmo de ordenação mais rápido foi '{fastest_sorting_algorithm}'.")


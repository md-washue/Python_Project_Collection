import random
import time

def making_half(array):
    if len(array) <= 1:
        return array
    half = len(array) // 2

    left = making_half(array[:half])
    right = making_half(array[half:])

    return merge_sort(left, right)

def merge_sort(left, right):
    array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1
        
    array.extend(left[i:])
    array.extend(right[j:])

    return array

def generate_data(size):
    print(f"[*] Generating {size:,} random data points...")
    return [random.randint(1, 100000) for _ in range(size)]


def run_benchmark(data):
    data_for_custom = data.copy()
    data_for_native = data.copy()

    print("[*] Running Custom Merge Sort...")
    start_time = time.time()
    making_half(data_for_custom)
    custom_time = time.time() - start_time
    print(f"    -> Time taken: {custom_time:.4f} seconds")

    print("[*] Running Python Native Sort...")
    start_time = time.time()
    data_for_native.sort()
    native_time = time.time() - start_time
    print(f"    -> Time taken: {native_time:.4f} seconds")

    if native_time > 0:
        speed_diff = custom_time / native_time
        print(f"\n[+] Result: Python's native sort was {speed_diff:.2f}x faster on this dataset.")


if __name__ == "__main__":
    print("=== Algorithm Benchmarker Tool ===\n")
    
    DATA_SIZE = 200000 
    
    test_dataset = generate_data(DATA_SIZE)
    print("--------------------------------------------------")
    
    run_benchmark(test_dataset)
    print("==================================================")
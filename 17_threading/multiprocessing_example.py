import multiprocessing
import time
import concurrent.futures

def cpu_bound_task(n):
    result = 0
    for i in range(n):
        result += i * i
    return result

def io_bound_task(seconds):
    time.sleep(seconds)
    return f"Task completed after {seconds} seconds"

def worker_process(name, numbers):
    print(f"Process {name} starting")
    total = sum(cpu_bound_task(n) for n in numbers)
    print(f"Process {name} finished with total: {total}")
    return total

if __name__ == "__main__":
    numbers = [100000, 200000, 300000, 400000]
    
    start_time = time.time()
    sequential_result = [cpu_bound_task(n) for n in numbers]
    sequential_time = time.time() - start_time
    print(f"Sequential execution time: {sequential_time:.2f} seconds")
    
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        parallel_result = pool.map(cpu_bound_task, numbers)
    parallel_time = time.time() - start_time
    print(f"Parallel execution time: {parallel_time:.2f} seconds")
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(cpu_bound_task, n) for n in numbers]
        results = [future.result() for future in futures]
        print(f"Results: {results}")
    
    processes = []
    for i in range(2):
        process = multiprocessing.Process(
            target=worker_process,
            args=(f"Worker-{i}", numbers[i:i+2])
        )
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    print("All processes completed")

import multiprocessing as mp
import random
import time
import matplotlib.pyplot as plt
from dask.distributed import Client 

def icircle(L, b):
  """Counts the number of (x, y) pairs inside the unit circle."""
  random.seed()  # Seed within the function for parallel execution
  M = sum(1 for _ in range(L) if random.random()**2 + random.random()**2 < 1)
  return M


def parpi(M, L, N):
  """Estimates pi using parallel execution and measures time."""
  client = Client(n_workers=M)
  start_time = time.time()
  counts = client.map( icircle, [L]*N, range(N))
  M_total = client.submit(sum,counts)
  end_time = time.time()
  piest = 4 * M_total.result() / (N * L)
  client.close()
  return piest, end_time - start_time


def pltres(workers, times, familyname):
  """Plots the execution times for different numbers of workers."""
  plt.figure(figsize=(8, 6))
  plt.plot(workers, times)
  plt.xlabel("Number of Workers")
  plt.ylabel("Execution Time (seconds)")
  plt.title("Execution Time vs. Number of Workers for " + familyname)
  plt.grid(True)
  plt.savefig(familyname + "_speedup.pdf")
  plt.close()


def measure(L, N, familyname):
  """Measures execution times for different numbers of workers."""
  max_workers = mp.cpu_count()
  for M in range(1, max_workers + 1):
     piest, time_taken = parpi(M, L, N)
     print(f"Workers: {M}, Estimated Pi: {piest:.4f}, Time: {time_taken:.4f} seconds")
  workers = range(1, max_workers + 1)
  pltres(workers, [time_taken for _ in workers], familyname)


def measureN(k, Nmax, familyname):
  """Measures execution times for different values of N while keeping k fixed."""
  workers = mp.cpu_count()
  N_values = [N for N in range(1, Nmax + 1) if k % N == 0]  # Ensure L is integer
  times = []
  for N in N_values:
    L = k // N
    piest, time_taken = parpi(workers, L, N)
    times.append(time_taken)
  pltres(N_values, times, familyname)


if __name__ == '__main__':
    L = 100000  # Number of (x, y) pairs
    N = 1000  # Number of realizations
    k = N * L  # Fixed k value for measureN

    # Run measure function with different worker numbers
    measure(L, N, "fixed_N")

    # Run measureN function with different N values while keeping k fixed
    measureN(k, 20, "fixed_k")  # Adjust Nmax as needed

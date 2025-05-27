import time
import matplotlib.pyplot as plt
import os
from graph_generator import GraphGenerator
from graph_operations import GraphOperations

class Benchmark:
    
    def __init__(self):
        self.generator = GraphGenerator()
    
    def run_all_tests(self):
        print("Running benchmark tests...")
        
        self.test_hamiltonian_graphs_30()
        self.test_hamiltonian_graphs_70()
        self.test_non_hamiltonian_graphs()
        
        print("Benchmark completed. Check generated plots.")
    
    def test_hamiltonian_graphs_30(self):
        print("Testing Hamiltonian graphs with 30% saturation...")
        
        sizes = list(range(11, 16))
        euler_times = []
        hamilton_times = []
        
        for n in sizes:
            print(f"Testing n={n}")
            
            graph = self.generator.generate_hamiltonian_graph(n, 30)
            operations = GraphOperations(graph)
            
            start_time = time.time()
            operations.find_euler_cycle()
            euler_time = time.time() - start_time
            euler_times.append(euler_time)
            
            start_time = time.time()
            operations.find_hamilton_cycle()
            hamilton_time = time.time() - start_time
            hamilton_times.append(hamilton_time)
        
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, euler_times, 'b-o', label='Euler cycle', linewidth=2)
        plt.plot(sizes, hamilton_times, 'r-o', label='Hamilton cycle', linewidth=2)
        plt.xlabel('Number of vertices (n)')
        plt.ylabel('Time (seconds)')
        plt.title('Algorithm performance - Hamiltonian graphs (30% saturation)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('hamiltonian_30_benchmark.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Saved: hamiltonian_30_benchmark.png")
    
    def test_hamiltonian_graphs_70(self):
        print("Testing Hamiltonian graphs with 70% saturation...")
        
        sizes = list(range(11, 16))
        euler_times = []
        hamilton_times = []
        
        for n in sizes:
            print(f"Testing n={n}")
            
            graph = self.generator.generate_hamiltonian_graph(n, 70)
            operations = GraphOperations(graph)
            
            start_time = time.time()
            operations.find_euler_cycle()
            euler_time = time.time() - start_time
            euler_times.append(euler_time)
            
            start_time = time.time()
            operations.find_hamilton_cycle()
            hamilton_time = time.time() - start_time
            hamilton_times.append(hamilton_time)
        
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, euler_times, 'b-o', label='Euler cycle', linewidth=2)
        plt.plot(sizes, hamilton_times, 'r-o', label='Hamilton cycle', linewidth=2)
        plt.xlabel('Number of vertices (n)')
        plt.ylabel('Time (seconds)')
        plt.title('Algorithm performance - Hamiltonian graphs (70% saturation)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('hamiltonian_70_benchmark.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Saved: hamiltonian_70_benchmark.png")
    
    def test_non_hamiltonian_graphs(self):
        print("Testing non-Hamiltonian graphs with 50% saturation...")
        
        sizes = list(range(11, 21))
        hamilton_times = []
        
        for n in sizes:
            print(f"Testing n={n}")
            
            graph = self.generator.generate_non_hamiltonian_graph(n)
            operations = GraphOperations(graph)
            
            start_time = time.time()
            operations.find_hamilton_cycle()
            hamilton_time = time.time() - start_time
            hamilton_times.append(hamilton_time)
        
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, hamilton_times, 'r-o', label='Hamilton cycle', linewidth=2)
        plt.xlabel('Number of vertices (n)')
        plt.ylabel('Time (seconds)')
        plt.title('Algorithm performance - Non-Hamiltonian graphs (50% saturation)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('non_hamiltonian_benchmark.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("Saved: non_hamiltonian_benchmark.png")
    
    def measure_time(self, func):
        start_time = time.time()
        result = func()
        end_time = time.time()
        return result, end_time - start_time
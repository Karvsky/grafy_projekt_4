#!/usr/bin/env python3
import sys
import argparse
from graph_generator import GraphGenerator
from graph_operations import GraphOperations
from benchmark import Benchmark

def main():
    parser = argparse.ArgumentParser(description='Graph algorithms with backtracking')
    parser.add_argument('--hamilton', action='store_true', help='Generate Hamiltonian graph')
    parser.add_argument('--non-hamilton', action='store_true', help='Generate non-Hamiltonian graph')
    parser.add_argument('--benchmark', action='store_true', help='Run benchmark tests')
    
    args = parser.parse_args()
    
    if args.benchmark:
        benchmark = Benchmark()
        benchmark.run_all_tests()
        return
    
    if not args.hamilton and not args.non_hamilton:
        print("Use --hamilton or --non-hamilton argument")
        return
    
    if args.hamilton:
        nodes = int(input("nodes> "))
        if nodes <= 10:
            print("Number of nodes must be greater than 10")
            return
        
        saturation = int(input("saturation> "))
        if saturation not in [30, 70]:
            print("Saturation must be 30 or 70")
            return
        
        generator = GraphGenerator()
        graph = generator.generate_hamiltonian_graph(nodes, saturation)
        
    elif args.non_hamilton:
        nodes = int(input("nodes> "))
        generator = GraphGenerator()
        graph = generator.generate_non_hamiltonian_graph(nodes)
    
    operations = GraphOperations(graph)
    
    while True:
        print("\nChoose operation:")
        print("1. Print graph")
        print("2. Find Euler cycle")
        print("3. Find Hamilton cycle")
        print("4. Exit")
        
        choice = input("Your choice> ")
        
        if choice == '1':
            operations.print_graph()
        elif choice == '2':
            euler_cycle = operations.find_euler_cycle()
            if euler_cycle:
                print(f"Euler cycle: {' -> '.join(map(str, euler_cycle))}")
            else:
                print("No Euler cycle found")
        elif choice == '3':
            hamilton_cycle = operations.find_hamilton_cycle()
            if hamilton_cycle:
                print(f"Hamilton cycle: {' -> '.join(map(str, hamilton_cycle))}")
            else:
                print("No Hamilton cycle found")
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
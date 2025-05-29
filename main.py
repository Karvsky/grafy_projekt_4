#!/usr/bin/env python3
import sys, os
import argparse
from graph_generator import GraphGenerator
from graph_operations import GraphOperations
from benchmark import Benchmark
from graph_visualization import export_to_tikz

os.system('cls' if os.name=='nt' else 'clear')  

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
        while True:
            try:
                nodes = int(input("nodes> "))
                if nodes <= 10:
                    print("Number of nodes must be greater than 10")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                saturation = int(input("saturation> "))
                if saturation in [30, 70]:
                    break
                print("Saturation must be 30 or 70")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        generator = GraphGenerator()
        graph = generator.generate_hamiltonian_graph(nodes, saturation)
        export_to_tikz(graph, filename="output_graph.tex")
        print("TikZ saved to output_graph.tex")
        
    elif args.non_hamilton:
        while True:
            try:
                nodes = int(input("nodes> "))
                if nodes > 1:
                    break
                print("Nodes must be above 1")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        generator = GraphGenerator()
        graph = generator.generate_non_hamiltonian_graph(nodes)
        export_to_tikz(graph, filename="output_graph.tex")
        print("TikZ saved to output_graph.tex")
    
    operations = GraphOperations(graph)
    os.system('cls' if os.name=='nt' else 'clear')  

    while True:
        print("Choose operation:")
        print("1. Print graph")
        print("2. Find Euler cycle")
        print("3. Find Hamilton cycle")
        print("4. Exit")
        
        choice = input("Your choice> ")
        os.system('cls' if os.name=='nt' else 'clear')  

        if choice == '1':
            operations.print_graph()
        elif choice == '2':
            euler_cycle = operations.find_euler_cycle()
            if euler_cycle:
                print(f"Euler cycle: {' -> '.join(map(str, euler_cycle))}\n")
            else:
                print("No Euler cycle found\n")
        elif choice == '3':
            hamilton_cycle = operations.find_hamilton_cycle()
            if hamilton_cycle:
                print(f"Hamilton cycle: {' -> '.join(map(str, hamilton_cycle))}\n")
            else:
                print("No Hamilton cycle found\n")
        elif choice == '4':
            break
        else:
            print("Invalid choice\n")

if __name__ == "__main__":
    main()
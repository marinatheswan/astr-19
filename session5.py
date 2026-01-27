import numpy as np

def generate_sin_table():
    x_values = np.linspace(0, 2 * np.pi, 1000)
    sin_values = np.sin(x_values)
    
    print(f"{'x':>10} | {'sin(x)':>10}")
    print("-" * 25)
    
    for x, s in zip(x_values, sin_values):
        print(f"{x:10.6f} | {s:10.6f}")

def main():
    generate_sin_table()

if __name__ == "__main__":
    main()
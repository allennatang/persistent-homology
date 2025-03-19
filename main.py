import numpy as np
from ripser import ripser
from persim import plot_diagrams

def main():
    data = np.random.random((100,2))
    diagrams = ripser(data)['dgms']
    plot_diagrams(diagrams, show=True)

if __name__ == "__main__":
    main()
import os
from posixpath import dirname


def main():
    
    print(os.path.dirname("./output/file.txt"))

    # if not os.path.exists('output/run22/lois/file.csv'):
    #     os.makedirs('output/run22/lois/file.csv')

main()
    
import csv
from time import perf_counter
path = (r"C:\Users\MuratDizdar\Downloads\4000-most-common-english-words-csv.csv")

word_list = []

def bubble_sort(words):
    '''Write your code here!'''
    pass

def selection_sort(words):
    '''Write your code here!'''
    pass

def insertion_sort(words):
    '''Write your code here!'''
    pass


def main():
    load_list(path)
    
    time = perf_counter()
    bubble_sort(word_list)
    print("Bubble sort completed in", perf_counter() - time)
    
    time = perf_counter()
    selection_sort(word_list)
    print("Selection sort completed in", perf_counter() - time)
    
    time = perf_counter()
    insertion_sort(word_list)
    print("Insertion sort completed in", perf_counter() - time)

    
def load_list(csv_file):
    try:
        with open(csv_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            # Assuming the 'Word' column is in the first position (index 0)
            for row in reader:
                word_list.append(row[0])    
        print("Words loaded successfully!")
        print("Words List:", word_list)
    except FileNotFoundError:
        print(f"File '{csv_file}' not found.")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()


"""
This is my first project which will be documented later
"""

#Task -
# Open a file from the web
# iterate over the file
# create a list of words from the file
# iterate over new list
import sys


def fetch_words(g):
    """
    Fetch a list of words from a file
    :param g: url address of a encoded file
    :return: nothing
    """
    from urllib.request import urlopen
    with urlopen(g) as story:
        story_words = []
        for line in story:
            # print(line.decode('utf-8'))
            line_rec = line.decode('utf-8').split()
            for word in line_rec:
                story_words.append((word))
    for word in story_words:
        print(word)
    print("The file has: ", len(story_words), " words")

def main(g):
    fetch_words(g)

if __name__ == '__main__':
    # g = r'file:C:\Users\theld\OneDrive\Documents\const.txt'
    url = sys.argv[1]
    main(url)
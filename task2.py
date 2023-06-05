import re

class Word:
    def __init__(self, word):
        self.word = word
        self.files = set()

    def add_file(self, file_index):
        self.files.add(file_index)

    def __str__(self):
        file_indices = ', '.join(str(file_index) for file_index in self.files)
        return f"{self.word}: {file_indices}"

class LinkedListNode:
    def __init__(self, file_name):
        self.file_name = file_name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, file_name):
        if not self.head:
            self.head = LinkedListNode(file_name)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = LinkedListNode(file_name)

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.file_name)
            current = current.next
        return ', '.join(elements)

class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_word(self, word, file_name):
        if word in self.index:
            self.index[word].append(file_name)
        else:
            new_word = Word(word)
            new_word.add_file(file_name)
            self.index[word] = LinkedList()
            self.index[word].append(file_name)

    def __str__(self):
        elements = []
        for word, linked_list in self.index.items():
            elements.append(f"{word}: {str(linked_list)}")
        return '\n'.join(elements)

class Text:
    def __init__(self, inverted_index):
        self.inverted_index = inverted_index

    def parse_text_file(self, file_path, file_name):
        with open(file_path, 'r') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
            for word in words:
                word = word.lower()
                self.inverted_index.add_word(word, file_name)

def main():
    inverted_index = InvertedIndex()
    file_paths = [('1.txt', '1.txt'), ('2.txt', '2.txt')]
    db_file_path = 'db.txt'

    for file_path, file_name in file_paths:
        text = Text(inverted_index)
        text.parse_text_file(file_path, file_name)

    with open(db_file_path, 'w') as file:
        file.write(str(inverted_index))

if __name__ == '__main__':
    main()

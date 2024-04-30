def read_lines(book_path: str) -> str:
    with open(book_path) as file:
        file_contents = file.read()

    return file_contents


def word_count(content: str) -> int:
    words = content.split()
    return len(words)


def main():
    book = "books/frankenstein.txt"
    book_content = read_lines(book)
    words = word_count(book_content)
    print(f"This book has {words} words")


if __name__ == "__main__":
    main()

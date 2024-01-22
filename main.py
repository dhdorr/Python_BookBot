
if __name__ == '__main__':
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        f.close()
        print(len(file_contents.split()), " words found in the document")
        letters_dict = {}
        test = list(file_contents.lower())
        for l in sorted(test):
            if l.isalpha():
                if l in letters_dict:
                    letters_dict[l] += 1
                else:
                    letters_dict[l] = 1
        
        for l in letters_dict:
            print(f"The '{l}' character was found {letters_dict[l]} times")

    print("--- End report ---")

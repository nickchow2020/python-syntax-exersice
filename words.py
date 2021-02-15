def print_upper_words(words,start_with):
    """
        collect a words list and print out only the prefix
        charactor that match a specific charactor
    """
    for word in words:
        for star in start_with:
            if word.startswith(star):
                print(word.upper())





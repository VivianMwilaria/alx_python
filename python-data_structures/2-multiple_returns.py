def multiple_returns(sentence):
    # Check if the sentence is empty
    if len(sentence) == 0:
        # If empty, return a tuple with length None and first character None
        return (None, None)
    else:
        # If not empty, return a tuple with length of the string and its first character
        return (len(sentence), sentence[0])

    
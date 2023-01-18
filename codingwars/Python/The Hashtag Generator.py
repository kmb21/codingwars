def generate_hashtag(s):
    final = "#"
    split_s = s.split()
    for item in split_s:
        final += item.capitalize() 
    if len(final)>140:
        return False
    elif final == "#":
        return False
    else:
        return final
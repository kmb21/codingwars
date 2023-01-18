def to_camel_case(text):
    camel_case = ""
    if "-" not in text:
        dash  = text.split("_")
    elif "_" not in text:
        dash = text.split("-")
    else:
        text = text.replace('-', '_')
        dash = text.split("_")
    for number in range(1, len(dash)):
        dash[number] = dash[number].capitalize()
    for item in dash:
        camel_case += item
    return camel_case
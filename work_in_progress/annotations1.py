
def get_type_line(source):

    type_pattern = re.compile("# type:\\ ignore(\\[[a-zA-Z-]+\\])?$")


    if len(type_lines) == 0:
        # Catch common typo patterns like extra spaces, typo in 'ignore', etc.
        wrong_type_pattern = re.compile("#[\t ]*type[\t ]*(?!: ignore(\\[.*\\])?$):")
        wrong_type_lines = list(
            filter(lambda line: wrong_type_pattern.search(line[1]), lines)
        )

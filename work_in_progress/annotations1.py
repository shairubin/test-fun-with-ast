
def get_type_line(source):

    type_pattern = re.compile("# type:\\ ignore(\\[[a-zA-Z-]+\\])?$")

    if len(type_lines) == 0:
        wrong_type_pattern = re.compile("#[\t ]*type[\t ]*(?!: ignore(\\[.*\\])?$):")

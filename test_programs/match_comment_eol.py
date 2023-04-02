def MatchCommentEOL(self, string, remove_comment=False):
    remaining_string = string
    comment = ''
    full_line = re.match(r'(.*)(#.*)', string)
    if full_line:
        comment = full_line.group(2)
    if comment:
        self.end_of_line_comment = comment
    if remove_comment and full_line:
        remaining_string = full_line.group(1)
    return remaining_string


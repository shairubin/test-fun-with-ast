

class Journal:

    @classmethod
    def from_journal(cls, other: "Journal") -> "Journal":
        """Creates a new journal by copying configuration and entries from
        another journal object"""
        new_journal = cls(other.name, **other.config)

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text: str) -> None:
        self.count += 1
        self.entries.append(f'{self.count}: {text}')
    
    def remove_entry(self, pos: int) -> None:
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)


class PersistData:
    @staticmethod
    def save_to_file(journal: Journal, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(journal))

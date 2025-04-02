from dataclasses import dataclass

from model.studente import Student


@dataclass
class Course:
    codins: str
    crediti: int
    nome: str
    pd: int
    # studenti: list[Student] = None  #lazy initialization
    # matricole: list[str] = None


    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):  # per metterlo in memoria
        return hash(self.codins)

    def __str__(self):
        return f"{self.nome} ({self.codins}) - {self.crediti} CFU"
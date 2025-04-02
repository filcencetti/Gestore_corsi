from dataclasses import dataclass


@dataclass
class Student:
    matricola: int
    cognome: str
    nome: str
    CDS: str
    # corsi: list[Course] = None
    # codins: list[str] = None

    def __eq__(self, other):
        return self.matricola == other.matricola

    def __hash__(self):  # per metterlo in memoria
        return hash(self.matricola)

    def __str__(self):
        return f"{self.cognome} {self.nome} ({self.matricola}) - {self.CDS}"
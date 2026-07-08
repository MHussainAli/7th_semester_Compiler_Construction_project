from dataclasses import dataclass
@dataclass
class Token:
    type: str
    lexeme: str
    line: int
    column: int
    def __str__(self):
        return f"{self.type:<14} {self.lexeme:<12} ({self.line},{self.column})"

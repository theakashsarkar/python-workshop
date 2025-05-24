from dataclasses import dataclass, field

@dataclass
class ClubMemeber:
    name: str
    guests: field(default_factory=list)
    athlete: bool = field(default=False, repr=False)

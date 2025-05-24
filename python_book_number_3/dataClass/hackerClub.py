from dataclasses import dataclass, field

@dataclass
class ClubMemeber:
    name: str
    guests: list[str] = field(default_factory=list)
    athlete: bool = field(default=False, repr=False)

@dataclass
class HackerClubMember(ClubMemeber):
    all_handle = set()
    handle: str = ''

    def __post_init__(self):
        cls = self.__class__
        if self.handle == '':
            self.handle = self.name.split()[0]
        if self.handle in cls.all_handle:
            msg = f"handle {self.handle!r} already exists."
            raise ValueError(msg)
        cls.all_handle.add(self.handle)

# print(HackerClubMember.__doc__)
# hackerClubMember = HackerClubMember('akash', 'myName')
# print(hackerClubMember)
# hackerClubMember2 = HackerClubMember('akash','myName','akash')
# hackerClubMember2.handle = 'akash2'
# hackerClubMember2.athlete = True
# hackerClubMember2 = HackerClubMember('akash', ['akash', 'myname', 'first'],'akash')
# hackerClubMember2.guests.append('akash2')
# hackerClubMember2.guests.append('akash3')
hackerClub = HackerClubMember('akash', 'akash1', 'akash')
hackerClub.name = 'ami'
hackerClub.guests.append('akash')
print(hackerClub)

# class BadUser:
#     def __init__(self, name: str, tags = []):
#         self.name = name
#         self.tags = tags
# bu1 = BadUser('akash')
# bu2 = BadUser('akash2')
# bu1.tags.append('admin')
# print(bu2.tags)
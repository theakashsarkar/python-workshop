from typing import TypeVar, Tuple, Mapping, Dict, Generic, Optional
T = TypeVar('T')

def get_coordinates() -> Tuple[float, float]:
    return (23.5, 45.6)

def get_user_info() -> Tuple[str, int, bool]:
    return ("John", 30, True)

class Cache(Generic[T]):
    def __init__(self) -> None:
        self._data: Dict[str, T] = {}
    
    def set(self, key: str, value: T) -> None:
        self._data[key] = value

    def get(self, key: str) -> Optional[T]:
        return self._data.get(key)

def process_config(settings: Mapping[str, str]) -> None:
    for key, value in settings.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    point = get_coordinates()
    print(f"Location: {point[0]}, {point[1]}")
    user_info = get_user_info()
    name, age, active = user_info

    int_cache = Cache[int]()
    int_cache.set("key", 42)

    config = {"timeout": 30, "retries": 3}
    process_config(config)
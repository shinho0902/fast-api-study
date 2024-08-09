# 타입 추가하기 


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age

print(get_name_with_age("john", "doe"))


from typing import List
# items 는 리스트 인데, 리스트 원소 타입들은 str 이다.
def process_items(items: List[str]): 
    for item in items:
        print(item.capitalize)


from typing import Set, Tuple
# items_t 는 튜플 인데, 튜플 원소 타입들은 int, int, str 이다.
# items_s 는 셋 인데, 셋 원소 타입은 bytes 이다.
def process_items(items_t: Tuple[int, int, str], items_s: Set[bytes]):
    return items_t, items_s



from typing import Dict

# prices 는 딕셔너리인데, 딕셔너리의 키-밸류는 str-float 이다.
def process_items(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)




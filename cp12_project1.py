def print_baggage_items(*items, **item_with_count):
    print("# 단일 품목")
    for i in items:
        print(i)
    print("# 다중 품목")
    for i in item_with_count.keys():
        print(f"{i} {item_with_count[i]} 개")

print_baggage_items('laptop', 'camera', socks=8, pants=2, shirts=4)

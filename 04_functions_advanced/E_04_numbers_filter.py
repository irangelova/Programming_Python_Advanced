def even_odd_filter(**kwargs):
    results = {}
    for key, value in kwargs.items():
        results[key] = []
        if key == "even":
            for el in value:
                if int(el) % 2 == 0:
                    results[key].append(int(el))
            #kwargs[key] = [x for x in value if x % 2 == 0]
        elif key == "odd":
            for el in value:
                if int(el) % 2 != 0:
                    results[key].append(int(el))
            #kwargs[key] = [x for x in value if x % 2 != 0]

    return dict(sorted(results.items(), key=lambda x: -len(x[1])))
    #return results


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))


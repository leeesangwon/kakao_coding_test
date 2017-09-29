class cache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache_list = list()

    def find(self, in_val):
        if self.cache_size == 0:
            return self.miss_time()
        if in_val in self.cache_list:
            self.hit(in_val)
            return self.hit_time()
        else:
            self.miss(in_val)
            return self.miss_time()

    def hit_time(self):
        return 1

    def miss_time(self):
        return 5

    def hit(self, in_val):
        self.cache_list.remove(in_val)
        self.cache_list.append(in_val)

    def miss(self, in_val):
        if len(self.cache_list) == self.cache_size:
            self.cache_list.pop(0)
        self.cache_list.append(in_val)


def main():
    cache_size = int(input('cacheSize: '))
    assert (cache_size >= 0 & cache_size <= 30), "0 <= cacheSize <= 30"
    cities = input("cities(ex. [city1, city2, ..., cityN]): ").strip()
    assert (cities[0] == '[') & (cities[-1] == ']'), 'Input is not valid format'
    cities = list(map(str.lower, ''.join(cities[1:-1].split()).split(',')))
    assert len(cities) <= 100000, "too many cities"

    cities_cache = cache(cache_size)
    run_time = 0
    for city in cities:
        run_time += cities_cache.find(city)

    print(run_time)


if __name__ == '__main__':
    main()

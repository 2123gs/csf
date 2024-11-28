def fully_associative_cache(cache_size, memory_accesses):
    cache = []
    hits = 0

    for access in memory_accesses:
        if access in cache:
            hits += 1
        else:
            if len(cache) == cache_size:
                cache.pop(0)
            cache.append(access)

    print(f"Cache hits: {hits}")
    print(f"Cache misses: {len(memory_accesses) - hits}")

cache_size = 4
memory_accesses = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
fully_associative_cache(cache_size, memory_accesses)
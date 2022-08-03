from circularDoublyLinkedList import *

def do_sim(cache_slots):

    cache_hit = 0
    tot_cnt = 0
    cache = CircularDoublyLinkedList()

    data_file = open("linkbench_short.trc")

    for line in data_file.readlines():
        lpn = line.split()[0]
        tot_cnt += 1

        if not lpn in cache.get(lpn):
            if cache.size() < cache_slots:
                cache.append(lpn)
            else:
                cache.pop(0)
                cache.append(lpn)
        else:
            cache_hit += 1
            cache.pop(cache.index(lpn))
            cache.append(lpn)

        # do programming here!
        

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":

    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)

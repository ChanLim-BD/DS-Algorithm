from itertools import combinations

def calculate_min_movies(n, m, friends, movies):
    all_movies = set()
    for movie_list in movies:
        all_movies.update(movie_list)
    
    if len(all_movies) < n:  # 모든 영화의 수가 n보다 작다면 모든 친구가 보고 싶은 영화를 볼 수 없으므로 -1을 반환합니다.
        return -1
    
    for i in range(1, m + 1):
        for selected_movies in combinations(movies, i):
            selected_movies = sum(selected_movies, [])  # combinations로 선택된 영화들을 하나의 리스트로 만듭니다.
            
            if set(selected_movies) == set(friends):  # 선택된 영화들이 모든 친구가 보고 싶은 영화와 동일하다면 해당 선택된 영화들의 수를 반환합니다.
                return i
    
    return -1  # 가능한 조합이 없을 경우 -1을 반환합니다.

n = 10
m = 7
friends = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
movies = [["a", "c", "d", "h", "i", "j"], ["a", "d", "i"], ["a", "c", "f", "g", "h", "i", "j"], ["b", "d", "g"], ["b", "c", "f", "h", "i"], ["b", "e", "g", "j"], ["b", "c", "g", "h", "i"]]

result = calculate_min_movies(n, m, friends, movies)
print(result)

def main():
    # Step 2 - Create a complex data structure
    data = {
        'full_name': 'Rajat Patel',
        'student_id': 10327381,
        'pizza_toppings': ['RED ONIONS', 'GREEN BELL PEPPERS', 'MUSHROOMS'],
        'movies': [
            {'title': 'inception', 'genre': 'sci-fi'},
            {'title': 'the shawshank redemption', 'genre': 'Drama'}
        ]
    }

    # Step 3 - Add another movie to the data structure
    data['movies'].append({'title': 'the godfather', 'genre': 'crime'})
    
# Step 4 - Function that prints student name and ID	
    def print_student_name_and_id(data):
        full_name = data['full_name']
        first_name = full_name.split()[0]
        print(f"My name is {full_name}, but you can call me sir {first_name}.")
        print(f"My student ID is {data['student_id']}.")
        print()
        return
    
# Step 5 - Function that adds pizza toppings to data structure
    def add_pizza_toppings(data, toppings):
        data['pizza_toppings'].extend(toppings)
        data['pizza_toppings'] = sorted(data['pizza_toppings'])
        data['pizza_toppings'] = [topping.lower() for topping in data['pizza_toppings']]
        return

# Step 6 - Function that prints bullet list of pizza toppings
    def print_pizza_toppings(data):
        print("My favourite pizza toppings are:")
        for topping in data['pizza_toppings']:
            print(f"- {topping}")
        print()        
        return

# Step 7 - Function that prints comma-separated list of movie genres
    def print_movie_genres(data):
        genres = [movie['genre'] for movie in data['movies']]
        if len(genres) >1:
            genres_text = ', '.join(genres[:-1]) + ', and ' + genres[-1]
        else:
            genres_text = genres[0]
        print(f"I like to watch {genres_text} movies.")
        print()        
        return 

# Step 8 - Function that prints comma-separated list of movie titles
    def print_movie_titles(movies):
        titles = [movie['title'].title() for movie in movies]
        if len(titles) >1:
            titles_text = ', '.join(titles[:-1]) + ', and ' + titles[-1]
        else:
            titles_text = titles[0]
        print(f"Some of my favourite movies are {titles_text}!")
        return
    
    print_student_name_and_id(data)
    print_pizza_toppings(data)

    new_toppings = ('JALAPENOS', 'TOMATOES')
    add_pizza_toppings(data,new_toppings)

    print_pizza_toppings(data)
    print_movie_genres(data)
    print_movie_titles(data['movies'])

if __name__ == '__main__':
    main()
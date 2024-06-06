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
        first_name = full_name.split([0])
        print(f"My name is {full_name}, but you can call me Mr. {first_name}.")
        print(f"My student ID is {data['student_id']}.")
        print()
        return
    
# Step 5 - Function that adds pizza toppings to data structure
    def add_pizza_toppings(data, toppings):
        data['pizza_toppings'].extend(toppings)
        data['pizza_toppings'] = sorted(data['pizza_topings'])
        data['pizza_toppings'] = [toppings.lower() for topping in data['pizza_toppings']]
        return

# Step 6 - Function that prints bullet list of pizza toppings
    def print_pizza_toppings(about_me):
        
        return

# Step 7 - Function that prints comma-separated list of movie genres
    def print_movie_genres(about_me):
        
        return 

# Step 8 - Function that prints comma-separated list of movie titles
    def print_movie_titles(movie_list):
        
        return
    print_student_name_and_id(data)
    print_pizza_toppings(data)

    new_toppings = ('JALAPENOS', 'TOMATOES')
    add_pizza_toppings(data,new_toppings)

if __name__ == '__main__':
    main()


def give_ratings(scores_file):
    """reads file and returns alphabetized ratings of restaurants"""
    food_grades = {}
    restaurant_ratings = open(scores_file)

    for line in restaurant_ratings:
        line.rstrip()
        item_list = line.split(':')
        restaurant = item_list[0]
        grade = item_list[1]
        food_grades[restaurant] = grade

    # sort the keys
    sorted_restaurants = sorted(food_grades)

    # for each key in the sorted keys:
    for restaurant in sorted_restaurants:

        alphabetized_restaurants = food_grades.keys()
        alphabetized_grades = food_grades.values()
        print alphabetized_restaurants, "has a rating of", alphabetized_grades





# # make a list of each line, then sort that list
#         line.rstrip()
#         # make a list, then split each item 
#         item_list = line.split(':')
#         key_list = restaurant[0]
#         key_list.sort()

#         for item in item_list:
#             restaurant = item_list[0]
#             grade = item_list[1]
#             print restaurant, grade

#             # key = token[0]
#             # value = token[1] 
give_ratings('scores.txt')

    # scores_file.close()
    # return sorted



    # for line in data_file:
    #     line.rstrip()
    #     word_list = line.split(' ')
    #     for word in word_list:
    #         # get method returns a default value associated with key 
    #         # by setting it to 0 
    #         # add one each time word appears through loop
    #         word_counts[word] = word_counts.get(word, 0) + 1

    # print word_counts
    # return

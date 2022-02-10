# Import dependencies
import pandas as pd
import pickle

def predict(form_data):
    # Convert ImmutableMultiDict to list of lists
    data_list = list(form_data.lists())

    # Create variables for form info
    title = data_list[0][1][0]
    description = data_list[1][1][0]
    content_rating = data_list[2][1][0]
    runtime = pd.to_numeric(data_list[3][1][0])
    genres = data_list[4][1]

    # Create dictionary to add preprocessed input data
    input_data = {}

    # Add numeric features
    input_data["runtime"] = runtime
    input_data["total_genres"] = len(genres)
    input_data["title_word_count"] = len(title.split())
    input_data["title_char_count"] = len(title)
    input_data["info_word_count"] = len(description.split())
    input_data["info_char_count"] = len(description)

    # Add genre features
    genres_list = ['Drama', 'Comedy', 'Action & Adventure',
        'Mystery & Suspense', 'Art House & International', 'Romance', 'Horror',
        'Science Fiction & Fantasy', 'Classics', 'Kids & Family', 'Documentary',
        'Musical & Performing Arts', 'Special Interest', 'Animation', 'Western',
        'Television', 'Sports & Fitness', 'Cult Movies', 'Gay & Lesbian',
        'Faith & Spirituality', 'Anime & Manga']
    for genre in genres_list:
        if genre in genres:
            input_data[genre] = 1
        else:
            input_data[genre] = 0

    # Add content rating features
    rating_list = ['content_rating_G', 'content_rating_NC17',
        'content_rating_NR', 'content_rating_PG', 'content_rating_PG-13',
        'content_rating_R']
    for rating in rating_list:
        if rating.split('_')[2] == content_rating:
            input_data[rating] = 1
        else:
            input_data[rating] = 0

    # Convert dictionary to DataFrame
    input_data_df = pd.DataFrame(input_data, index=[0])

    # Reorder columns to match ML model data
    columns=['runtime', 'content_rating_G', 'content_rating_NC17',
        'content_rating_NR', 'content_rating_PG', 'content_rating_PG-13',
        'content_rating_R', 'Drama', 'Comedy', 'Action & Adventure',
        'Mystery & Suspense', 'Art House & International', 'Romance', 'Horror',
        'Science Fiction & Fantasy', 'Classics', 'Kids & Family', 'Documentary',
        'Musical & Performing Arts', 'Special Interest', 'Animation', 'Western',
        'Television', 'Sports & Fitness', 'Cult Movies', 'Gay & Lesbian',
        'Faith & Spirituality', 'Anime & Manga', 'total_genres',
        'title_word_count', 'title_char_count', 'info_word_count',
        'info_char_count']
    input_data_df = input_data_df[columns]

    # Load the saved model
    loaded_model = pickle.load(open("finalized_model.pkl", 'rb'))

    # Make predition from input data
    prediction = loaded_model.predict(input_data_df)[0]

    return prediction
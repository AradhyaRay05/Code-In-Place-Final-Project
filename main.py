from ai import call_gpt 

def get_genre():
    print("Choose a genre:")
    print("1. Adventure\n2. Horror\n3. Comedy\n4. Fantasy")
    choice = input("Enter your choice (1-4): ")
    genres = {'1': 'Adventure', '2': 'Horror', '3': 'Comedy', '4': 'Fantasy'}
    return genres.get(choice, 'Adventure')

def main():
    print("Welcome to the Thought-to-Story Generator 📝")

    thoughts = input("Enter your thoughts: ")
    while True:
        more = input("Do you want to add more thoughts? (yes/no): ").lower()
        if more == 'yes':
            extra = input("Add more thoughts: ")
            thoughts += " " + extra
        else:
            break

    genre = get_genre()
    lines = int(input("How many lines should the story be?: "))

    mood = input("What mood should the story have? (e.g., happy, dark, mysterious, funny): ")
    main_character = input("What is the main character’s name?: ")
    ending = input("Preferred ending? (happy, sad, cliffhanger, open): ")
    dialogue = input("Should the story have conversations/dialogue? (yes/no): ")
    language_style = input("Language style? (formal, casual, poetic, simple): ")

    prompt = f" Write a {genre.lower()} story in about {lines} lines based on this user thought: {thoughts}.The story should have a {mood} mood, with main character named {main_character}.It includes dialogue: {dialogue}.Use {language_style} language.End the story with a {ending} ending."

    print("\nGenerating your story \n")
    story = call_gpt(prompt)
    print("Here's your story:\n")
    print(story)

if __name__ == "__main__":
    main()

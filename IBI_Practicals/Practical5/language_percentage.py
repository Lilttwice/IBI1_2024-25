# Libraries needed for this code
import matplotlib.pyplot as plt
import matplotlib
print(matplotlib.get_backend())


# make dictionary to recode the usage percentage of programming languages
language_data = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
    }

# Variable to select a specific language (can be modified)
selected_language = "Python"  # Modify this to check different languages

# Retrieve popularity of the selected language
popularity = language_data.get(selected_language, "Language not found")

# Print the result
if isinstance(popularity, float):
    print(f"The popularity of {selected_language} is {popularity}%")
else:
    print(popularity)

# draw a bar chart to show the usage percentage of programming languages
# x-axis: programming languages
# y-axis: percentage of users
languages = list(language_data.keys())
percentages = list(language_data.values())

plt.bar(languages, percentages, color = "skyblue")
plt.xlabel('Programming Languages')
plt.ylabel('Users (percentage)')
plt.title('Usage Percentage of Programming Languages')
plt.show()


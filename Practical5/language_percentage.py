import matplotlib.pyplot as plt
import matplotlib
print(matplotlib.get_backend())


# create a dictionary recoding the usage percentage of programming languages
language_data = {
    "JavaScript": 62.3,
    "HTML": 52.9,
    "Python": 51,
    "SQL": 51,
    "TypeScript": 38.5
    }

# print the dictionary
print(language_data)

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


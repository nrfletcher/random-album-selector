import urllib.request

url = 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Albums/500'
file_name = 'wikipedia_page.html'

# Fetch the HTML content
with urllib.request.urlopen(url) as response:
    html_content = response.read()

# Save the HTML content to a file
with open(file_name, 'wb') as file:
    file.write(html_content)

print(f"HTML content has been saved to {file_name}")
import requests
from bs4 import BeautifulSoup
import openai

# Define the list of URLs
urls = [
]
# Initialize OpenAI API key
openai.api_key=''

# Initialize an empty string to store extracted data
extracted_data = ""
url=urls[0]
# Loop through the list of URLs

    # Send a request to the URL
response = requests.get(url)

    # Check if the request was successful (status code 200)
if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <div> element with id="primary" and class="content-area primary"
    content_div = soup.find('div', {'id': 'primary', 'class': 'content-area primary'})

        # Check if the element exists
    if content_div:
            # Extract the text or content within the <div> element
        content_text = content_div.get_text()
            
            # Send the extracted content to OpenAI to extract specific information
        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": content_text + "extract to me json data like this with only this property  Category: Air conditioner,Product Title: Price Product Description Product Features write only this no thing else"}]
            )

            # Append the extracted data to the result
        extracted_data += completion['choices'][0]['message']['content'] + "\n"
    else:
            print(f'The div with id "primary" and class "content-area primary" was not found on the page for URL: {url}')
else:
        print(f'Failed to retrieve the webpage for URL: {url}. Status code:', response.status_code)

with open('data.txt', 'a') as file:
    file.write(extracted_data)

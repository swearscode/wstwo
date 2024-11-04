from bs4 import BeautifulSoup
import json

# Path to your local HTML file
file_path = 'Books.html'

# Open and read the local HTML file
with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all product containers
products = soup.find_all('div', class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v2lk1billfaou72dkme0sb0jkg6 s-latency-cf-section puis-card-border')

# List to hold product data
product_data = []

# Loop through each product and extract the required information
for product in products:
    title = product.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')
    title_text = title.get_text(strip=True) if title else 'N/A'

    price = product.find('span', class_='a-price-whole')
    price_text = price.get_text(strip=True) if price else 'N/A'

    # Append the data to the list
    product_data.append({
        'title': title_text,
        'price': price_text
    })

# Save the data to a JSON file
with open('Products.json', 'w') as json_file:
    json.dump(product_data, json_file, indent=4)

print('Data has been scraped and saved to Products.json.')
"""
This code is specifically written to scrap data from the webpage:https://www.vviptravel.com/tours 

Written by Adriel
Only for the purpose of interviewing with STORICITY

"""

# VIP TRAVEL PARSER

from bs4 import BeautifulSoup
import requests

# 0. Prepare a file that we will write results on
korea_group_tours = open('korea_group_tours.csv', 'w')
korea_group_tours.write(f'\nTOUR TITLE\tTOUR RATING\tTOUR PRICE\tPICTURE URL\tMORE DETAILS AT\n\n')

# 1. Fetching the "Korea Group Tours" page
source = requests.get('https://www.vviptravel.com/tours').text
soup = BeautifulSoup(source, 'html.parser')


# DEALING WITH PAGINATION

# 2. gathering pages' urls
pages = ['https://www.vviptravel.com/tours',]

pages_list = soup.find('ul', class_='page-numbers').find_all('li')

# we skip the first link (current page) and the last link (next)
for page in pages_list[1:-1]:
    page_url = page.a['href']
    pages.append(page_url)


# NOW WE VISIT EACH PAGE AND GATHER ITS INFORMATION

for page in pages:

    # 3. Visit the page and parse it
    page_source = requests.get(page).text
    page_soup   = BeautifulSoup(page_source, 'html.parser')
    
    # 4. Find a "ul" that contains all tours
    group_tours_wrapper = page_soup.find('ul', class_='products')

    # 5. Gather all tours in a list
    tours = group_tours_wrapper.find_all('li', class_='product')

    # 6. Collect information for each individual tour
    for tour in tours:
        # picture source (url)
        tour_picture = tour.find('div', class_='inside-wc-product-image').img['data-src']

        # tour title
        tour_title = tour.find('h2', class_='woocommerce-loop-product__title').text

        # tour rating (ex: 5.00)
        tour_rating = tour.find('div', class_='star-rating').strong.text

        # tour price (ex: ₩60,000 -> 60,000)
        tour_price = tour.find('span', class_='price').bdi.text[1:]

        # tour link for more info
        tour_details_link = tour.find('a', class_='button')['href']

        # 7. Write this information to our cvs file
        korea_group_tours.write(f'{tour_title}\t{tour_rating}\t{tour_price}\t{tour_picture}\t{tour_details_link}\n')
        
        # UNCOMMENT NEXT LINE TO SEE LIVE ACTION
        print(tour_title,'\n', tour_rating,'\n', tour_price,'\n', tour_picture,'\n', tour_details_link,'\n\n')

# 8. Finally close the file
korea_group_tours.close()
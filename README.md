# sample_crawler
A sample crawler for the webpage: https://www.vviptravel.com/tours written for the purpose of Interviewing with STORICITY

## THIS CRAWLER BASICALLY DOES THE FOLLOWING:
  1. Visit the page https://www.vviptravel.com/tours and parse its html using BeautifulSoup Libraly
  2. Because the page uses pagination, it first collects urls to all pages
  3. Visit each of the pages
  4. On each page extract the data for each tour listed
  5. Writes all this information to a csv file (located in the same directly as the script)

Requirements:
1. Python 3
2. BeautifulSoup 4 Libraly
3. Requests Libraly

Running the script
1. Open your terminal and navigate to the directly where the script is located
2. then type: python3 vip_travel_scrapper.py

# sample_crawler
A sample crawler for the webpage: https://www.vviptravel.com/tours written for the purpose of Interview with STORICITY

## THIS CRAWLER BASICALLY DOES THE FOLLOWING:
  1. Visit the page https://www.vviptravel.com/tours and parse its html using BeautifulSoup Libraly
  2. Because the page uses pagination, it first collects urls to all pages
  3. Visit each of the pages
  4. On each page extract the data for each tour listed
  5. Writes all this information to a csv file (located in the same directly as the script)

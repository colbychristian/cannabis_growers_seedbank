# cannabis_growers_seedbank
Data scraping spider to collect growing data on various cannabis strains

Scrapy spider that scrapes data from https://growdiaries.com/

Spider does not perfectly scrape data due to HTML inconsistencies between strain pages, some manual data cleaning is required. Spider also only captures first 20 breeders and 20 of their respective strains because of javascript enabled scrolling page element that uncovers more breeders and strains.

Future Work:
1. clean up data scraping on strain pages
2. capture all breeders and strains
3. Create application for strain analysis
4. Automate strain data refresh

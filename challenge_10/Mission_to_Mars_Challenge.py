
# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)
html = browser.html
mars_hemi_soup = soup(html , 'html.parser')


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
parent_elem = mars_hemi_soup.find_all('div', class_='description')

for elem in parent_elem:
    
# get title
    title = elem.find('h3').get_text()
#get link to website link for each image
    img_url_partial = elem.find('a').get('href')
    img_url_complete =url+img_url_partial
# visit each link, parse and use soup for each site opened.
    img_url_visit = browser.visit(img_url_complete)
    html = browser.html
    img_new_page_soup = soup(html, 'html.parser')
    # retrieve image url
    parent_elem_new_site = img_new_page_soup.find('div', class_='downloads')
    img_high_resol_href =  parent_elem_new_site.ul.li.select_one('a').get('href')
    img_url = url + img_high_resol_href

    browser_back = browser.back()
    
    #insert information in hemisphere
    hemisphere_image_urls.append({'img_url':img_url,'title':title})
    

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()




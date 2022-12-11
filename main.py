from requests import get
from bs4 import BeautifulSoup

# websites = ("google.com","airbnb.com","https://twitter.com","facebook.com","https://tictok.com")
#
# for website in websites:
#     if not website.startswith("https://") :
#         website = f"https://{website}"
#     print(website)

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    # print(len(jobs))
    for job_section in jobs:
        # print(job_section.find_all('li'))
        job_posts = job_section.find_all('li')
        job_posts.pop(1)
        for post in job_posts:
            anchors = post.find_all('a')
            # print(anchors)
            anchor = anchors[1]
            # print('href : ' + anchor['href'])
            company, kind, region = anchor.find_all('span', class_="company")
            # print(company, kind, region)
            title = anchor.find('span', class_='title')
            print(company, kind, region, title)
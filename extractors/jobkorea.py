from requests import get
from bs4 import BeautifulSoup

def extract_jobkorea_jobs(keyword):
    base_url = "https://www.jobkorea.co.kr/Search/?stext="

    response = get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        job_box = soup.find('div', class_="list-default")
        job_list = job_box.find_all('ul', class_="clear")
        for job_section in job_list:
            job_posts = job_section.find_all('li', class_="list-post")
            for post in job_posts:
                anchor = post.find('a')
                #print(f'######{anchor}\n')
                link = anchor['href']
                #print(f'link: {link}')
                company = anchor['title']
                #print(f'company: {company}')
                paragraph = post.find('p', class_="option")
                #print(f'$$$$$${paragraph}\n')
                location = paragraph.find('span', class_="long")
                #print(f'location: {location.string}')
                position_anchor_div = post.find('div', class_="post-list-info")
                position_anchor = position_anchor_div.find('a')
                position = position_anchor['title']
                #print(f'position:{position}')

                job_data = {
                    'link': f'https://www.jobkorea.co.kr/{link}',
                    'company': company,
                    'location': location.string.replace(",", " "),
                    'position': position.replace(",", " ")
                }
                
                results.append(job_data)
    return results
import datetime
import os
import shutil
import requests
from bs4 import BeautifulSoup

class ImageFolder:

    def __init__(self, keyword:str, num_images:int):
        self.keyword =keyword
        self.num_images = num_images
        self.creation_date = datetime.date.today()
        self.Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
        self.u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
        self._create_folder()
        self._scrap_images()
    
    def _create_folder(self):
        path = os.getcwd()
        folder_dir = os.path.join(path, self.keyword)
        if not os.path.isdir(folder_dir):
            os.mkdir(folder_dir)
            print(f'Image folder created at:\n{folder_dir}')
        else:
            print(f'The folder "{self.keyword}" already exists in directory:\n{folder_dir}')
        global image_folder
        image_folder = folder_dir
        
        

    def delete_folder(self, name_folder:str):
        path = os.getcwd()
        folder_dir = os.path.join(path, name_folder)
        if os.path.isdir(folder_dir):
            shutil.rmtree(folder_dir)
            print(f'Folder "{name_folder}" deleted.\nDirectory{folder_dir} removed')
        else:
            print(f'Folder "{name_folder}" does not exist')

    def _scrap_images(self):
        search_url = Google_Image + 'q=' + self.keyword
        response = requests.get(search_url, headers=u_agnt)
        html = response.text
        b_soup = BeautifulSoup(html, 'html.parser')
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
        count = 0
        imagelinks= []
        for res in results:
            try:
                link = res['data-src']
                imagelinks.append(link)
                count = count + 1
                if (count >= self.num_images):
                    break            
            except KeyError:
                continue 
        for i, imagelink in enumerate(imagelinks):
            response = requests.get(imagelink) 
            imagename = image_folder + '/' + self.keyword + str(i+1) + '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)

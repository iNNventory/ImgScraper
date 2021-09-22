# Image Scraper
This is a basic tool I made to download images from Google Images to build a dataset that can be used to train the NN algorithms I need for my final degree project.

Credits to [Anand Suresh](https://medium.com/@wwwanandsuresh/web-scraping-images-from-google-9084545808a2) for the base code.

## Installation
1.- Clone the repository
```command
git clone https://github.com/iNNventory/ImgScraper
```
2.- Install dependencies
```command
pip install -r requirements.txt
```
3.- Get Google Drive API credentials

1. Visit [Google Cloud Console](https://console.cloud.google.com/apis/dashboard) and create a new project
2. Enable Google Drive API
3. Configure the OAuth 2.0 consent screen for our particular use
   1. Select `Internal use`
   2. Input an application name
   3. Select a user support email
   4. Input a developer contact email
   5. Press "Save and continue" in the next steps
4. Create new credentials
   1. Select `OAuth ID client`
   2. Select `Web application` on the drop-down menu
   3. Input a name for the application
   4. In `JavaScript authorized origins` add `http://localhost:8080` 
   5. In `Authorized redirect URIs` add `http://localhost:8080/`
   6. Click on `Create`
5. Download the JSON with the credential of our API and save it on the project's root

4.- Create the shared drive in which you want to store the folder containing the scraped photos and create the folder

5.- Copy the last part of the shared drive's URL and paste it on the `.env`'s GDRIVE_TEAMDRIVE_ID variable

```url
https://drive.google.com/drive/u/0/folders/XXXXXXXXXXXXXX
``` 

6.- Copy the last part of the folder's URL that is inside the shared drive and paste it on the `.env`'s GDRIVE_FOLDER_ID variable
```url
https://drive.google.com/drive/u/0/folders/XXXXXXXXXXXXXX
``` 
## Usage
To run the application from the terminal, you just have to write the following command, changing the parameters to your will.
```command
python3 main.py photo_count query1 query_2 ... queryN
```
**Important**: instead of using spaces (\" \") in the search terms use an underscore (\"_\"), the program will automatically remove it for the search.
#### **Example**
```command
python3 main.py 3 allen_key screwdriver hammer
```
## Warning
If the Google Drive upload fails the image(s) will be stored in `~/photos/` and might become a heavy folder, so it is recommended to delete it.

## TODO
- [ ] Don't only upload content to shared folders
- [ ] Start photo count in name for each search term
- [ ] Help menu 
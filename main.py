import requests

# URLs for Zoom client downloads
urls = {
    # 'Windows': 'https://zoom.us/client/latest/ZoomInstaller.exe',
    # 'MacOS': 'https://zoom.us/client/latest/Zoom.pkg',
    'Linux': 'https://zoom.us/client/latest/zoom_amd64.deb'
}

# Download executable files for each operating system
for os, url in urls.items():
    response = requests.get(url)
    if response.status_code == 200:
        filename = f'ZoomInstaller_{os.replace(" ", "")}.{url.split(".")[-1]}'
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f'Download successful for {os}. File {filename} has been saved.')
    else:
        print(f"Failed to download {os}. Status code: {response.status_code}")

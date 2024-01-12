import requests

# URLs for Zoom client downloads
urls = {
    # 'Windows': 'https://zoom.us/client/latest/ZoomInstaller.exe',
    # 'MacOS': 'https://zoom.us/client/latest/Zoom.pkg',
    'Debian': 'https://zoom.us/client/latest/zoom_amd64.deb',
    'Centos': 'https://zoom.us/client/latest/zoom_x86_64.rpm',
    'openSUSE': 'https://zoom.us/client/latest/zoom_openSUSE_x86_64.rpm',
    'Arch': 'https://zoom.us/client/latest/zoom_x86_64.pkg.tar.xz',
    'otherLinux': 'https://zoom.us/client/latest/zoom_x86_64.tar.xz'
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

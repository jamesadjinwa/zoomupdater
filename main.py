import requests
import platform
import sys

# URLs for Zoom client downloads
urls = {
    'Windows': 'https://zoom.us/client/latest/ZoomInstaller.exe',
    'Darwin': 'https://zoom.us/client/latest/Zoom.pkg', #'Darwin' is the kernel name for macOS
    'debian': 'https://zoom.us/client/latest/zoom_amd64.deb',
    'Centos': 'https://zoom.us/client/latest/zoom_x86_64.rpm',
    'openSUSE': 'https://zoom.us/client/latest/zoom_openSUSE_x86_64.rpm',
    'Arch': 'https://zoom.us/client/latest/zoom_x86_64.pkg.tar.xz',
    'otherLinux': 'https://zoom.us/client/latest/zoom_x86_64.tar.xz'
}


# Get the operating system
    
def get_linux_distribution():
    try:
        with open('/etc/os-release', 'r') as f:
            lines = f.readlines()

        distribution_info = {}
        for line in lines:
            key, value = line.strip().split('=')
            distribution_info[key] = value.strip('"\'')

# This line is using the get method of the distribution_info 
# dictionary to retrieve the value associated with the key
# 'PRETTY_NAME'. If the key is present in the dictionary, it 
# returns the corresponding value. If the key is not found in 
# the dictionary, it returns the default value 'Unknown distribution'.
        return distribution_info.get('ID_LIKE', 'Unknown distribution family')
    except Exception as e:
        return f"Error: {e}"


if platform.system() == 'Linux':
    running_os = get_linux_distribution()
    print(f"Running on Linux {running_os}")
elif platform.system() in ['Windows', 'Darwin']: # 'Darwin' is the kernel name for macOS
        running_os = platform.system()
        print(f"Running on {platform.system}")
else:
    print("Running on an unsupported operating system")
    sys.exit(1)
    


# Download executable file for running operating system

for os, url in urls.items():
    if os == running_os: 
        response = requests.get(url)
        if response.status_code == 200:
            filename = f'ZoomInstaller_{os.replace(" ", "")}.{url.split(".")[-1]}'
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f'Download successful for {os}. File {filename} has been saved.')
        else:
            print(f"Failed to download {os}. Status code: {response.status_code}")
            sys.exit(1)
        break

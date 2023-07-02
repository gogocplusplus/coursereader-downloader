# coursereader-downloader
Downloads each canvas coursereader page into a folder, combines into single pdf under combined folder

## Installation

### Install Node Package Manager (NPM) and node.js
1. Download the `nvm-setup.exe` from https://github.com/coreybutler/nvm-windows/releases | Github documentation: https://github.com/coreybutler/nvm-windows
2. Run the `nvm-setup.exe` to install nvm and run it in a terminal
3. Open a terminal and type `nvm`, a list of options should appear
4. Determine if NPM and node.js are already installed:
5. Enter `node -v` and `npm -v` and nothing should appear if not installed
6. Install NPM and node.js by typing in  `nvm install latest`
7. Enter `node -v` and `npm -v` and NPM and node.js should display their respective versions and be successfully installed

### Install node.js packages
* You can run the `install.bat` file to automatically install the node js packages
* Or open a terminal in the current directory and enter `npm install` 
* This command tells npm to read the package.json file and install all the dependencies listed under the "dependencies" and/or "devDependencies" sections.
* npm will now download and install all the required packages specified in the package.json file. The packages will be stored in a folder called node_modules in your project directory.

### Install python
* Download python and install, add python to the system path
* https://www.python.org/downloads/

### Setup python virtual directory venv and install python library requirements
* You can run the `install.bat` file to automatically install virtual environment and python requirements
1. Or create a virtual environment manually inside a venv folder using `python -m venv venv`
2. After creating activate by entering `venv\scripts\activate.bat`
3. Enter `python -m pip install --upgrade pip` to upgrade the venv's pip first
4. Enter `python -m pip install -r requirements.txt` to install PyPDF2 and pdfplumber

## Usage
* You can click on `run.bat` in the folder to run the `pdfmaker.js` in a loop, it'll call the python `pdfcombiner.py` every time the loop executes or you can run it manually using the instructions below:
* Open a terminal or command prompt
* Change directory `cd` to the coursereader-downloader folder or open folder in Windows Explorer and right-click then `Open in terminal` or `Git bash here` or `Powershell, open here`
* Enter `node pdfmaker.js`, the script will run:
1. Enter the base url: Go to canvas page with the coursereader and open up web inspector `Ctrl + Shift + I`. Go to `Elements` tab. The div with the coursereader is under `iframe style =` and `src="the url with the coursereader.html`. Open the link in a new tab, it should take you to the coursereader website. Copy the url at the top and paste it into here. Note that you can skip the inspect element step if you already have the coursereader url. Usually sections in the coursereader are incremented by a letter like `1-a` then `1-b` then `2-a` then `2-b`. The javascript looks at all `iframe` in the url.
2. Enter the base file name: The name that you want the folder and all the files to be named as. For example `ch01`
3. Enter the layout (portrait, landscape; default is landscape): Default for this use case is landscape and you can click enter. Type `portrait` in all undercase characters to use portrait (vertical) orientation.
4. Enter the scale value (0.1-1, default is 0.55): You can click enter to use the default value of 0.55. Going above 0.6 on landscape can cause slides not to fit and take more than one page.
5. Enter the format(A3, A4, Letter, Legal, Tabloid; default is A4): You can click enter to use the default page of A4. A3 and others have more white space.
6. Javascript will execute and pdf files will be individually saved to under the `pdf` folder to `./coursereader-downloader/pdf/*subdirectory`
7. Python will save the combined pdf file and table of contents text file directly to `./coursereader-downloader/pdf/combined/combined.pdf and also combined_toc.txt`

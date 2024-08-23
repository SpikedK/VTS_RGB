# VTS_RGB

Simple .exe plugin to trigger a rainbow animation on selected ArtMeshes for any Vtuber on Vtube Studio.

Download [Link](https://github.com/SpikedK/VTS_RGB/archive/refs/heads/main.zip).


## Installation

It is recommended to unzip the file in .\SteamLibrary\steamapps\common\VTube Studio\VTube Studio_Data\Plugins to keep things organized.

It can be used in any other directory.

## First Time Setup

1. Go to the dist\VTS_RGB_Ver1\_internal directory.
2. Locate `config.json` and `meshes.txt`. If they are missing, create the files as described in **File Content**.
3. Open `config.json`. This file contains the parameters to set the duration of the rainbow animation and which hotkey is used to trigger the animation.
4. Set the duration of the rainbow animation by changing the number in the value of the first key `"rainbow_timer"`. In the file provided, the value is set to 5; this value is in seconds.
5. Set the hotkey that will trigger the rainbow animation. To find the name of the hotkey used by VTube Studio and the specific model you are going to use, you must open VTube Studio, go to Settings > Hotkey Settings and Expressions, and scroll to the hotkey you want to link to the rainbow animation. Copy the name assigned to that hotkey. Paste the name of the hotkey in the value of the second key `"hotkeyName"`. In the file provided, the value is set to `"My Animation 1"`. Make sure the value is enclosed in quotation marks `""`.
6. Save the file, and then close it.
7. Back in the file explorer, open `meshes.txt`.
8. Write the name of every ArtMesh that you want to be affected when triggering the rainbow animation, one ArtMesh per line. Press Enter after writing down each ArtMesh. To find the names of the ArtMeshes on your model, go to Settings > Model Settings, and scroll down to Customize Model. Select the button and choose "Customize Multiply/Screen Color for ArtMeshes." Here you will find the full list of ArtMeshes in your model. Write down the names of the ArtMeshes you want to use. To identify them more easily, you can hover over and click on them in VTube Studio, which will highlight and filter the selected ArtMeshes.
9. Save the file, and then close it.
10. VTS_RGB should be ready to run. I recommend creating a shortcut for quicker access. Right-click `VTS_RGB_Ver1.exe` and create a shortcut.
11. Read **Usage** to start using the plugin.

### File Content

**config.json:** This file uses the JSON format to store the values for the timer and the name of the hotkey set in VTube Studio to trigger the rainbow animation.  
To create the file if missing, go to the dist\VTS_RGB_Ver1\_internal directory, create a new text file, and copy this line into it:  
> {"rainbow_timer": 5, "hotkeyName": "My Animation 1"}  

Then save the file with the exact name "config" as a .json, or change the extension of the file after saving it as a .txt first.

---

**meshes.txt:** This file is a list of all the ArtMeshes that will be tinted during the rainbow animation. Every mesh name must be listed on its own line. As an example, using VTube Studio's hiyori_vts model, VTS_RGB lists a small group of ArtMeshes for this model.  
To create the file if missing, go to the dist\VTS_RGB_Ver1\_internal directory and create a new text file with the exact name "meshes".

## Usage

1. Open VTube Studio and wait until everything loads.
2. In VTube Studio, make sure the API is running; this allows the plugin to interface with VTube Studio.  
   Go to Settings > General Settings and scroll down to VTube Studio and switch the toggle ON to Start API.  
   VTS_RGB uses the default settings to connect on **port 8001**. If it's using a different port, change it before switching the toggle.
3. Run `VTS_RGB_Ver1.exe` located in the \Plugins\dist\VTS_RGB_Ver1 directory.
4. In VTube Studio, if prompted, grant permission. If it is denied by accident, you can close VTS_RGB and run it again to attempt another connection.
5. Using the hotkey set up in **First Time Setup** will play the rainbow animation for the set amount of time.  
   To trigger the animation again, the previous animation needs to have finished. Wait a couple of seconds for the VTube Studio API to reset.

## Potential Issues

After VTS_RGB requests permission in VTube Studio, the plugin might not get access granted due to having a mismatched token. If so, go to the folder where VTS_RGB is running and delete the `Token.txt` file. This file is created at runtime on the first run, but if you got the plugin from other sources, they might have shared the file containing their unique token. After deleting it, run VTS_RGB again, and it should work.

Source code is provided in the zip file, VTS_RGB_Ver1.py.

## Future Versions

Future versions should include a GUI for ease of use, as well as unifying the Config, Meshes, and Token files into a single file.  
Other additions would include setting specific colors to be triggered temporarily, setting the timer at runtime, or letting the tint stay indefinitely.

## License

MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

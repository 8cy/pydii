# Pydii
A simple and open source Discord custom RPC tool.

## Usage
To use this tool, all you need to do is;
1. Download the latest [release](https://github.com/fuwn/pydii/releases).
2. Configure the provided `config.json`.
3. Start up the Pydii executable!

Alternatively, you can just clone or download the [repository](https://github.com/fuwn/pydii) and run the `pydii.py` file.

There are also extra features down below so check out the image.

![](https://strelizia.cc/mvq3zLDLiXIlrHvPGQIjoUu7bU9eGDOg.png)

# Config Explained
- `client_id` - Your Discord Application's client ID
- `details` - The first row of text under the applications name
- `state` - The the row of text under the details
- `time` - If this is left enabled, then you can choose to either set a custom start time or keep track of time.
- `custom_time` - If this enabled, you can specify a custom start time in the `start` value.
- `start` - Here you can set the custom start time if enabled
- `end` - Here you can specify a custom end time. **Advanced users only**
- `large_image` - Here you can specify the large image/ icon.
- `large_text` - Here you can specify the text which is displayed when hovering over the `large_image`.
- `small_image` - Here you can specify the small image/ icon in the bottom right corner of the `large_image`.
- `small_text` - Here you can specify the text which is displayed when hovering over the `small_image`.
- `party_id` - Here you can specify a party key for the application. **Advanced users only**
- `party_size` - Here you can specify a party size for the application. **Advanced users only**
- `join` - Here you can specify a join key for the application. **Advanced users only**
- `spectate` - Here you can specify a spectate key for the application. **Advanced users only**
- `match` - Here you can specify a match key for the application. **Advanced users only**
- `instance` - Honestly I don't really remember what this does, I think it might control weather or not he instance of the RPC will even start or not, so... *Advanced users only**

## TODO
- Eventually make this an executable. I wanted to but for some reason my build wasn't working so plain old python file it was.

## Development
If you want to help witht the development process, feel free to clone or download this repository and/ or make pull requests as you see fit!

If you want to work on this project, you are going to need to install the [pypresence](https://github.com/qwertyquerty/pypresence) library with pip via `pip install pypresence`.

### License
MIT

# Neural Image Generation

This GitHub project demonstrates the use of neural networks to generate images. The model leverages machine learning techniques to produce a variety of visual content, ranging from photorealistic landscapes to abstract artwork.

## Installation

```bash
# Clone the repository
git clone https://github.com/S1avv/gen7free.git

# Go to your project folder
cd gen7free

# Create a virtual environment
poetry shell

# Install the required dependencies
poetry install
```

## Usage example

```python

from gen7free.Image.Client import Client
import asyncio

client = Client("TOKEN", "SECRET_KEY")

model_id = client.get_model()

params = {
    "type": "GENERATE",
    "numImages": 1,
    "width": "1024",
    "height": "1024",
    "generateParams": {
        "query": f"Cat"
    }
}

uuid = client.generate(params, model_id)
images = asyncio.run(client.check_generation(uuid, delay=10, attempts=10))

print(images[0])

```


You can get the token and secret key for free on the [fusionbrain](https://fusionbrain.ai/keys/) website

## Get file.png

```python
import base64

image_data_base64 = images[0]

image_data = base64.b64decode(image_data_base64)

with open("image.png", "wb") as f:
    f.write(image_data)

```

# Required components/libraries

- Poetry: tool for managing Python dependencies and virtual environments can be installed [here](https://python-poetry.org/docs/#installing-with-the-official-installer)
- Requests: The requests library is required to send HTTP requests. It simplifies the process of making HTTP calls from Python and is commonly used for tasks such as fetching data from web APIs or making HTTP requests to web servers. 
Documentation [here](https://pypi.org/project/requests/)
  
## Installing libraries
```bash
poetry install
```
## Or if you want to install the library:
```bash

poetry add [library name]
```

# License
This project is licensed under the MIT License. See the LICENSE file for details.

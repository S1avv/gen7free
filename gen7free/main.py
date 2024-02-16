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

import httpx


API_URL = "https://api.thecatapi.com/v1/breeds"


async def validate_breed(breed: str) -> bool:
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            names_list = [item['name'] for item in data if 'name' in item]
            return breed in names_list
        else:
            return False

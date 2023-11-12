import aiohttp
import asyncio

async def download_html(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"Failed to download {url}. Status code: {response.status}")
            return None

async def main():
    base_url = "https://health-diet.ru/base_of_food/sostav/{}.php"
    start_index = 1
    end_index = 23000  # Укажите нужный диапазон

    async with aiohttp.ClientSession() as session:
        tasks = [download_html(session, base_url.format(i)) for i in range(start_index, end_index + 1)]
        html_pages = await asyncio.gather(*tasks)

    for i, html in enumerate(html_pages, start=start_index):
        if html is not None:
            with open(f"parser/page_{i}.html", "w", encoding="utf-8") as file:
                file.write(html)

if __name__ == "__main__":
    asyncio.run(main())

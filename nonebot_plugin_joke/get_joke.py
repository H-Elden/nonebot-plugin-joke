import httpx


async def get_random_joke_en() -> str:
    """使用[JokeAPI](https://sv443.net/jokeapi/v2/)获取英文笑话"""
    # JokeAPI的URL
    url = "https://v2.jokeapi.dev/joke/Any"

    async with httpx.AsyncClient() as client:
        # 发送异步GET请求
        response = await client.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            joke_data = response.json()
            # 判断返回的是单部分还是双部分的笑话
            if joke_data["type"] == "single":
                return str(joke_data["joke"])
            else:  # 如果是'twopart'
                return f'Q: {joke_data["setup"]}\nA: {joke_data["delivery"]}'
        else:
            raise RuntimeError(f"无法获取笑话，状态码:{response.status_code}")


async def get_random_joke_cn() -> str:
    """使用[夏柔API](https://api.aa1.cn/)获取中文笑话"""
    # 夏柔API的URL
    url = "https://tools.mgtv100.com/external/v1/pear/duanZi"

    async with httpx.AsyncClient() as client:
        # 发送异步GET请求
        response = await client.get(url)

        # 检查请求是否成功
        if response.status_code == 200:
            joke_data = response.json()
            if joke_data["status"] == "success":
                return str(joke_data["data"]).replace("<br>", "\n")
            else:
                raise RuntimeError(f"访问错误！{joke_data}")
        else:
            raise RuntimeError(f"无法获取笑话，状态码: {response.status_code}")

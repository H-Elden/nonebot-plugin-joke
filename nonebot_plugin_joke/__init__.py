from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.plugin import PluginMetadata

from .get_joke import get_random_joke_cn, get_random_joke_en

__plugin_meta__ = PluginMetadata(
    name="中英文笑话",
    description="笑一笑，十年少~ 看个笑话吧~",
    usage=("关键词匹配：\n  [@]讲个笑话：默认中文\n  [@]讲个英语笑话"),
    type="application",
    homepage="https://github.com/H-Elden/nonebot-plugin-joke",
    supported_adapters={"~onebot.v11"},
)

joke_cn = on_keyword({"讲个笑话", "说个笑话"}, rule=to_me(), priority=6, block=True)
joke_en = on_keyword(
    {"讲个英文笑话", "讲个英语笑话", "说个英文笑话", "说个英语笑话"},
    rule=to_me(),
    priority=7,
    block=True,
)


@joke_cn.handle()
async def _():
    try:
        joke = await get_random_joke_cn()
    except Exception as e:
        await joke_cn.finish(f"ERROR! {e}")
    await joke_cn.send(joke)


@joke_en.handle()
async def _():
    try:
        joke = await get_random_joke_en()
    except Exception as e:
        await joke_en.finish(f"ERROR! {e}")
    await joke_en.send(joke)

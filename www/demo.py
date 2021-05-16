import orm
from models import User, Blog, Comment
import asyncio


async def test():
    await orm.create_pool(user='awesome', password='awesome', db='awesome', loop=loop)
    # await orm.create_pool(loop=loop)

    # 插入
    # u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')
    # await u.save()

    # 删除--只能根据主键删除
    # u = User(id='00161295962085348848f997a704569b53aa392c3f2f6b4000')
    # remove1 = await u.delete()

    # 更新--根据主键更新,不修改的字段也要传入之前的值
    # u = User(name='Test2', id='001612961134032ac039525560e45b6be3459e99b9929dd000', email='test2@example.com', passwd='1234567890', image='about:blank')
    # await u.update()

    # 查询
    u = User
    # 主键查询，只要传入主键值
    # find0 = await u.find('0016129600031761285f514896646428b25b4264284db1c000')
    # print(find0)
    # 条件查询
    find1 = await u.findAll("name='Test'")
    print(find1)
    # 数据数量查询
    # find2 = await u.findNumber('count(*)')
    # print(find2)
    # 求和查询
    # find3 = await u.findNumber('sum(created_at) sum')
    # print(find3)
    # 多个关键字查询：两种方式
    # find4 = await u.findAll("name='Test' order by id desc limit 2")
    # find5 = await u.findAll("name='Test'", None, orderBy='id desc', limit=2)
    # print(find4)
    # print(find5)
    #
    # # 创建博客
    # blog = Blog(user_id='0016129600031761285f514896646428b25b4264284db1c000', user_name='Test', name='Test Blog1',
    #             summary='Test Summary1', content='My name is Nidhogg.', user_image='about:blank')
    # await blog.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test())






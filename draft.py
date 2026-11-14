# import asyncio


# # Event Loop - менеджер


# async def task(name, seconds):
#     await asyncio.sleep(seconds)
#     print(f'Задача {name}  готово!')

# async def main():
#     await asyncio.gather(     # gather -- позволяет запустить несколько асинхронных задач одновременно 
#         task('1', 4),
#         task('2', 2),
#         task('3', 1),
#     )

# asyncio.run(main())
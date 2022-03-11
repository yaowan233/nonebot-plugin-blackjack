import setuptools


setuptools.setup(
    name="nonebot_plugin_blackjack",
    version="0.0.4",
    keywords=("pip", "nonebot2", "nonebot", "nonebot_plugin"),
    description="""nonebot2 21点插件""",
    url="https://github.com/yaowan233/nonebot_plugin_blackjack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    platforms="any",
    install_requires=['nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0', 'nonebot2>=2.0.0-beta.1,<3.0.0', 'httpx>=0.19.0', ]
)
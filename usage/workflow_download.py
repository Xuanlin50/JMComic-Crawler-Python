from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
斗罗大陆
斗破苍穹
神印王座

'''

# 单独下载章节
jm_photos = '''



'''


def env(name, default, trim=('[]', '""', "''")):
    import os
    value = os.getenv(name, None)
    if value is None or value == '':
        return default

    for pair in trim:
        if value.startswith(pair[0]) and value.endswith(pair[1]):
            value = value[1:-1]

    return value


def get_id_set(env_name, given):
    aid_set = set()
    for text in [
        given,
        (env(env_name, '')).replace('-', '\n'),
    ]:
        aid_set.update(str_to_set(text))

    return aid_set


def main():
    album_id_set = get_id_set('JM_ALBUM_IDS', jm_albums)
    photo_id_set = get_id_set('JM_PHOTO_IDS', jm_photos)

    helper = JmcomicUI()
    helper.album_id_list = list(album_id_set)
    helper.photo_id_list = list(photo_id_set)

    option = get_option()
助手。跑(选项)
选项。call_all_plugin('下载后')


定义 get_option():
    #读取选项配置文件
option=create_option(操作系统。路径.abspath(操作系统。路径.参加(__file__，'。。/。。/assets/option/option_workflow_download.yml')))

    # 支持工作流覆盖配置文件的配置
    cover_option_config(选项)

    #把请求错误的html下载到文件，方便GitHub Actions下载查看日志
    log_before_raise()

    返回选项


定义 cover_option_config(选项：JmOption):
目录规则=env('DIR_rule',没有一个)
    如果目录规则(_R)是 不 没有一个:
_old=选项。目录规则(_R)
新的(_N)=DirRule(Dir_rule，base_dir=旧的。基底目录(_D))
选项。目录规则(_R)=新的(_N)

impl=env('CLIENT_IMPL',没有一个)
    如果impl是 不 没有一个:
选项。客户.impl=impl

后缀=env('Image_SUFFIX',没有一个)
    如果后缀是 不 没有一个:
选项。下载.图像.后缀=fix_suffix(后缀)


定义 log_before_raise():
JM_download_dir=env('JM_DOWNLOAD_DIR',工作空间())
    mkdir_if_not_exists(JM_download_dir)

    定义 决定文件路径(_F)(e):
RESP=e.语境.得到(ExceptionTool。context_KEY_RESP,没有一个)

        如果RESP是 没有一个:
后缀=str(time_stamp())
        其他:
后缀=resp.URL

name='-'.参加(
            fix_windir_name(它)
            为它在……内 [
e。描述,
                当前线程(_T)().姓名,
后缀
            ]
        )

路径=f'{JM_download_dir}/【出错了】{姓名}.log'
        返回路径

    定义 异常监听器(_L)(E:JmcomicException):
        """
异常监听器，实现了在GitHub操作下，把请求错误的信息下载到文件，方便调试和通知使用者
"""
        # 决定要写入的文件路径
路径=决定文件路径(_F)(e)

        # 准备内容
内容=[
            str(类型(e)),
e。味精,
        ]
        为K，v在……内e。语境.项目():
内容。追加(f'{k}:{v}')

        #resp.text
RESP=e.语境.得到(ExceptionTool。context_KEY_RESP,没有一个)
        如果RESP：
内容。追加(F'响应文本：{RESP.文本}')

        # 写文件
        写入文字(_T)(路径，'\n'.参加(内容))

JmModuleConfig.register_exception_listener(JmcomicException，exception_listener)


如果__name__=='__main__':
    主要的()

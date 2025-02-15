"""处理接口响应信息"""
from rest_framework.response import Response


class APIResponse(Response):
    # 构建 API 响应
    def __init__(self, code=0, message='', data=None, status=200, headers=None, content_type=None, **kwargs):
        dic = {'code': code, 'message': message}
        if data is not None:
            dic['data'] = data

        dic.update(kwargs)  # 这里使用update
        super().__init__(data=dic, status=status,
                         template_name=None, headers=headers,
                         exception=False, content_type=content_type)

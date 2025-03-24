from pydantic import Extra, BaseModel


class Config(BaseModel, extra=Extra.ignore):
    pica_account: str = ""  # （必填）哔咔账号
    pica_password: str = "" # （必填）哔咔密码
    zip_ispwd: bool = True # （必填）是否开启压缩包密码
    zip_password: str = "1919810" # （必填）压缩包密码
    SYSTEM_PROXY: str = "" # （必填）本地代理

class ConfigError(Exception):
    pass
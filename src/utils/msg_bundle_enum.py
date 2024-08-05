class Config:
    indicator_prefix = "foo"
    formatter_string = "{{{name}}}"


class MessageBundleMetaClass(type):
    Config = Config

    def formatter_enum_meta_getter(self, key: str):
        res = super().__getattribute__(key)

        if key == "Config":
            return res

        prefix = getattr(self.Config, "indicator_prefix", Config.indicator_prefix)
        format_string = getattr(self.Config, "formatter_string", Config.formatter_string)

        if (
            not prefix
            or key.startswith(prefix)
        ):
            return format_string.format(name=key)
        
        return res


MessageBundleMetaClass.__getattribute__ = MessageBundleMetaClass.formatter_enum_meta_getter


class MessageBundleEnum(metaclass=MessageBundleMetaClass):
    Config = Config

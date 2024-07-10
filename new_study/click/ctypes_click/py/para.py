import click
from api import *
import typing as t

if t.TYPE_CHECKING:
    import typing_extensions as te
    from .shell_completion import CompletionItem


class click_param_TEST1_T(click.ParamType):
    name = "test1_t"
    type = test1_t

    def convert(
        self, value: t.Any, param: t.Optional["Parameter"], ctx: t.Optional["Context"]
    ) -> t.Any:
        return eval("test1_t("+str(value)+")")
    
# class click_param_TEST2_T(click.ParamType):
#     name = "test2_t"
#     type = test2_t

#     def convert(
#         self, value: t.Any, param: t.Optional["Parameter"], ctx: t.Optional["Context"]
#     ) -> t.Any:
#         return eval("test2_t("+str(value)+")")

class click_param_TEST2_T(click.ParamType):
    name = "test2_t"
    type = test2_t

    def convert(
        self, value, param, ctx
    ):
        return eval("test2_t("+str(value)+")")
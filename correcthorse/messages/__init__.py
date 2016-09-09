import os
import sys
from flufl.i18n import registry, PackageStrategy
application = registry.register(PackageStrategy(
    __package__.rsplit('.', 1)[-2], sys.modules[__package__]))
_ = application._
_.default = os.environ.get("LANGUAGE")


def N_(x):
    return x

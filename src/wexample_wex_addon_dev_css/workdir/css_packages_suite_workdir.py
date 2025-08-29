from __future__ import annotations

from typing import TYPE_CHECKING

from wexample_wex_core.workdir.framework_packages_suite_workdir import (
    FrameworkPackageSuiteWorkdir,
)

if TYPE_CHECKING:
    from wexample_wex_core.workdir.code_base_workdir import CodeBaseWorkdir


class CssPackagesSuiteWorkdir(FrameworkPackageSuiteWorkdir):
    def _get_children_package_workdir_class(self) -> type[CodeBaseWorkdir]:
        from wexample_wex_addon_dev_css.workdir.css_package_workdir import (
            CssPackageWorkdir,
        )

        return CssPackageWorkdir

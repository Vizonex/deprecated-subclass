import pytest

from deprecated_subclass import deprecated_subclass, join_version_if_sequence


def test_subclass_deprecation() -> None:
    @deprecated_subclass("subclassing me is discouraged")
    class Test:
        pass

    # This cannot raise
    _ = Test()

    with pytest.warns(DeprecationWarning):

        class SubTest(Test):
            pass


class HurricaneWarning(Warning):
    pass


class TornadoWarning(Warning):
    pass


class EarthquakeWarning(Warning):
    pass


@pytest.fixture(
    params=(
        DeprecationWarning,
        HurricaneWarning,
        TornadoWarning,
        EarthquakeWarning,
        PendingDeprecationWarning,
    )
)
def warnings(request: pytest.FixtureRequest) -> type[Warning]:
    return request.param


@pytest.fixture(
    params=(
        "1.1",
        "4.2.0",
        (6, 9, 0),
    ),
    ids=("1", "2", "3"),
)
def versions(request: pytest.FixtureRequest) -> tuple[str, tuple[int, ...] | str]:
    param = request.param  # type: str | tuple[int, ...]
    return join_version_if_sequence(param), param


def test_different_categories(warnings: type[Warning]) -> None:
    @deprecated_subclass("this class will be removed soon.", category=warnings)
    class Test:
        pass

    # This cannot raise
    _ = Test()
    with pytest.warns(warnings, match="this class will be removed soon."):

        class Subclass(Test):
            pass


def test_removed_in_version(versions: tuple[str, str | tuple[int, ...]]) -> None:
    o, i = versions  # in/out
    ds = deprecated_subclass("this will be removed soon", removed_in=i)
    assert ds.removed_in == o

    @ds
    class Test:
        pass

    with pytest.warns(
        DeprecationWarning,
        match=rf"this will be removed soon \[Removing subclassing in: {o}\]",
    ):

        class SubClass(Test):
            pass


def test_with_existing_init_subclass() -> None:

    @deprecated_subclass("deprecated")
    class MyClass:
        def __init_subclass__(cls, name: str | None = None) -> None:
            cls.name = name

    with pytest.warns(DeprecationWarning):

        class MySubclass(MyClass, name="A name"):
            pass

    with pytest.warns(DeprecationWarning):

        class MySubclass2(MyClass):
            pass


def test_stack_level() -> None:
    ds = deprecated_subclass("this will be removed soon", stacklevel=2)
    assert ds.stacklevel == 2

    ds2 = deprecated_subclass("this will be removed soon", stacklevel=1)
    assert ds2.stacklevel == 1

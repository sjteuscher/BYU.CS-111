from byu_pytest_utils import with_import


@with_import("lab01", "eighteen_seventy_five")
def test_eighteen_seventy_five(eighteen_seventy_five):
    assert eighteen_seventy_five() == 1875

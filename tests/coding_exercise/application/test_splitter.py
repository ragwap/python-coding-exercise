from inspect import getmembers, isfunction, signature

from assertpy import assert_that

from coding_exercise.application.splitter import Splitter

SPLIT_SIGNATURE = "(self, cable: coding_exercise.domain.model.cable.Cable, times: int)"


def test_should_have_split_method():
    def has_expected_split_method_signature(object):
        return str(signature(object)) == SPLIT_SIGNATURE

    def is_named_split(object):
        return object.__name__ == "split"

    def split_method(object):
        return (
            isfunction(object)
            and is_named_split(object)
            and has_expected_split_method_signature(object)
        )

    assert_that(getmembers(Splitter, predicate=split_method)).is_not_empty()

import sys

from assertpy import assert_that

from coding_exercise.domain.model.cable import Cable


def test_should_have_length():
    given_length = 101

    assert_that(Cable(given_length).length).is_equal_to(given_length)


def test_should_raise_error_if_float_provided_for_length():
    assert_that(Cable).raises(ValueError).when_called_with(101.101)


def test_should_raise_error_if_none_provided_for_length():
    assert_that(Cable).raises(ValueError).when_called_with(None)


def test_should_raise_error_if_negative_provided_for_length():
    assert_that(Cable).raises(ValueError).when_called_with(-101)


def test_should_raise_error_if_greater_than_maxsize_provided_for_length():
    assert_that(Cable).raises(ValueError).when_called_with(sys.maxsize + 1)


def test_should_equal():
    given_length = 101

    assert_that(Cable(given_length)).is_equal_to(Cable(given_length))


def test_should_not_equal():
    assert_that(Cable(101)).is_not_equal_to(Cable(1010))

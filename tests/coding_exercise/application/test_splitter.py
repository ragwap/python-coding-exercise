from assertpy import assert_that
import pytest

from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()

# Asserts a scenario where a cable is split into equal halves
def test_should_split_equally():
    splitter = Splitter()
    cable = Cable(10, "test_cable")
    result = splitter.split(cable, 1)

    assert_that(result).is_length(2)
    assert_that([c.length for c in result]).contains_only(5)
    total_length = sum(c.length for c in result)
    assert_that(total_length).is_equal_to(cable.length)

# Testing a split for a cable with minimum length and minimum times
def test_should_handle_minimal_split():
    splitter = Splitter()
    cable = Cable(2, "small_cable")
    result = splitter.split(cable, 1)

    assert_that(result).is_length(2)
    assert_that([c.length for c in result]).contains_only(1)

# Testing the maximum split that the given ranges can accomodate
def test_should_handle_maximal_split():
    splitter = Splitter()
    cable = Cable(1024, "large_cable")
    result = splitter.split(cable, 63)

    assert_that(result).is_length(64)
    assert_that([c.length for c in result]).contains_only(16)
    total_length = sum(c.length for c in result)
    assert_that(total_length).is_equal_to(cable.length)

# Testing if the validation works for length ranges
def test_should_validate_cable_length():
    splitter = Splitter()
    with pytest.raises(ValueError, match="Cable length should be in range 2 to 1024 inclusive"):
        splitter.split(Cable(1, "too_small"), 1)

    with pytest.raises(ValueError, match="Cable length should be in range 2 to 1024 inclusive"):
        splitter.split(Cable(1025, "too_large"), 1)

# Testing if the validation works for times ranges
def test_should_validate_split_times():
    splitter = Splitter()
    cable = Cable(10, "coconuts")

    with pytest.raises(ValueError, match="Number of splits should be in range 1 to 64 inclusive"):
        splitter.split(cable, 0)

    with pytest.raises(ValueError, match="Number of splits should be in range 1 to 64 inclusive"):
        splitter.split(cable, 65)

# Testing if the input formats for a cable are validated
def test_should_validate_cable_instance():
    splitter = Splitter()
    with pytest.raises(ValueError, match="Invalid input types"):
        splitter.split(None, 1)
    with pytest.raises(ValueError, match="Invalid input types"):
        splitter.split("not_a_cable", 1)

# Testing if the split lengths are validated
def test_should_validate_split_lengths():
    splitter = Splitter()
    cable = Cable(10, "coconuts")

    with pytest.raises(ValueError, match="Cannot split cable into valid lengths"):
        splitter.split(cable, 11)

# Testing splits that do not divide in equal lengths
def test_should_validate_uneven_split():
    splitter = Splitter()
    cable = Cable(5, "coconuts")
    result = splitter.split(cable, 2)

    assert_that(result).is_length(5)
    assert_that([c.length for c in result]).contains_only(1)
    total_length = sum(c.length for c in result)
    assert_that(total_length).is_equal_to(cable.length)

# Testing if the names generated for the cables when split, are correct
def test_should_generate_correct_names():
    splitter = Splitter()
    cable = Cable(10, "coconuts")
    result1 = splitter.split(cable, 1)
    result2 = splitter.split(cable, 2)

    assert_that([c.name for c in result1]).contains(
        "coconuts-0", "coconuts-1"
    )
    assert_that([c.name for c in result2]).contains(
        "coconuts-00", "coconuts-01", "coconuts-02", "coconuts-03", "coconuts-04", "coconuts-05", "coconuts-06", "coconuts-07", "coconuts-08", "coconuts-09"
    )

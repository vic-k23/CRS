"""Testing of module target."""

from logging import INFO, getLogger, basicConfig
from typing import Any
from collections.abc import Mapping
from pytest import mark, raises

from app.target import Target, Coordinates


basicConfig(level=INFO)
logger = getLogger(__name__)


@mark.parametrize(
    "params",
    [
        {"organization_name": "abc", "city": "Cheboksary", "street": "Chelomeya", "building": "1"},
        {
            "organization_name": "abc",
            "city": "Cheboksary",
            "street": "Chelomeya",
            "building": "1",
            "office": 176,
        },
        {
            "organization_name": "abc",
            "city": "Cheboksary",
            "street": "Chelomeya",
            "building": "1",
            "office_name": "176",
            "coordinates": Coordinates(),
        },
    ],
)
def test_target_create_ok(params: Mapping[str, Any]) -> None:
    """Testing creating of target with correct parameters."""
    assert Target(**params)


@mark.parametrize(
    "params, exception",
    [
        ({}, KeyError),
        ({"organization_name": "abc"}, KeyError),
        ({"organization_name": "abc", "city": "Cheboksary"}, KeyError),
        ({"organization_name": "abc", "city": "Cheboksary", "street": "Chelomeya"}, KeyError),
        (
            {
                "organization_name": "abc",
                "city": "Cheboksary",
                "street": "Chelomeya",
                "building": 1,
            },
            KeyError,
        ),
    ],
)
def test_target_create_failed(params: Mapping[str, Any], exception: type[Exception]) -> None:
    """Testing creating of target with incorrect parameters."""
    with raises(exception):
        tgt = Target(**params)  # noqa: F841
    logger.debug("Received parameters: %s", params.keys())

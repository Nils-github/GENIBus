import pytest

from genibus.utils import crc


def test_check_telegram() -> None:
    frame = (0x27, 0x07, 0x20, 0x01, 0x02, 0xC3, 0x02, 0x10, 0x1A, 0x90, 0x1C)

    assert crc.check_telegram(frame)


def test_check_telegram_raises_on_invalid_crc() -> None:
    broken = bytearray([0x27, 0x07, 0x20, 0x01, 0x02, 0xC3, 0x02, 0x10, 0x1A, 0x90, 0x00])

    with pytest.raises(crc.CrcError):
        crc.check_telegram(broken)

    assert crc.check_telegram(broken, silent=True) is False


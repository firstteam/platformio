# Copyright (C) Ivan Kravets <me@ikravets.com>
# See LICENSE for details.

from os.path import join

from platformio.platforms.base import BasePlatform


class AtmelavrPlatform(BasePlatform):
    """
        An embedded platform for Atmel AVR microcontrollers
        (with Arduino Framework)
    """

    PACKAGES = {

        "toolchain-atmelavr": {
            "path": join("tools", "toolchain"),
            "alias": "toolchain",
            "default": True
        },

        "tool-avrdude": {
            "path": join("tools", "avrdude"),
            "alias": "uploader",
            "default": True
        },

        "framework-arduinoavr": {
            "path": join("frameworks", "arduino"),
            "default": True
        }
    }

    def get_name(self):
        return "atmelavr"

    def after_run(self, result):
        # fix STDERR "flash written" for avrdude
        if "flash written" in result['err']:
            result['out'] += "\n" + result['err']
            result['err'] = ""
        return result
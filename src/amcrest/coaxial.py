# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# vim:sw=4:ts=4:et

from .http import Http


# This API is based on an undocumented API of Amcrest Cameras.
# This API may change without notice
class Coaxial(Http):
    def set_coax(self, enable: bool) -> str:
        """
        Params:
            mode         - True to enable white LED, false to disable

        Turns white LED on or off in the camera
        """
        strM = 1 if str(enable).lower() == "true" else 2
        ret = self.command(
            f"coaxialControlIO.cgi?action=control&channel=1&info[0].Type=1&info[0].IO={strM}&info[0].TriggerMode=2"
        )
        return ret.content.decode()

    async def async_set_coax(self, enable: bool) -> str:
        strM = 1 if str(enable).lower() == "true" else 2
        ret = await self.async_command(
            f"coaxialControlIO.cgi?action=control&channel=1&info[0].Type=1&info[0].IO={strM}&info[0].TriggerMode=2"
        )
        return ret.content.decode()

    def coax_config(self) -> str:
        return self._get_coax_config()

    async def async_coax_config(self) -> str:
        return await self._async_get_coax_config()

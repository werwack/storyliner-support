# GPLv3 License
# Copyright (C) 2024 WerwacK
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
StoryLiner

Call this file in command line to launch Blender in a "project context", ie in a context where StoryLiner gets all the project information
thanks to a reference to its Project Settings json file.

See how to setup a configuration to launch an instance of Blender in the context of your project here:
https://werwackfx.com/storyliner/doc/how-to/how-to-useinproduction.html#launching-blender-in-a-context-of-project

"""

import bpy


# set your project file path here:
# eg: project_settings_file_path = "z:/MyProject/MyProjectSettings.json"
project_settings_file_path = "z:/MyProject/MyProjectSettings.json"

if "storyliner" not in bpy.context.preferences.addons:
    print("StoryLiner not found")
else:
    try:
        from storyliner.api.launch_blender_in_project_context import launchBlenderInProjectContext

        launchBlenderInProjectContext(project_settings_file_path)

    except Exception as e:
        print(f"{e}. Cannot set project path")

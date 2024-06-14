-------------------------
## 1.0.61
- **Beta**
-------------------------


### Bug fixes
- Fixed missing font error on Mac

-------------------------
## 1.0.52
- **Release**
-------------------------

### Bug fixes
- Fixed error at first register time when PIL is not installed

-------------------------
## 1.0.51
- **Release**
-------------------------

### Bug fixes
- Fixed crash in 2.5D Free GP edition, when a new layer was added in draw mode and autokey activated
- Fixed error message in rendered of Essential ed, due to the use of otio

-------------------------
## 1.0.50
- **Release**
-------------------------

### UI
- Added a button to show and toggle the multiframe state of the grease pencil draw mode

### 2.5D Free GP:
- Added UI component to enable motion path on selected free gp

### Toolbar:
- Added an option to align to other axes that just Y

### Bug fixes
- Added a condition to use the icon named "LIGHTPROBE_VOLUME" instead of "LIGHTPROBE_GRID" because its name changed in Blender 4.1
- Ensure that the storyboard frame don't get visible when set to "invisible" and the camera is selected
- Storyboard frame visibility fixed when camera is selected and when current shot is changed
- Edit Play Mode fixed: first frame of shots was played twice
- Edit Play Mode fixed: issue when play started from a disabled shot


-------------------------
## 1.0.25
- **Pre Release #3**
-------------------------

### Edit Play Mode
- Fixed play loop issue when time arrived at time range end

### UI
- Fixed Audio button visual state
- Fixed ambiguous parameter in tool "Create Multiple Shots"

### Storyboard / Hybrid
- Added a new row under the Current Layer row to easily get the 3 latest materials used on the layer
- Added support for layer masks (V 1.0.25)
- The Add new Material now let the user choose between creating a new slot or using the active one
- Move to Layer operator has been replace by native operator call

### Viewport Toolbar
- Fixed the display of the Flop button in Storyboard mode (by duplicating the reference to the operator)
- Adapted the camera gizmos to use selected camera when the viewport is not set to the current camera
- Improved tooltips and disabled state display of camera gizmos

### Rendering
- Bug fix: intermediate directory was not deleted when a shot was rendered in image sequence and without StampInfo

### Code
- Added shortcut to turn on dev mode

### Bug fixes
- Fixed a bug in the Retimer where a crash occurred when time range was in the deleted range

-------------------------
## 1.0.23
- **Pre Release #2**
-------------------------

### UI
- Added a button to toggle the Lock View Rotation

### Edit Timeline
- Improved interactions with clips: double-click on clip is now supported even when not in interactive mode
- When double-clicking on a shot clip, key modifiers and behaviors are now consistent with those used
  in the main panel
- Button to display the widget settings in the Timeline toolbar has been changed
- Added a tooltip on clips to display shot information (press Alt and wait)
- Added suitable mouse cursors when manipulating shot clips
- Added support for mouse wheel for zoom and pan (Ctrl + mouse wheel)

### Interactive Shots Stack
- When double-clicking on a shot clip, key modifiers and behaviors are now consistent with those used
  in the main panel
- Scaling of shot content (shift + move handle) is now done after the manipulation, not during it, to fixed precision issues
  with grease pencil drawing frames
- Added a tooltip on clips to display shot information (press Alt and wait)
- Added a shortcut (HOME) in the Edit Timeline to frame the whole edit
- Added suitable mouse cursors when manipulating shot clips
- Button to display the widget settings in the Timeline toolbar has been changed

### Hybrid
- Added controls for the canvas of Free GP objects
- Added information to see the size of the canvas in scene units, as well as the size of the grid
- Added controls to set the grid on GP objects
- Fixed disabled layout when a GP was selected
- Fixed the addition of a default layer and material to new free gp

### Retimer
- Added support for annotations
- Fixed support for grease pencil animated properties

### Display devices
- Added a button in the Preferences to print the monitors information
- Changed the ui scale from view.ui_scale to system.ui_scale

### Bug fixes
- Made the color change disabled in the Duplicate Shot popup when the camera is not duplicated

### Code
- Reorganized the functions to create default layer on new gp
- Added support for tooltip in Component2D

-------------------------
## 1.0.22
-------------------------

Packed Previz Edition

### Code
- Reorganized imports

-------------------------
## 1.0.21
- **Pre Release #1**
-------------------------

Packed Light Edition

### Storyboard
- Added a default gp material
- Added a default layer with a default drawing frame on new storyboard frames

### Code
- Restructured features and tools

-------------------------
## 1.0.14
- **Beta Release #5**
-------------------------

### Code
- Merged code for Light edition

### Bug fix
- Fixed an error when rendering with StampInfo not installed

-------------------------
## 1.0.13
- **Beta Release #4**
-------------------------

### Storyboard tools and workflow
- Added a set of copy / paste operators to duplicate strokes and their materials to other
  layers or grease pencil objects in an efficient way

### Features - Viewport Toolbar
- Fixed Objects Depth Move, added undo support for accelerator
- Added support for several objects in selection for Objects Pan and Objects Scale operators

### UI
- Added support for the Viewport Toolbar to the Overlays Toggle button

### Rendering
- Render queue of each scene is now automatically cleared when a file is loaded
- A Reset Render Queue item has been added to the Render panel settings menu
- Fixed an error message when a snapshot was rendered with StampInfo

### Code
- Refactored add-on preferences inheritance

-------------------------
## 1.0.10
- **Beta Release #3**
-------------------------

### Important changes
- The orientation of the Storyboard Frame has been changed to match the general convention
  of having the -Y axis pointing forward

- OpenTimelineIO is not supported anymore on mac, due to installation issues. This only impact
  the Studio edition, and just for the tools that were using this library

- OpenTimelineIO is currently not supported on PC either on Blender 4.1. This is due to the fact that
  Blender 4.1 uses Python 3.11 and the OpenTimelineIO packages for this version of Python have not
  been released yet. At soon as the packages are available on pypi.org OpenTimelineIO will be automatically
  installed and usable at new. This affects only the Studio edition, and just for the tools that were using this library

- When a new Storyboard shot or a new Free Grease Pencil objects are created, they will get the set
  of layers and materials from the preset only if requested in the UI of the related creation dialog box.
  When created from the + buttons (=when there is no dialog box), preset layers and materials are added
  only if the related preference property is turned on (see add-on Preferences panel, in Sequences and Shots
  Default Settings).
  The Quick Layers toolbar related to these layers is then visible only for objects owning them, or if
  it is explicitly made visible by checking the "Use Quick Layers" in the tool button of the panel.

### Storyboard layout
The Storyboard properties panel has been completely redesigned: new UI, new tools, new workflow.

Layer slots:
- A new mode has been added to allow the last material used on a slot to be set as the active
  one when this slop is set

Layers list:
    All the properties (use mask, onion skinning, visibility, lock) now have additional behaviors
    to affect also the other layers (see the tooltips)

Material list:
    Since it is actually material slots that are used by layers, and not materials, the slot
    indices have been exposed in the material list
    All the properties (onion skinning, visibility, lock) now have additional behaviors to affect also
    the other materials (see the tooltips)

- New tools were added or exposed: layers auto lock, grid, mirror, material picking

- The time navigation toolbar has been improved

- On the Storyboard Frames, property canvasOpacity is deprecated. The opacity of the canvas
  is now directly controlled by the opacity layer property

### Hybrid layout and 2.5D tools
The 2.5D Grease Pencil panel has been modified to match the design and workflow of the Storyboard
properties panel.
- Added a button to create a "Free Scene Grease Pencil", which is the term used in StoryLiner to 
designate a grease pencil frame that can be used to receive some 2D drawings
- Added a Pick button to get another grease pencil object while still being in the same object interaction mode
- Added an Autolock Layers to lock all the layers but the current one (and then be able to erase or sculpt only on current layer)
- Added an option to automatically align the view to the grease pencil when entering in Draw mode

### Features - Viewport Toolbar
- Improved colors and alignment
- Added a camera rotate mode
- Added a flop camera mode
- Added a terminology from real cam movements
- Added an Align Cursor to Active Object functionality in the Move Object to Cursor
- Reworked all interactions and axis drawings
- Activated mouse cursor screen loop by default (can be toggled in the Preferences panel)
- Fixed the position of the Maximize Screen when view is locked

### UI
- Viewports now have a red frame when autokey is on. This can be disabled in the General tab in Preferences
- In Camera HUD, added a shadow to improve readability
- Shortcuts are now displayed in the tooltips of the playbar and draw mode buttons
- Improved tooltip descriptions here and there
- Replaced the name of the layout "Edit" by "Editing"
- The 2.5D Free Grease Pencil panel can be used as a separated panel (see in Preferences)

### Playbar and time navigation:
- The playbar at the top of the StoryLiner panel is not disabled anymore when no shots are in the edit
- Undo have been added to all the navigation operators
- "Jump to First / Last Enabled Shot" now go to the start / end of the time range when the current edit has no shots or
  no shots enabled
- "Jump to Start / End of Shot" now go to the start / end of the time range when the current edit has no shots or
  no shots enabled
- "Jump to Previous Frame" and "Jump to Next Frame" are now referring to the time of the edit. In other words, when a
  frame that is out of a shot range is requested then the scene time is set to the time of the first (or last) frame
  of the next (or previous) shot.

### Key mapping
- More key mapping have been exposed
- The Keymap section in the add-on Preferences panel has been completed with a category for the Playbar operators.
- The use of the up and down arrow keys to navigate between previous and next shots is now inverted by default,
  to match the behavior of any other DCC or edit software.
  Go to the Key Mapping section of the add-on Preferences to change it
- An operator has been exposed to pick another grease pencil object (free or storyboard frame) at any time and
  continue the editing with the same interaction mode

### Edit tools
- Added an Export Edit as text and JSON in the Edit tools menu

### Rendering
- Added a message when still image is out of shot render range
- When a rendering category has an issue, the corresponding rendering buttons are now disabled and a warning panel
  is displayed in place of its properties do explain the issue

### Code
- Harmonisation of the panel property names
- Moved retimer and stampinfo to the Tools folder

### Bug fixes
- Fixed StampInfo not generated for out of shot range still images
- Fixed StampInfo not displaying the handles information when handles were activated in the sequence settings
- Fixed an error in the Retimer when using Emtpy objects as images
- Grease Pencil frame is not deleted anymore when the camera of the shot is not deleted 

    
-------------------------
## 1.0.2
- **Beta Release #2**
-------------------------
### Editions
- OpenTimelineIO is not installed anymore for Mac since it seems not able to compile successfully

### Features
- Added a feature in the edit tools to export the current edit as a JSON file
- Added a Center View on Selected Object in the viewport toolbar

### Storyboard
- Reorganized the Storyboard panel
- Added a Toggle Grid tool
- Added a green default color for the frame grid

### UI
- Improved UI of Camera BG properties panel
- Improved UI of Camera BG properties panel

### Code
- Refactored structure of grease pencil 2.5D
- Added preferences for Experimental as aggregation
- Added Experimental preferences and mechanics

### Bug fixes
- Fixed a crash of the Preferences panel on Mac due to an invalid file path

-------------------------
## 1.0.1
- **Beta Release #1**
-------------------------
### UI
- Improved the Add New Shot window to always get the current time as the shot start
- Removed the At current Time parameter in the Duplicate Shot panel, for storyboard shots
- Added QuickHelp Display toggle preference also in the General UI
- Fixed some tooltips

### UX
- Added a selection clear when a new edit is created

### Viewport Toolbar
- Centered the toolbar between the left side of the viewport and the left side of the N toolbar
- Added buttons to minimize the sub toolbars

### Project Settings
- Added a mode and offset to control the start time of the new storyboard shots

### Rendering
- The render queue of each scene is now reset when the Blender file is loaded

### Code
- Renamed collapsible functions

### Bug fixes
- Fixed sequence start time that was not correctly initialized
- Fixed the duration of the new shots, which was too long by 1 frame
- Fixed an error message in the render playblast when otio libraries are used (cf setRenderEngineSettings())
- Fixed a display issue with the render queue when it contains invalid configuration
- Fixed invalid region in Edit Timeline with several 3D views

-------------------------
## 0.9.413
- **Alpha Release #16**
-------------------------
### UI
- Added the sequence properties menu also to the Edit tools menu

### Shots Stack
- Better support of the user Preferences global scale

### Edit Timeline
- Various graphics fixes

### Editions
- Set the Edit layout to Studio Edition only

-------------------------
## 0.9.412
- **Alpha Release #15**
-------------------------
### UX
- Improved undos on shot creation and deletion
- Improved Open Explored tooltips
- Improved messages when OTIO not available

### Dev
- Added buttons in the Preferences to acced to the Python and install libraries folders

### Bug fixes
- Fixed a wring display in a quick tooltip
- Fixed an error when OTIO was not installed but requested
- Fixed Get Current Frame button in the Add New Shot
- Temporary fixed a crash on Mac in the texture shader

-------------------------
## 0.9.411
- **Alpha Release #14**
-------------------------
### UI Storyboard
- Fixed canvas layer state that was changed when all the layers states (lock and visibility) were changed

### Otio
- Fixed a fps issue for xml export

### Editions
- Separate features according to edition

### Rendering
- Rewrote file format management in createTakeRenderJobs()
- Reorganized render sections
- Introduced more flexibility to specify the output file formats

### Bug fixes
- Fixed sequence video files not always rendered

-------------------------
## 0.9.410
- **Alpha Release #13**
-------------------------
### UI Storyboard
- Change the position of the Draw button, made its icon reflect the current sub mode
- Added a button to toggle the onion skin
- Added behaviors on the layers buttons to toggle their lock state with shift key modifier

### UI
- Update a few icons

### Bug fixes
- Fixed rendering issue for shots with a "." char in their name

-------------------------
## 0.9.401
- **Alpha Release #12**
-------------------------
### UI
- Change behavior of Overlay Toggle button

### Bug fixes
- Fixed position of the Fullscreen/Maximize button in the viewport
- Fixed a context override issue with bpy.ops.action.view_frame in zoom_dopesheet_view_to_range when new storyboard shots were created
- Fixed a rendering issue when using the Playblast mode

-------------------------
## 0.9.400
- **Alpha Release #11**
-------------------------
First version without BGL. Fully working on GPU !!!
This alpha release is supported by Blender 4.0 Beta and sould be supported by Metal on Mac OS

### Sequence Timeline 
- Removed Sequence Timeline code
- Removed bgl code in favor of gpu

### Edit Timeline 
- Introduced Edit Timeline, which is a brand new widget to edit the sequence in edit time in the viewport.
It is fully based on the library GPU, and completely replace the Sequence Timeline.

### Bug fixes
- Rendering: Fixed a crash when pressing the Snapshots and the Edit Board rendering modes

-------------------------
## 0.9.110
-------------------------

### Base version for new Edit Timeline


-------------------------
## 0.9.103
- **Alpha Release #10**
-------------------------
### Rendering
- Completely refactored the rendering queue for a better support of output file formats

- Deep changes in the Render UI:
    - Removed edit list render mode item
    - Moved the Render All at the end of the list
    - Better display of the output file formats
    - Added a button to reset the render settings

- Fixed crashes in the Playblast render mode
- Added support for relative media paths in the edit list
- Added the possibility to export an edit list with the shot as image sequences 
- Added a new type of rendering: the snapshots. Here only the representative frames of the shots are rendered
- Playblast: Fix on the view color management so that the SOLID view mode is rendered with the same filter
- Split the render jobs so that the progress bar is more accurate and the queue can be interrupted more easily

### Viewport Toolbar
- Added a button to hide the viewport toolbar at the top of the main panel
- Moved the Fullscreen gizmo from the bottom right side of the viewport to the top right cause more convenient there

### Shots
- Replace the shot start and end sliders in the Add New Shot dialog box by a shot start and duration sliders
- Reinforced the notion of Sequence Start Time

### UI
- Removed the Interactive Toggle button that was at the top of the main panel cause it wasn't so useful there
- Improved warnings display

### Project Settings
- Improved support for output file formats
- Added a Reset Properties button

### Code
- Removed the rendering code from StampInfo
- Removed RSS outdated code
- wrote a function getFontSize() to encapsulate getsize from PIL, which became deprecated since PIL 10.0

-------------------------
## 0.9.7
- **Alpha Release #9**
-------------------------
cf commits

-------------------------
## 0.9.6
- **Alpha Release #9**
-------------------------
### UI
- Removed Toggle Shots Stack Interaction from the main panel (cause not so much used)
- Added a Toggle Viewport Toolbar instead

- Fixed issue with the Resolution Percentage during rendering

-------------------------
## 0.9.5
- **Alpha Release #8**
-------------------------
### Prefs
- Placed the UI Behavior properties for shot selection above in the list

### UI
- Fixed a bug in the selection of cameras in hybrid mode
- Added an autokey button on the playbar that is red when autokey is active
- Fixed a visual bug (vertical lines visible when in camera mode) in the Camera HUD

### Storyboard
- Toolbar: Changed the place of the Full Screen gizmo
- Storyboard Frame: Any object can now be linked to the storyboard frame, to be part of its local time

- Fixed a bug in the new unique names used for any new objects created in StoryLiner
- Added codes for warnings and a warning when there is a layout issue in the scene

-------------------------
## 0.9.4
- **Alpha Release #7**
-------------------------
Added support for editions
Updated documentation

-----
## 0.9.2
### UI
- Added the StoryLiner logo to the About and Prefs panels
- Make the From File Project Settings parameter visible only when this setting is chosen
- Added the StoryLiner logo
- Improved some tooltips

-----
## 0.9.1
### UI and concepts
- Replaced the term Take to Edit in the user interface

### Storyboard
- Added support for text on storyboard frames

### Doc
- Updated the documentation

-------------------------
## 0.8.28
- **Alpha Release #6**
-------------------------
Added Resets buttons to the pref panel

### Code refactor
Cleaned Resets module
Cleaned methods to assign a category to a property

-------------------------
## 0.8.27
- **Alpha Release #5**
-------------------------
### Code refactor
- Initialization process in the scene has been refactored and cleaned
- Post Load hanlders and patches application has been completely rewritten
- Cleaned Reset ui functions

### Bug fixes:
- Fixes a preset buttons lock issue

-------------------------
## 0.8.26
- **Alpha Release #4**
-------------------------
### Bug fixes:
- Improved StoryLiner init state detection
- Added a Reset item in the menu
- Set hard min and max values to the number or rows and columns of the Edit Board

-------------------------
## 0.8.25
- **Alpha Release #3**
-------------------------
### Bug fixes:
- Rename cameras from shot names fixed
- attempt to cacht a crash when issues in the installation of the Python libs

-------------------------
## 0.8.23
- **Alpha Release #2**
-------------------------
### Toolbar
- Improved tools for Storyboard layout

- Improved the UI of the Add New Shot window
- Started rendering task of camera backgrounds
- Fixed small bugs here and there

-----
## 0.8.22
### Toolbar
- Added items dedicated to Storyboard

- Fixed wrong shot type in Add New Shot dialog window

-----
## 0.8.21

### Layouts
- Introduction of new layouts: Hybrid and Edit
- Clean-up in the Preferences panel for layout related features and behaviors
- Auto setup storyboard layout when opening a 2D workspace
- New File and Add Workspace items in the main panel menu

### Toolbar
- Added a toolbar in the 3D viewport to manipulate the drawings, objects and cameras

- Export Storyboard feature renamed to Export Edit Board

### Bug fixes
- Various crashes during rendering 

-------------------------
## 0.8.15
- **Alpha Release**
-------------------------

-----
## 1.0.16
### Storyboarding
- Moved the batch shots creations tools in the Shots menu to the Shot Tools section
- Made the indice of the first shot of the batch stoyborad frame creation start at 10 instead of 0

### Viewport Toolbar
- Added a viewport toolbar inspired by Storytools (Thomas )

### Interactive Shots Stack
- When Interactions is set to off the Shots Stack transparency is increased
- A parameter has been added to control the opacity in that case

### Preferences
- Improved the UI and default settings mode for the layouts

### Code
- Splitted the add-on preferences in several files
- In the gpu_2d library components are now affected by the opacity of the parent by default

-----
## 1.0.13
### Rendering
- Added a progress bar in the render panel, and the ability to pause and cancel the rendering

-----
## 1.0.12
- Removed the notion of current take
- Added a list box to display and manage all the takes at the same time
- Fixed rename of shot dependencies when a camera shot is renamed

-----
## 1.0.11
- Added a global display mode to show and hide quick help buttons
- Exposed some options for the Sequence Timeline to change its display size
- Added a feature to make the name of the camera match the name of its shot
- Deeply improved the Make Camera Unique features and information feedback
- Added SMPTE timings in the Edit mode
- Added a button to set the shot using the selected camera as the current one
- Fixed a crash in Duplicate Shot

-----
## 1.0.10
### Rendering
- Deep refactor in the rendering function
- Fixed the sound that wasn't rendered for image sequences only
- Fixed the playblast rendering

-----
## 1.0.9
- Improved quick help components

-----
## 1.0.8
### Storyboard Export to PDF
- Added an option to preserve the rendered snapshots
- Cleaned some function names

-----
## 1.0.7
- Updated the renderers available in the Render panel to support Cycles hardware rendering
- Revamped the UI of the renderers
- Fixed the name of the operator classes to add 'OT'

-----
## 1.0.6
### Storyboard Export to PDF
- Added an Export Edit Board to PDF rendering button

-----
## 1.0.5
### Stamp Info
- Added a "production name" field

-----
## 1.0.4
- Added an import takes from Shot Manager feature

- Removed the OTIO distribution and get it directly online
- Fixed the ZippAddon script for the needs of StoryLiner

-----
## 1.0.3
### Project Settings
- Project Settings can be saved to a json file and reloaded
- Introduced a mode to have the settings directly taken from a json file and udpdated when the file changes

### Stamp Info
- Settings can now be saved to a json file and reloaded

-----
## 1.0.2
- Deep refactor to rename from Shot Manager to StoryLiner
- CSS style sheet in doc

-----
## 1.0.1
- Forked from Ubisoft Shot Manager add-on (https://github.com/ubisoft/shotmanager) V2.1.42



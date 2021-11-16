# BlenderColabRender
Render .blend files on google colab

# Important to know
google colab suspends tasks if no user interaction is detected.

so interacting(random scrolling, clicking in blank areas) with google colab is required


# prerequisites
 upload your .blend file in google drve

# usage
 1. [open](https://colab.research.google.com/github/aditya24raj/blendercolabrender/blob/master/RenderMyBlender.ipynb) this notebook in google colab
 2. on google colab site do- File > save a copy in drive
 3. enter render preferences-
    - filepath: location of .blend file
    - camera_name: camera which you want to render
    - start_frame: start rendering from this frame
    - end_frame: stop rendering at this frame
  4. click play button (present on left of render preferences)
  5. rendered frames are saved in a folder named 'camera_name'(provided at step 3) at filepath folder
  6. keep interacting every now and then, else render will stop
  7. if render stop, find last rendered frame and set start_frame to be next frame number

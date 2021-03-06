from OpenGL.GL import glPushMatrix, glPopMatrix
from OpenGL.GL import glPointSize, glLineWidth

#import pyvrui
from pyvrui import getCurrentFrameTime

elapsedTime = getCurrentFrameTime

pushMatrix = glPushMatrix
popMatrix  = glPopMatrix
pointSize  = glPointSize
lineWidth  = glLineWidth

# Global variables

_App            = None  # the Application object
_App_Path       = None  # path to the vroom application root directory
_App_Fullpath   = None  # path to the vroom application 
_Module_Name    = None  # name of the vroom module
_Resource_Paths = None  # system resource directories

_Listener       = None

class _Global:
   
   def require(self, attr):
      def decorator(f):
         def wrapped(*args, **kwargs):
            if not getattr(Global, attr, False):
               return
            f(*args, **kwargs)
         return wrapped
      return decorator

Global = _Global()

def currentFrame():
   return _App.frame_count

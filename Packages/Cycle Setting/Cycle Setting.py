"""

Cycle Setting plugin for Sublime Text 2.
Copyright 2011 Jesse McCarthy <http://jessemccarthy.net/>

Adds a command that can be called from a key binding to toggle or
cycle through values for a non-boolean setting.

The Software may be used under the MIT (aka X11) license or Simplified
BSD (aka FreeBSD) license.  See LICENSE

"""

import sublime, sublime_plugin

class CycleSettingCommand( sublime_plugin.TextCommand ):

  def run( self, edit, setting, options ):

    """Cycle $setting to next of $options"""

    options = list( set( options ) )

    index = len( options )

    if not index :

      return


    settings = self.view.settings()

    value = settings.get( setting )


    if value in options :

      index = options.index( value )


    index += 1


    if index >= len( options ) :

      index = 0


    value = options[ index ]


    settings.set( setting, value )


    self.view.set_status(

      'cycle_setting',

      "Setting '{setting}' cycled to value '{value}'".format( **locals() )

    )
    
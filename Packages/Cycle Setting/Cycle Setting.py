import sublime, sublime_plugin

class CycleSettingCommand( sublime_plugin.TextCommand ):

  def run( self, edit, setting, options ):

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


    self.view.set_status( 'cycle_setting', "Setting '{setting}' cycled to value '{value}'".format( **locals() ) )
    
import sublime, sublime_plugin

class CycleSettingCommand( sublime_plugin.TextCommand ):
  
  def run( self, edit, setting, options ):

    options = list( set( options ) )
      
    settings = self.view.settings()

    value = settings.get( setting )

    index = len( options )

    if value in options :

      index = options.index( value )


    index += 1


    if index >= len( options ) :

      index = 0


    value = options[ index ]


    settings.set( setting, value )


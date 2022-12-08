class Topos(dict):
    """
        Topos is a class to handle 
        collections of objects in vniversvs
    """
    # attrs: []
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

##########################################################################################
# GENERAL ################################################################################
##########################################################################################

    def create_object( self, object_name, object_initialization_data ):
        try:
            object = self.vniversvs.objects[object_name](
                initialization_data = object_initialization_data
            )
        except:
            object = self.vniversvs.objects[object_name]()
        if object_name not in self:
            self[object_name] = {}
        self[object_name][object_initialization_data['name']] = object
        self.devs.make_object_metadata(object)
        return object

    def read_object( self, object_id ):
        object = None
        for object_type in self:
            if object_id in self[object_type]:
                object = self[object_type][object_id]
        if object == None:
            print('read_object method returned None')
        return object




#

from devs.alpha import Alpha
from vniversvs.game import Game
from vniversvs.match import Match
from vniversvs.player import Player
from vniversvs.agent import Agent
import pandas as pd
import os
import poker 
import random as rd

class VNIVERSVS(dict):
    """
        vniversvs the class to handle project objects
    """
    # attrs: []
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.objects = {
            ### PLACE EVERY CLASS HERE LIKE SO:
            # 'ClassName': class
            'Game': Game,
            'Match': Match,
            'Player': Player,
            'Agent': Agent,
            # 'Match': Match,
            # 'Match': Match,
        }
        self.pd = pd
        self.os = os
        self.pk = poker
        self.rd = rd

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

##########################################################################################
# OBJECT HANDLING ########################################################################
##########################################################################################

    def create_object( self, object_name, object_initialization_data ):
        try:
            object = self.objects[object_name](
                initialization_data = object_initialization_data
            )
        except:
            object = self.objects[object_name]()
        if object_name not in self.topos:
            self.topos[object_name] = {}
        self.topos[object_name][object_initialization_data['name']] = object
        self.devs.make_object_metadata(object)
        return object

    def read_object( self, object_id ):
        object = None
        for object_type in self.topos:
            if object_id in self.topos[object_type]:
                object = self.topos[object_type][object_id]
        if object == None:
            print('read_object method returned None')
        return object

    # def update_object( self, object_id, new_object_data ):
    #     try:
    #         object = self.read_object( object_id )
    #         for attribute_name in new_object_data.keys():
    #             object.attribute = new_object_data[ attribute ]
    #     except:
    #         print('Could not find object', object_name)
    #
    # def delete_object( self, object_name ):
    #     try:
    #         for collection_name in self.collections.keys():
    #             if object_name in self.collections[collection_name].keys():
    #                 self.collections[collection_name].pop(object_name)
    #     except:
    #         print('could not find object', object_name)


##########################################################################################
# PROJECT HANDLING #######################################################################
##########################################################################################

    def init_project( self ):
        # print('banana')
        self.start_game()

    def start_game(self):
        self.game = self.create_object(
            'Game',
            {'name': 'game'}
        )
        self.game.initiate_new_match()
        # self.game.run()
        

#

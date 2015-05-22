##########################################################################
# Copyright (C) RIPJAR, Ltd - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Robert Biggs <robert.biggs@yripjar.com>, April 2015
##########################################################################


import force_atlas


def layout(G, iterations=-1, duration=-1, haltVelocity=3.):
    force_atlas.layout(G, debug=True, haltVelocity=haltVelocity, iterations=iterations, duration=duration)

class Hero:
    """
    in-memory representation of a Hero and all its information.
    """
    def __init__(self):
        # String name of the hero.
        self.name = None

        # String of the primary attribute ("Strength", "Agility", or "Intelligence")
        self.primary_attribute = None

        # dict where key is "Strength", "Agility", or "Intelligence" and value
        # is tuple of (base, growth per level)
        self.attr_growth = dict()

        # attributes with calculated scaling by level.  Map from attribute name
        # to tuple of (base, level 1, level 16, level 25) value.
        self.scaling_attrs = dict()

        # dict of attributes with single values, such as "attack range", where
        # the key is the attribute name (k="attack range", v="Melee")
        self.kv_attrs = dict()

        # TODO: complete hero state

    def pretty_print(self):
        print "Name: %s" % self.name
        print "Attributes:"
        print "  Primary: %s" % self.primary_attribute
        for attr, val in self.attr_growth.items():
            print("  %s: %s +%s" % (attr, val[0], val[1]))
        print("Scaling attributes:")
        for attr, val in self.scaling_attrs.items():
            print("  %s: base: %s, lvl1: %s, lvl16: %s, lvl25: %s" % (
                attr, val[0], val[1], val[2], val[3]
            ))
        print("Other attributes:")
        for attr, val in self.kv_attrs.items():
            print("  %s: %s" % (attr, val))

class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:
    (1) items added
    (2) items removed
    (3) keys same in both but changed values
    (4) keys same in both and unchanged values
    """

    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.set_current_keys, self.set_past_keys = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.set_current_keys.intersection(self.set_past_keys)

    def added(self):
        added_keys = list(self.set_current_keys - self.intersect)
        result = {}
        for key in added_keys:
            result[key] = self.current_dict[key]

        return result

    def removed(self):
        removed_keys = list(self.set_past - self.intersect)
        result = {}
        for key in removed_keys:
            result[key] = self.current_dict[key]

        return result

    def changed(self):
        result = {}
        for key in list(self.intersect):
            try:
                if self.current_dict[key] != self.past_dict[key]:
                    result[key] = self.current_dict[key]
            except:
                pass

        return result

    def unchanged(self):
        result = {}
        for key in list(self.intersect):
            try:
                if self.current_dict[key] != self.past_dict[key]:
                    result[key] = self.current_dict[key]
            except:
                pass

        return result

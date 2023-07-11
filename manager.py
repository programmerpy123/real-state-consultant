class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def __str__(self):
        return f"{self._class}"

    def search(self,**kwargs):

        results = list()
        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                compare = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare = 'max'
            else:
                compare = 'equal'
            for obj in self._class.object_list:
                if hasattr(obj, key) :
                    if compare == 'min':
                        if getattr(obj, key) >= value:
                            results.append(obj)
                    elif compare == 'max':
                        if getattr(obj,key) <= value:
                            results.append(obj)
                    else:
                        if getattr(obj,key) ==value:
                            results.append(obj)


        return results
